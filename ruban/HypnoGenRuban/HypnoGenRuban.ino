/* HYPNOGEN — RUBAN : le ruban LED de la carte HYPNOGEN piloté par l'appli du téléphone.
 *
 * Carte : Arduino Nano ESP32 (même brochage que HypnoGenNano : PWM R/V/B = D2/D3/D4, MOSFET IRLB8721).
 * Le téléphone garde l'interface et le son ; ce croquis ne fait que la lumière, par Bluetooth
 * basse consommation. Tout fonctionne hors ligne : liaison directe téléphone ↔ carte.
 *
 * Bibliothèque : BLE intégrée au paquet « esp32 » d'Espressif (2.x ou 3.x), rien à installer.
 * Réglage de la carte dans l'IDE : Arduino Nano ESP32, Pin Numbering « By Arduino pin » (défaut).
 *
 * Service GATT (UUID ci-dessous, à l'identique dans l'appli) :
 *   NOEUDS   écriture sans réponse : un ou plusieurs nœuds de 16 octets (voir ruban_core.h)
 *   SYNC     écriture de 4 octets (numéro) → notification de 8 octets (numéro, micros())
 *   CMD      écriture d'1 octet : 1 START, 2 PAUSE, 3 REPRISE, 4 FIN
 *   INFO     lecture : version du protocole et limites appliquées (texte)
 *
 * Sécurité, indépendante de l'appli : puissance du ruban plafonnée (LUM_MAX), plafonds bêta et
 * gamma calculés d'après la fréquence réellement produite, lumière coupée entre 26,5 et 33,5 Hz et
 * au-dessus de 46,5 Hz (l'appli s'arrête à 25, 35 et 45 Hz), extinction en 0,3 s dès que la liaison tombe ou que les nœuds manquent.
 */
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include "ruban_core.h"

#define NOM_BLE      "HYPNOGEN-RUBAN"
#define UUID_SERVICE "6f0c0001-5a1e-4b8e-9d3a-48594e4f474e"
#define UUID_NOEUDS  "6f0c0002-5a1e-4b8e-9d3a-48594e4f474e"
#define UUID_SYNC    "6f0c0003-5a1e-4b8e-9d3a-48594e4f474e"
#define UUID_CMD     "6f0c0004-5a1e-4b8e-9d3a-48594e4f474e"
#define UUID_INFO    "6f0c0005-5a1e-4b8e-9d3a-48594e4f474e"
#define PROTOCOLE    1

static const int PIN_R = D2, PIN_V = D3, PIN_B = D4;
static const uint32_t PWM_HZ = 10000;        // fréquence prévue par le filtre de la carte PWR
static const uint8_t  PWM_BITS = 12;
static const uint32_t PWM_MAX = (1u << PWM_BITS) - 1;

static ruban::Moteur moteur;
static portMUX_TYPE verrou = portMUX_INITIALIZER_UNLOCKED;
static BLECharacteristic* cSync = nullptr;
static volatile bool aRelancer = false;

/* ---------- PWM ---------- */
static void pwmInit() {
#if ESP_ARDUINO_VERSION_MAJOR >= 3
  ledcAttach(PIN_R, PWM_HZ, PWM_BITS); ledcAttach(PIN_V, PWM_HZ, PWM_BITS); ledcAttach(PIN_B, PWM_HZ, PWM_BITS);
#else
  ledcSetup(0, PWM_HZ, PWM_BITS); ledcSetup(1, PWM_HZ, PWM_BITS); ledcSetup(2, PWM_HZ, PWM_BITS);
  ledcAttachPin(PIN_R, 0); ledcAttachPin(PIN_V, 1); ledcAttachPin(PIN_B, 2);
#endif
}
static inline uint32_t enPwm(float v) { if (v <= 0) return 0; if (v >= 1) return PWM_MAX; return (uint32_t)(v * PWM_MAX + 0.5f); }
static void pwmEcrire(float r, float v, float b) {
#if ESP_ARDUINO_VERSION_MAJOR >= 3
  ledcWrite(PIN_R, enPwm(r)); ledcWrite(PIN_V, enPwm(v)); ledcWrite(PIN_B, enPwm(b));
#else
  ledcWrite(0, enPwm(r)); ledcWrite(1, enPwm(v)); ledcWrite(2, enPwm(b));
#endif
}

/* ---------- tâche lumière : 1 kHz, cœur 1 (le Bluetooth tourne sur le cœur 0) ---------- */
static void tacheLumiere(void*) {
  TickType_t reveil = xTaskGetTickCount();
  for (;;) {
    ruban::Sortie s;
    portENTER_CRITICAL(&verrou);
    s = moteur.calculer((uint32_t)micros());
    portEXIT_CRITICAL(&verrou);
    pwmEcrire(s.r, s.g, s.b);
    vTaskDelayUntil(&reveil, 1);              // 1 tick = 1 ms (CONFIG_FREERTOS_HZ = 1000)
  }
}

/* ---------- Bluetooth ---------- */
class RappelsServeur : public BLEServerCallbacks {
  void onConnect(BLEServer*) override {
    portENTER_CRITICAL(&verrou); moteur.connecte = true; portEXIT_CRITICAL(&verrou);
    Serial.println("Telephone connecte");
  }
  void onDisconnect(BLEServer*) override {
    portENTER_CRITICAL(&verrou); moteur.deconnexion(); portEXIT_CRITICAL(&verrou);
    aRelancer = true;                          // la publicité reprend depuis loop()
    Serial.println("Telephone deconnecte : lumiere coupee");
  }
};
class RappelsNoeuds : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic* c) override {
    auto v = c->getValue();                    // std::string (2.x) ou String (3.x)
    portENTER_CRITICAL(&verrou);
    moteur.ajouter((const uint8_t*)v.c_str(), (int)v.length());
    portEXIT_CRITICAL(&verrou);
  }
};
class RappelsSync : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic* c) override {
    uint32_t t = (uint32_t)micros();           // daté au plus près de la réception
    auto v = c->getValue();
    if (v.length() < 4) return;
    uint8_t r[8]; memcpy(r, v.c_str(), 4);
    r[4] = t; r[5] = t >> 8; r[6] = t >> 16; r[7] = t >> 24;
    cSync->setValue(r, 8); cSync->notify();
  }
};
class RappelsCmd : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic* c) override {
    auto v = c->getValue();
    if (v.length() < 1) return;
    portENTER_CRITICAL(&verrou); moteur.commande((uint8_t)v[0]); portEXIT_CRITICAL(&verrou);
  }
};

void setup() {
  Serial.begin(115200);
  pwmInit(); pwmEcrire(0, 0, 0);
  pinMode(LED_BUILTIN, OUTPUT);

  BLEDevice::init(NOM_BLE);
  BLEDevice::setMTU(185);                      // plusieurs nœuds par écriture quand le téléphone l'accepte
  BLEServer* srv = BLEDevice::createServer();
  srv->setCallbacks(new RappelsServeur());
  BLEService* svc = srv->createService(UUID_SERVICE);

  BLECharacteristic* cN = svc->createCharacteristic(UUID_NOEUDS, BLECharacteristic::PROPERTY_WRITE_NR | BLECharacteristic::PROPERTY_WRITE);
  cN->setCallbacks(new RappelsNoeuds());
  cSync = svc->createCharacteristic(UUID_SYNC, BLECharacteristic::PROPERTY_WRITE | BLECharacteristic::PROPERTY_WRITE_NR | BLECharacteristic::PROPERTY_NOTIFY);
  cSync->addDescriptor(new BLE2902());         // abonnement aux notifications (ajouté d'office en 3.x récent)
  cSync->setCallbacks(new RappelsSync());
  BLECharacteristic* cC = svc->createCharacteristic(UUID_CMD, BLECharacteristic::PROPERTY_WRITE | BLECharacteristic::PROPERTY_WRITE_NR);
  cC->setCallbacks(new RappelsCmd());
  BLECharacteristic* cI = svc->createCharacteristic(UUID_INFO, BLECharacteristic::PROPERTY_READ);
  char info[96];
  snprintf(info, sizeof info, "HYPNOGEN-RUBAN p%d lum%.2f beta%.0f-%.0f gamma%.0f-%.0f", PROTOCOLE,
           ruban::LUM_MAX, ruban::F_SURE, ruban::F_COUPE_BAS, ruban::F_GAMMA_MIN, ruban::F_GAMMA_MAX);
  cI->setValue((uint8_t*)info, strlen(info));
  svc->start();

  BLEAdvertising* pub = BLEDevice::getAdvertising();
  pub->addServiceUUID(UUID_SERVICE);
  pub->setScanResponse(true);
  BLEDevice::startAdvertising();

  xTaskCreatePinnedToCore(tacheLumiere, "lumiere", 4096, nullptr, 5, nullptr, 1);
  Serial.println("HYPNOGEN-RUBAN pret, en attente du telephone");
}

void loop() {
  if (aRelancer) { aRelancer = false; delay(200); BLEDevice::startAdvertising(); }
  // témoin : clignote en attente, fixe une fois le téléphone connecté
  bool c; portENTER_CRITICAL(&verrou); c = moteur.connecte; portEXIT_CRITICAL(&verrou);
  digitalWrite(LED_BUILTIN, c ? HIGH : (millis() / 500) & 1);
  delay(50);
}
