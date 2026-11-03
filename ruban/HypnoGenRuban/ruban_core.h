/* HYPNOGEN — ruban LED piloté par le téléphone : noyau du calcul de la lumière.
 *
 * Aucune dépendance Arduino : ce fichier est compilé tel quel par le croquis et par le banc
 * de test sur PC (test/test_ruban.cpp). Toute la logique de sécurité est ici.
 *
 * Principe (le même que l'appli et le firmware principal : une seule phase, deux lecteurs).
 * Le téléphone calcule la phase du battement et l'envoie en avance, par « nœuds » espacés de
 * 50 ms, datés sur l'horloge de l'ESP32 (micros()). Entre deux nœuds, la phase est interpolée
 * linéairement : à fréquence constante c'est exact, et une rampe varie de moins d'un millième
 * de hertz en 50 ms. La fréquence n'est pas transmise : elle est déduite ici de la pente de la
 * phase, ce qui rend les plafonds de sécurité indépendants de ce que dit le téléphone.
 *
 * Format d'un nœud, 16 octets, petit-boutiste :
 *   u32 t      instant d'affichage, micros() de l'ESP32 (repli modulo 2^32 géré)
 *   u32 ph     phase en cycles, virgule fixe Q16.16 (repli modulo 65536 cycles géré)
 *   u16 a      amplitude lumineuse linéaire, 0..65535 (lumière × enveloppe, plafonds de l'appli inclus)
 *   u8  prof   profondeur 0..255 (creux = 1 - prof)
 *   u8  mix    forme d'onde : 0 = sinus, 255 = impulsion
 *   u8  duty   largeur de l'impulsion, en 1/256 de cycle (115 ≈ 0,45 comme l'appli)
 *   u8  r,g,b  couleur 0..255 (sans rouge saturé, déjà appliqué par l'appli)
 */
#pragma once
#include <stdint.h>
#include <string.h>
#include <math.h>

namespace ruban {

/* ---------- limites de sécurité, appliquées ici quoi que demande le téléphone ---------- */
static const float LUM_MAX      = 0.50f;  // puissance maximale du ruban (ruban 12 V : très lumineux)
static const float F_SURE       = 14.0f;  // jusqu'ici, aucune restriction
static const float F_BETA       = 25.0f;  // zone bêta 15–25 Hz : lumière bridée (jusqu'à la coupure)
static const float BETA_LUM     = 0.40f;  //   lumière <= 40 %
static const float BETA_PROF    = 0.50f;  //   profondeur <= 50 %, sinus imposé
/* Coupures, avec une marge de 1,5 Hz sur les limites de l'appli (25, 35 et 45 Hz) : la fréquence est lue sur la
   pente de la phase, et l'appli peut faire glisser l'horloge de 2 % au plus pour absorber ses recalages. */
static const float F_COUPE_BAS  = 26.5f;  // 26,5–33,5 Hz : lumière coupée (l'appli ne passe jamais entre 25 et 35)
static const float F_GAMMA_MIN  = 33.5f;  // gamma de 33,5 à 46,5 Hz
static const float F_GAMMA_MAX  = 46.5f;  // au-delà : lumière coupée
static const float GAMMA_LUM    = 0.50f;  // gamma : lumière <= 50 %
static const float BETA_MAX_S   = 660.f;  // filet : 11 min de bêta par séance (l'appli s'arrête à 10)
static const float GAMMA_MAX_S  = 1260.f; // filet : 21 min de gamma par séance (l'appli s'arrête à 20)
static const uint32_t FONDU_PAUSE_US = 30000;   // un appui sur le téléphone : extinction en 30 ms
static const uint32_t FONDU_FIN_US   = 150000;  // fin de séance
static const uint32_t FONDU_MANQUE_US= 300000;  // plus de nœud à venir (liaison perdue) : extinction en 0,3 s
static const uint32_t FONDU_ENTREE_US= 300000;

static const int NB = 128;                // tampon : 6,4 s de nœuds à 50 ms

struct Noeud { uint32_t t; uint32_t ph; uint16_t a; uint8_t prof, mix, duty, r, g, b; };

static inline Noeud decoder(const uint8_t* d) {
  Noeud n;
  n.t  = (uint32_t)d[0] | (uint32_t)d[1] << 8 | (uint32_t)d[2] << 16 | (uint32_t)d[3] << 24;
  n.ph = (uint32_t)d[4] | (uint32_t)d[5] << 8 | (uint32_t)d[6] << 16 | (uint32_t)d[7] << 24;
  n.a  = (uint16_t)(d[8] | d[9] << 8);
  n.prof = d[10]; n.mix = d[11]; n.duty = d[12]; n.r = d[13]; n.g = d[14]; n.b = d[15];
  return n;
}

static inline float lisse(float x) { if (x <= 0) return 0; if (x >= 1) return 1; return x * x * (3 - 2 * x); }

/* même impulsion que l'appli (montée et descente brèves, plateau), largeur variable */
static inline float impulsion(float x, float d) {
  float e = d / 5; if (e > 0.03f) e = 0.03f; if (e < 0.002f) e = 0.002f;
  if (x < e) return x / e;
  if (x < d) return 1;
  if (x < d + e) return 1 - (x - d) / e;
  return 0;
}

enum Cmd : uint8_t { CMD_START = 1, CMD_PAUSE = 2, CMD_REPRISE = 3, CMD_FIN = 4 };

struct Sortie { float r, g, b; float f; bool active; };

class Moteur {
public:
  Noeud q[NB]; int tete = 0, n = 0;       // file circulaire, dans l'ordre des temps
  float porte = 0;                         // fondu global 0..1
  bool pause = false, fin = true, connecte = false;
  uint32_t dernier = 0; bool premier = true;
  float tBeta = 0, tGamma = 0;             // secondes passées dans chaque zone depuis START
  float fEst = 0;
  uint32_t nRefus = 0;

  void commande(uint8_t c) {
    if (c == CMD_START) { n = 0; tete = 0; pause = false; fin = false; tBeta = tGamma = 0; }
    else if (c == CMD_PAUSE) pause = true;
    else if (c == CMD_REPRISE) pause = false;
    else if (c == CMD_FIN) fin = true;
  }
  void deconnexion() { connecte = false; }

  /* ajoute des nœuds (multiple de 16 octets) ; un nœud qui ne suit pas le précédent est refusé */
  void ajouter(const uint8_t* d, int len) {
    for (int i = 0; i + 16 <= len; i += 16) {
      Noeud x = decoder(d + i);
      if (n > 0) {
        const Noeud& p = q[(tete + n - 1) % NB];
        int32_t dt = (int32_t)(x.t - p.t);
        if (dt <= 0 || dt > 2000000) { nRefus++; continue; }
      }
      if (n == NB) { tete = (tete + 1) % NB; n--; }
      q[(tete + n) % NB] = x; n++;
    }
  }

  /* état de la lumière à l'instant now (micros), appelé environ toutes les millisecondes */
  Sortie calculer(uint32_t now) {
    Sortie s = {0, 0, 0, 0, false};
    float dts = premier ? 0 : (int32_t)(now - dernier) * 1e-6f; premier = false; dernier = now;
    if (dts < 0 || dts > 0.1f) dts = 0;

    // segment [a, b] qui contient now ; les nœuds dépassés sont retirés
    while (n >= 2 && (int32_t)(now - q[(tete + 1) % NB].t) >= 0) { tete = (tete + 1) % NB; n--; }
    bool segment = n >= 2 && (int32_t)(now - q[tete].t) >= 0;

    float cible = (segment && !pause && !fin && connecte) ? 1.f : 0.f;
    uint32_t tau = fin ? FONDU_FIN_US : pause ? FONDU_PAUSE_US : !segment || !connecte ? FONDU_MANQUE_US : FONDU_ENTREE_US;
    float pas = dts * 1e6f / tau;
    porte = cible > porte ? fminf(cible, porte + pas) : fmaxf(cible, porte - pas);

    if (!segment) { fEst = 0; return s; }
    const Noeud& a = q[tete]; const Noeud& b = q[(tete + 1) % NB];
    float D = (int32_t)(b.t - a.t) * 1e-6f;
    float u = (int32_t)(now - a.t) * 1e-6f / D;
    float dph = (int32_t)(b.ph - a.ph) / 65536.f;            // cycles entre les deux nœuds
    float f = dph / D; fEst = f;
    float ph = (a.ph & 0xFFFF) / 65536.f + dph * u;
    float x = ph - floorf(ph);

    float A = (a.a + (b.a - a.a) * u) / 65535.f;
    float prof = (a.prof + (b.prof - a.prof) * u) / 255.f;
    float mix = (a.mix + (b.mix - a.mix) * u) / 255.f;
    float duty = (a.duty + (b.duty - a.duty) * u) / 256.f;
    float r = a.r + (b.r - a.r) * u, g = a.g + (b.g - a.g) * u, bl = a.b + (b.b - a.b) * u;

    // ---- plafonds selon la fréquence réellement produite ----
    float lumMax = 1, profMax = 1, coupe = 1;
    if (f < 0 || f > F_GAMMA_MAX) coupe = 0;
    else if (f > F_COUPE_BAS && f < F_GAMMA_MIN) coupe = 0;
    else if (f >= F_GAMMA_MIN) { lumMax = GAMMA_LUM; tGamma += dts * porte; if (tGamma > GAMMA_MAX_S) coupe = 0; }
    else {
      float z = lisse(f - F_SURE);                          // fondu entre 14 et 15 Hz, comme l'appli
      lumMax = 1 - z * (1 - BETA_LUM); profMax = 1 - z * (1 - BETA_PROF);
      mix *= 1 - z;
      if (f > F_SURE) { tBeta += dts * porte; if (tBeta > BETA_MAX_S) coupe = 0; }
    }
    if (A > lumMax) A = lumMax;
    if (prof > profMax) prof = profMax;

    float onde = (1 + cosf(6.2831853f * x)) / 2 * (1 - mix) + impulsion(x, duty) * mix;
    float v = ((1 - prof) + prof * onde) * A * porte * coupe * LUM_MAX;
    s.r = v * r / 255; s.g = v * g / 255; s.b = v * bl / 255; s.f = f; s.active = v > 0;
    return s;
  }
};

}  // namespace ruban
