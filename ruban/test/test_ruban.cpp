// Banc de test sur PC du noyau ruban_core.h : g++ -O2 -std=c++17 test_ruban.cpp -o t && ./t
#include "../HypnoGenRuban/ruban_core.h"
#include <cstdio>
#include <vector>
#include <cmath>
using namespace ruban;

static int ok = 0, ko = 0;
static void verif(bool c, const char* m) { if (c) { ok++; printf("  ok  %s\n", m); } else { ko++; printf("  ÉCHEC %s\n", m); } }

static void poser(uint8_t* d, uint32_t t, double ph, float a, float prof, float mix, float duty, uint8_t r, uint8_t g, uint8_t b) {
  uint32_t q = (uint32_t)(int64_t)llround(ph * 65536.0);
  uint16_t A = (uint16_t)lroundf(a * 65535);
  uint8_t v[16] = {(uint8_t)t, (uint8_t)(t >> 8), (uint8_t)(t >> 16), (uint8_t)(t >> 24),
                   (uint8_t)q, (uint8_t)(q >> 8), (uint8_t)(q >> 16), (uint8_t)(q >> 24),
                   (uint8_t)A, (uint8_t)(A >> 8), (uint8_t)lroundf(prof * 255), (uint8_t)lroundf(mix * 255),
                   (uint8_t)lroundf(duty * 256), r, g, b};
  memcpy(d, v, 16);
}
/* séance simulée : fréquence f(t) en Hz, nœuds tous les 50 ms à partir de t0 (µs, repli possible) */
struct Sim {
  Moteur m; uint32_t t0; double ph = 0; double tn = 0;
  float a = 1, prof = 1, mix = 0, duty = 0.45f; uint8_t r = 255, g = 236, b = 210;
  explicit Sim(uint32_t depart) : t0(depart) { m.connecte = true; m.commande(CMD_START); }
  template <class F> void envoyer(double jusqua, F freq) {
    while (tn <= jusqua) {
      uint8_t d[16]; poser(d, t0 + (uint32_t)llround(tn * 1e6), ph, a, prof, mix, duty, r, g, b);
      m.ajouter(d, 16);
      double f0 = freq(tn), f1 = freq(tn + 0.05); ph += (f0 + f1) / 2 * 0.05; tn += 0.05;
    }
  }
  Sortie a_t(double s) { return m.calculer(t0 + (uint32_t)llround(s * 1e6)); }
};
static float lum(const Sortie& s) { return std::max(s.r, std::max(s.g, s.b)); }

int main() {
  printf("1. Phase et fréquence d'un palier à 10 Hz\n");
  {
    Sim s(1000); s.envoyer(3, [](double) { return 10.0; });
    float fmin = 99, fmax = 0, err = 0;
    for (double t = 0; t < 2.5; t += 0.001) {
      Sortie o = s.a_t(t); fmin = fminf(fmin, o.f); fmax = fmaxf(fmax, o.f);
      // sinus pur, profondeur 1 : la lumière vaut LUM_MAX*(1+cos 2πft)/2 (×g/255 sur le vert)
      double att = LUM_MAX * (1 + cos(2 * M_PI * 10 * t)) / 2 * 236 / 255.0;
      if (t > 0.4) err = fmaxf(err, fabs(o.g - att));
    }
    verif(fabsf(fmin - 10) < 1e-3 && fabsf(fmax - 10) < 1e-3, "fréquence déduite de la pente : 10 Hz");
    char m[96]; snprintf(m, sizeof m, "forme du signal conforme (écart max %.4f)", err);
    verif(err < 0.01, m);
  }
  printf("2. Plafond de puissance\n");
  {
    Sim s(0); s.envoyer(2, [](double) { return 5.0; }); float mx = 0;
    for (double t = 0; t < 1.5; t += 0.0005) { float v = lum(s.a_t(t)); if (t > 0.5) mx = fmaxf(mx, v); }
    verif(mx <= LUM_MAX + 1e-4 && mx > LUM_MAX * 0.95f, "crête au plus LUM_MAX");
  }
  printf("3. Zone bêta : le firmware bride même si l'appli ne le fait pas\n");
  {
    Sim s(0); s.mix = 1; s.prof = 1; s.envoyer(3, [](double) { return 20.0; });
    float mx = 0, mn = 9;
    for (double t = 0; t < 2; t += 0.0002) { float v = s.a_t(t).r; if (t > 1) { mx = fmaxf(mx, v); mn = fminf(mn, v); } }
    char m[128]; snprintf(m, sizeof m, "20 Hz : crête %.3f <= %.3f, creux %.3f >= moitié de la crête", mx, LUM_MAX * BETA_LUM, mn);
    verif(mx <= LUM_MAX * BETA_LUM + 1e-4 && mn >= mx * 0.5f - 1e-3, m);
  }
  printf("4. Fondu des plafonds entre 14 et 15 Hz\n");
  {
    float pics[3]; double fs[3] = {14, 14.5, 15};
    for (int k = 0; k < 3; k++) {
      Sim s(0); double f = fs[k]; s.envoyer(2, [f](double) { return f; }); float mx = 0;
      for (double t = 0; t < 1.5; t += 0.0002) { float v = s.a_t(t).r; if (t > 0.8) mx = fmaxf(mx, v); }
      pics[k] = mx / LUM_MAX;
    }
    char m[96]; snprintf(m, sizeof m, "crêtes %.2f / %.2f / %.2f", pics[0], pics[1], pics[2]);
    verif(pics[0] > 0.99f && fabsf(pics[1] - 0.7f) < 0.02f && fabsf(pics[2] - BETA_LUM) < 0.01f, m);
  }
  printf("5. Bande 25–35 Hz et au-delà de 45 Hz : noir\n");
  {
    for (double f : {28.0, 32.0, 50.0}) {
      Sim s(0); s.envoyer(2, [f](double) { return f; }); float mx = 0;
      for (double t = 0; t < 1.5; t += 0.0002) { float v = lum(s.a_t(t)); if (t > 0.5) mx = fmaxf(mx, v); }
      char m[64]; snprintf(m, sizeof m, "%.0f Hz : lumière %.4f", f, mx); verif(mx == 0, m);
    }
  }
  printf("6. Gamma 40 Hz : 50 %% au plus, impulsion autorisée\n");
  {
    Sim s(0); s.mix = 1; s.duty = 0.45f; s.envoyer(3, [](double) { return 40.0; });
    float mx = 0; int on = 0, tot = 0;
    for (double t = 0; t < 2; t += 0.0001) { float v = s.a_t(t).r; if (t < 0.5) continue; if (t < 1) { mx = fmaxf(mx, v); continue; } tot++; if (v > 0.5f * mx) on++; }
    char m[96]; snprintf(m, sizeof m, "crête %.3f, rapport cyclique ≈ %.2f", mx / LUM_MAX, (double)on / tot);
    verif(fabsf(mx - LUM_MAX * GAMMA_LUM) < 1e-3 && fabsf((double)on / tot - 0.47) < 0.05, m);
  }
  printf("7. Liaison perdue : extinction en 0,3 s\n");
  {
    Sim s(0); s.envoyer(1.0, [](double) { return 8.0; });
    float avant = 0; for (double t = 0; t < 0.9; t += 0.001) avant = fmaxf(avant, lum(s.a_t(t)));
    float apres = 9; for (double t = 1.0; t < 1.4; t += 0.001) { Sortie o = s.a_t(t); if (t > 1.31) apres = fminf(apres, -lum(o)); }
    verif(avant > 0.4f * LUM_MAX && -apres == 0, "plus de nœud à venir : noir après 0,3 s");
    Sim s2(0); s2.envoyer(3, [](double) { return 8.0; }); s2.a_t(0.5); s2.m.deconnexion();
    float v = 0; for (double t = 0.5; t < 0.85; t += 0.001) v = lum(s2.a_t(t));
    verif(v == 0, "déconnexion : noir en 0,3 s malgré les nœuds en tampon");
  }
  printf("8. Pause : 30 ms\n");
  {
    Sim s(0); s.envoyer(3, [](double) { return 6.0; }); for (double t = 0.3; t < 1; t += 0.001) s.a_t(t);
    s.m.commande(CMD_PAUSE); float v = 1; for (double t = 1; t < 1.035; t += 0.001) v = lum(s.a_t(t));
    verif(v == 0, "noir 35 ms après PAUSE");
    s.m.commande(CMD_REPRISE); for (double t = 1.035; t < 1.5; t += 0.001) v = fmaxf(v, lum(s.a_t(t)));
    verif(v > 0, "REPRISE rallume");
  }
  printf("9. Repli de micros() (71,6 min) et de la phase Q16.16\n");
  {
    Sim s(0xFFFFFFFFu - 500000); s.ph = 65535.5; s.envoyer(2, [](double) { return 12.0; });
    float fmin = 99, fmax = 0;
    for (double t = 0; t < 1.8; t += 0.001) { Sortie o = s.a_t(t); fmin = fminf(fmin, o.f); fmax = fmaxf(fmax, o.f); }
    char m[96]; snprintf(m, sizeof m, "fréquence stable à travers les deux replis : %.3f–%.3f Hz", fmin, fmax);
    verif(fabsf(fmin - 12) < 1e-3 && fabsf(fmax - 12) < 1e-3, m);
  }
  printf("10. Rampe 10 → 6 Hz : phase continue\n");
  {
    Sim s(0); auto F = [](double t) { return 10 - 4 * fmin(1.0, t / 2); }; s.envoyer(3, F);
    double ph = 0, tp = 0, err = 0;
    for (double t = 0; t < 2.5; t += 0.001) {
      Sortie o = s.a_t(t); if (t > 0) ph += F(t - 0.0005) * (t - tp); tp = t;
      if (t > 0.4) { double att = LUM_MAX * (1 + cos(2 * M_PI * ph)) / 2; err = fmax(err, fabs(o.r - att)); }
    }
    char m[64]; snprintf(m, sizeof m, "écart à la phase exacte %.4f", err); verif(err < 0.01, m);
  }
  printf("11. Nœuds hors d'ordre refusés, tampon plein sans débordement\n");
  {
    Sim s(0); s.envoyer(1, [](double) { return 5.0; }); uint8_t d[16]; poser(d, 100, 0, 1, 1, 0, .45f, 1, 1, 1);
    s.m.ajouter(d, 16); verif(s.m.nRefus == 1, "nœud antérieur refusé");
    Sim s2(0); s2.envoyer(20, [](double) { return 5.0; }); verif(s2.m.n == NB, "tampon limité à NB nœuds");
  }
  printf("12. Filet de durée bêta : coupé après 11 min\n");
  {
    Sim s(0); float v1 = 0, v2 = 0;
    for (double t = 0; t < 700; t += 0.001) { s.envoyer(t + 0.8, [](double) { return 18.0; }); float v = lum(s.a_t(t)); if (t > 600 && t < 650) v1 = fmaxf(v1, v); if (t > 665) v2 = fmaxf(v2, v); }
    verif(v1 > 0 && v2 == 0, "allumé à 10 min, noir après 11 min");
  }
  printf("\n%d réussis, %d échecs\n", ok, ko);
  return ko ? 1 : 0;
}
