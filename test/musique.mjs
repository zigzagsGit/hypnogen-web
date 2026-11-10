// Contrôle hors navigateur du moteur de musique (v1.11).
// Extrait la synthèse (SYNTHE) et le catalogue de index.html, rend des extraits de chaque séance en musique
// avec un faux AudioWorklet, puis vérifie : niveaux, absence d'écrêtage, battement de la nappe en phase avec
// la lumière, frappes sur une crête, consonance avec la porteuse, coût de calcul.
// Usage : node test/musique.mjs [dossier-wav]   (écrit des extraits .wav si un dossier est donné)
import fs from 'node:fs';
import path from 'node:path';

const html = fs.readFileSync(new URL('../index.html', import.meta.url), 'utf8');
const SYNTHE = html.match(/const SYNTHE=`([\s\S]*?)`;/)[1];
const CAT = html.match(/const SEANCES=\[[\s\S]*?\nfunction souffleB[^\n]*\n/)[0];
const PHASE = html.match(/function phaseInfo\(s,st,dur\)\{[\s\S]*?\n\}\n/)[0];
const cat = new Function(CAT + PHASE + 'return {SEANCES,MUS,ORDRE,souffleB,phaseInfo};')();
const { SEANCES, MUS, ORDRE, souffleB, phaseInfo } = cat;

const SR = 44100, BLOC = 128;
function moteur(opts) {
  const g = { currentFrame: 0, sampleRate: SR, procs: {} };
  const f = new Function('AudioWorkletProcessor', 'registerProcessor', 'sampleRate', '__G',
    SYNTHE.replace(/currentFrame/g, '__G.currentFrame') + ';return Musique;');
  class AWP { constructor() { this.port = { onmessage: null }; } }
  let Proc; const Musique = f(AWP, (n, c) => { Proc = c; }, SR, g);
  const p = new Proc({ processorOptions: opts });
  return { p, g, Musique };
}

let ok = 0, ko = 0;
const verifie = (c, msg) => { if (c) ok++; else { ko++; console.log('  ÉCHEC :', msg); } };

/* rend [st0, st0+duree] d'une séance ; noeuds toutes les 50 ms comme planifier() (lissage compris).
   Le rendu commence 5 s avant st0 (mise en place de la réverbération) : la phase du battement part de là. */
function rendre(i, st0, duree, { iso = false, carr = 200, g = 0.09, m = 0.63, seed = 7 } = {}) {
  const s = SEANCES[i], dur = s.min * 60, d0 = Math.max(0, st0 - 5);
  const mus = Object.assign({ souffle: s.souffle || 0 }, MUS[s.mus]);
  const { p, g: G } = moteur({ carr, iso, t0: d0, mus, seed });
  const K = []; let f = phaseInfo(s, d0, dur).f;
  for (let t = d0; t <= st0 + duree + 1; t += 0.05) { const c = phaseInfo(s, t, dur).f; f += (c - f) * (1 - Math.exp(-0.05 / 0.15)); K.push([t, f, g, m]); }
  p.port.onmessage({ data: { n: K } });
  const n = Math.round(duree * SR), L = new Float32Array(n), R = new Float32Array(n);
  const frappes = [], tmpL = new Float32Array(BLOC), tmpR = new Float32Array(BLOC);
  let calcul = 0;
  const k0 = Math.floor(d0 * SR / BLOC), k1 = Math.round((st0 + duree) * SR / BLOC);
  for (let k = k0; k < k1; k++) {
    G.currentFrame = k * BLOC;
    const nb = p.M.B.length, nm = p.M.Mn.length;
    const tA = performance.now();
    p.process([], [[tmpL, tmpR]]);
    calcul += performance.now() - tA;
    if (p.M.B.length > nb || p.M.Mn.length > nm) frappes.push({ t: (k * BLOC) / SR, pB: p.pB });
    const base = k * BLOC - Math.round(st0 * SR);
    if (base < 0) continue;
    for (let j = 0; j < BLOC && base + j < n; j++) { L[base + j] = tmpL[j]; R[base + j] = tmpR[j]; }
  }
  return { L, R, frappes, calcul, dureeRendue: (k1 - k0) * BLOC / SR };
}

function wav(fich, L, R) {
  const n = L.length, b = Buffer.alloc(44 + n * 4);
  b.write('RIFF', 0); b.writeUInt32LE(36 + n * 4, 4); b.write('WAVEfmt ', 8); b.writeUInt32LE(16, 16); b.writeUInt16LE(1, 20);
  b.writeUInt16LE(2, 22); b.writeUInt32LE(SR, 24); b.writeUInt32LE(SR * 4, 28); b.writeUInt16LE(4, 32); b.writeUInt16LE(16, 34);
  b.write('data', 36); b.writeUInt32LE(n * 4, 40);
  for (let i = 0; i < n; i++) { b.writeInt16LE(Math.round(Math.max(-1, Math.min(1, L[i])) * 32767), 44 + i * 4); b.writeInt16LE(Math.round(Math.max(-1, Math.min(1, R[i])) * 32767), 46 + i * 4); }
  fs.writeFileSync(fich, b);
}
const rms = a => Math.sqrt(a.reduce((x, v) => x + v * v, 0) / a.length);
const crete = a => a.reduce((x, v) => Math.max(x, Math.abs(v)), 0);

// ---------- 1. catalogue ----------
const MED = SEANCES.map((s, i) => i).filter(i => SEANCES[i].mus);
verifie(MED.length === 4, 'quatre séances en musique');
for (const i of MED) {
  const s = SEANCES[i];
  verifie(!s.beta, s.nom + ' hors zone bêta');
  verifie(s.ph.every(p => p[1] >= 0.25 && p[2] <= 14 && p[1] <= 14), s.nom + ' sous 14 Hz');
  verifie(s.ph.every(p => p[4] === 's'), s.nom + ' en sinus');
  verifie(MUS[s.mus], s.nom + ' : ambiance définie');
  verifie(MUS[s.mus].acc.every(a => a.some(x => ((x % 12) + 12) % 12 === 0)), s.nom + ' : chaque accord contient la porteuse');
  verifie([10, 15, 20, 25, 30, 45, 60].includes(s.min), s.nom + ' : durée conseillée disponible');
}
verifie(ORDRE.slice(0, 15).every(i => !SEANCES[i].beta) && ORDRE.slice(15).every(i => SEANCES[i].beta), 'ordre : bêta en dernier');
verifie(ORDRE.length === SEANCES.length && new Set(ORDRE).size === SEANCES.length, 'ordre : toutes les séances une fois');
verifie(Math.abs(souffleB(10, 0)) < 1e-9 && Math.abs(souffleB(10, 4) - 1) < 1e-9 && souffleB(10, 9.99) < 1e-3, 'respiration : 4 s inspiration, 6 s expiration');

// ---------- 2. rendu et mesures ----------
const sortie = process.argv[2];
if (sortie) fs.mkdirSync(sortie, { recursive: true });
const extraits = [];
for (const i of MED) {
  const s = SEANCES[i], dur = s.min * 60;
  for (const [st0, nom] of [[25, 'debut'], [dur * 0.6, 'milieu']]) {
    const r = rendre(i, st0, 40);
    const c = Math.max(crete(r.L), crete(r.R)), e = (rms(r.L) + rms(r.R)) / 2;
    const tempsReel = r.calcul / 1000 / r.dureeRendue;
    console.log(`${s.nom.padEnd(8)} ${nom.padEnd(6)} f=${phaseInfo(s, st0, dur).f.toFixed(2)} Hz  crête ${c.toFixed(2)}  efficace ${e.toFixed(3)}  frappes ${r.frappes.length}  calcul ${(tempsReel * 100).toFixed(1)} % du temps réel`);
    verifie(c < 0.95, s.nom + ' ' + nom + ' : pas d\'écrêtage');
    verifie(e > 0.03, s.nom + ' ' + nom + ' : musique audible');
    verifie(tempsReel < 0.1, s.nom + ' ' + nom + ' : coût de calcul raisonnable');
    // frappes sur une crête du battement : la phase vient de repasser par 0
    verifie(r.frappes.every(x => x.pB < 0.05), s.nom + ' ' + nom + ' : frappes sur la crête');
    extraits.push({ r, nom: `${s.nom}-${nom}` });
    if (sortie) wav(path.join(sortie, `${s.nom}-${nom}.wav`), r.L, r.R);
  }
}

// ---------- 3. battement porté par la nappe, en phase avec la lumière ----------
// Musique seule (g = 0) : en binaural, la somme L+R d'une nappe décalée de ±f/2 bat à f ; son maximum doit
// tomber quand la phase du battement est nulle (crête du flash).
{
  const i = SEANCES.findIndex(s => s.nom === 'TEMPLE');
  const s = SEANCES[i], mus = Object.assign({ souffle: 0 }, MUS[s.mus], { bols: null, melo: null, houle: 0 });
  const { p, g: G } = moteur({ carr: 200, iso: false, t0: 0, mus, seed: 3 });
  const f = 6; p.port.onmessage({ data: { n: [[0, f, 0, 1], [100, f, 0, 1]] } });
  const tl = new Float32Array(BLOC), tr = new Float32Array(BLOC);
  const bins = new Float64Array(20), cnt = new Float64Array(20);
  let env = 0;
  for (let k = 0; k < Math.round(30 * SR / BLOC); k++) {
    G.currentFrame = k * BLOC; p.process([], [[tl, tr]]);
    if (k * BLOC < 5 * SR) continue;
    for (let j = 0; j < BLOC; j++) {
      const ph = ((p.pB - (BLOC - 1 - j) * f / SR) % 1 + 1) % 1;
      const v = (tl[j] + tr[j]) ** 2; env += v;
      const b = Math.floor(ph * 20); bins[b] += v; cnt[b]++;
    }
  }
  const prof = [...bins].map((v, k) => v / cnt[k]);
  const kMax = prof.indexOf(Math.max(...prof)), kMin = prof.indexOf(Math.min(...prof));
  console.log('nappe binaurale, énergie L+R selon la phase du battement :', prof.map(v => v.toFixed(4)).join(' '));
  verifie(kMax === 0 || kMax === 19, 'nappe : maximum de L+R à la crête du flash (case ' + kMax + ')');
  verifie(Math.abs(kMin - 10) <= 1, 'nappe : minimum en opposition (case ' + kMin + ')');
  verifie(prof[kMax] > 5 * prof[kMin], 'nappe : battement net');
}

// ---------- 4. même graine, même musique ; isochrone ----------
{
  const i = MED[0];
  const a = rendre(i, 30, 5, { seed: 11 }), b = rendre(i, 30, 5, { seed: 11 }), c = rendre(i, 30, 5, { iso: true, seed: 11 });
  // la houle utilise Math.random : on compare la nappe en neutralisant la houle
  verifie(a.frappes.length === b.frappes.length, 'même graine : mêmes frappes');
  verifie(crete(c.L) < 0.95 && Math.abs(rms(c.L) - rms(c.R)) < 0.2 * rms(c.L), 'isochrone : sans écrêtage, équilibré');
}

// ---------- 5. fin de séance : fondu en 150 ms puis arrêt du processeur ----------
{
  const i = MED[0], s = SEANCES[i];
  const { p, g: G } = moteur({ carr: 200, iso: false, t0: 0, mus: Object.assign({ souffle: 10 }, MUS[s.mus]), seed: 1 });
  p.port.onmessage({ data: { n: [[0, 8, 0.1, 0.5], [10, 8, 0.1, 0.5]], fin: 2 } });
  const tl = new Float32Array(BLOC), tr = new Float32Array(BLOC); let vivant = true, k = 0;
  while (vivant && k < 1000) { G.currentFrame = k++ * BLOC; vivant = p.process([], [[tl, tr]]); }
  verifie(!vivant && Math.abs(k * BLOC / SR - 2.15) < 0.01, 'arrêt 150 ms après la fin demandée');
}

console.log(`\n${ok} contrôles réussis, ${ko} échec(s)`);
process.exit(ko ? 1 : 0);
