// Rejoue dans le noyau du firmware des nœuds captés depuis l'appli (un nœud en hexadécimal par ligne)
// et affiche ce que le ruban produit : fréquence lue, crête, creux, rapport cyclique.
// g++ -O2 -std=c++17 rejouer.cpp -o rejouer && ./rejouer noeuds.hex
#include "../HypnoGenRuban/ruban_core.h"
#include <cstdio>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
int main(int argc, char** argv) {
  if (argc < 2) return 2;
  std::ifstream in(argv[1]); std::string l; std::vector<std::vector<uint8_t>> N;
  while (std::getline(in, l)) { std::istringstream s(l); std::string h; s >> h; if (h.size() != 32) continue;
    std::vector<uint8_t> b(16); for (int i = 0; i < 16; i++) b[i] = (uint8_t)std::stoi(h.substr(2 * i, 2), nullptr, 16); N.push_back(b); }
  if (N.size() < 3) { printf("trop peu de nœuds\n"); return 2; }
  ruban::Moteur m; m.connecte = true; m.commande(ruban::CMD_START);
  auto T = [&](size_t i) { return ruban::decoder(N[i].data()).t; };
  // on envoie chaque nœud 0,8 s avant son instant, comme le téléphone, et on calcule à 1 kHz
  size_t envoye = 0; uint32_t t0 = T(0), t1 = T(N.size() - 1);
  float fmin = 1e9, fmax = 0, crete = 0, creux = 1e9; long on = 0, tot = 0;
  for (uint32_t dt = 0; (int32_t)(t0 + dt - t1) < 0; dt += 1000) {
    uint32_t now = t0 + dt;
    while (envoye < N.size() && (int32_t)(T(envoye) - now) < 800000) { m.ajouter(N[envoye].data(), 16); envoye++; }
    ruban::Sortie o = m.calculer(now);
    if (dt > 500000) { float v = std::max(o.r, std::max(o.g, o.b)); fmin = std::min(fmin, o.f); fmax = std::max(fmax, o.f);
      crete = std::max(crete, v); creux = std::min(creux, v); tot++; if (v > 0.5f * ruban::LUM_MAX * 0.5f) on++; }
  }
  printf("%zu nœuds · fréquence lue %.2f–%.2f Hz · crête %.3f · creux %.3f (puissance max %.2f) · au-dessus de la mi-hauteur gamma %.0f %%\n",
         N.size(), fmin, fmax, crete, creux, ruban::LUM_MAX, 100.0 * on / tot);
  return 0;
}
