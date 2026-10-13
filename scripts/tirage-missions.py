"""Tirage au sort des missions de l'agence, vendredi 9 octobre 2026.

Les règles :
- quatre missions, A1, A2, C1 et C2, deux équipes par mission : huit équipes ;
- neuf équipes : une mission, tirée au sort, en accueille trois ;
- les trinômes sont tirés sur une même mission quand c'est possible, par
  équité ; s'ils sont trop nombreux pour une seule mission, ils en occupent
  le moins possible ;
- les missions tirées sont définitives.

Comment : la graine fixe tout le tirage. Avec neuf équipes, elle désigne
d'abord la mission qui en accueille trois. Puis les places sont mélangées,
autant de fois qu'il le faut pour que les trinômes soient regroupés. Tous les
tirages qui respectent la règle ont ainsi la même chance d'être retenus :
c'est un tirage sous condition, au sens des probabilités conditionnelles.

Reproductible : le même nombre d'équipes, les mêmes trinômes et la même
graine donnent le même résultat, sur n'importe quel ordinateur muni de
Python 3. Aucun nom : les équipes sont numérotées de 1 à N avant le tirage
de la graine, et la correspondance entre numéros et équipes reste dans la
salle.

Usage :
    python3 tirage-missions.py --equipes 8 --graine 3516
    python3 tirage-missions.py --equipes 8 --trinomes 3 6 --graine 3516
    python3 tirage-missions.py --equipes 9 --trinomes 3 6 --graine 3516
    python3 tirage-missions.py --equipes 8 --trinomes 3 6 --graine 3516 --simuler

Le tirage du vendredi 9 octobre 2026 : huit équipes, dont deux trinômes, les
équipes 3 et 6 ; graine 8532. Pour le refaire :
    python3 tirage-missions.py --equipes 8 --trinomes 3 6 --graine 8532

Licence : versé dans le domaine public, CC0 1.0
(https://creativecommons.org/publicdomain/zero/1.0/deed.fr).
"""
from __future__ import annotations

import argparse
import random
from collections import Counter
from fractions import Fraction
from itertools import permutations

MISSIONS = {
    "A1": "Les annulations",
    "A2": "Recommandé par l'IA",
    "C1": "Le temps d'attente",
    "C2": "Les robots de service",
}


def decimal(x: float) -> str:
    """0,250 plutôt que 0.250."""
    return f"{x:.3f}".replace(".", ",")


def enumeration(nombres: list[int]) -> str:
    """3 et 6 ; 1, 3 et 6."""
    textes = [str(n) for n in nombres]
    return textes[0] if len(textes) == 1 else ", ".join(textes[:-1]) + " et " + textes[-1]


def verifier(equipes: int, trinomes: list[int]) -> None:
    if equipes not in (8, 9):
        raise SystemExit("Le tirage prévoit 8 ou 9 équipes ; hors de ces cas, la règle est à arbitrer.")
    if len(set(trinomes)) != len(trinomes) or any(not 1 <= t <= equipes for t in trinomes):
        raise SystemExit(f"Trinômes invalides : {trinomes}. Donner des numéros d'équipe distincts, de 1 à {equipes}.")


def places(triple: str | None) -> list[str]:
    """Une entrée par place : deux par mission, trois pour la mission désignée s'il y a neuf équipes."""
    return [m for m in MISSIONS for _ in range(3 if m == triple else 2)]


def minimum(liste: list[str], nb_trinomes: int) -> int:
    """Le plus petit nombre de missions qui peut accueillir tous les trinômes."""
    capacites = sorted(Counter(liste).values(), reverse=True)
    total = k = 0
    while total < nb_trinomes:
        total += capacites[k]
        k += 1
    return k


def regroupes(missions_des_trinomes: list[str], k: int) -> bool:
    return len(set(missions_des_trinomes)) == k


def tirer(hasard: random.Random, equipes: int, trinomes: list[int]) -> tuple[str | None, list[str], int]:
    """La mission à trois équipes s'il y a lieu, puis un mélange des places qui regroupe les trinômes.

    L'équipe n reçoit la n-ième place du mélange. Renvoie aussi le nombre de mélanges tirés.
    """
    triple = hasard.choice(list(MISSIONS)) if equipes == 9 else None
    liste = places(triple)
    k = minimum(liste, len(trinomes))
    essais = 0
    while True:
        essais += 1
        melange = list(liste)
        hasard.shuffle(melange)
        if regroupes([melange[t - 1] for t in trinomes], k):
            return triple, melange, essais


def loi_exacte(equipe: int, equipes: int, trinomes: list[int]) -> dict[str, Fraction]:
    """P(l'équipe obtient chaque mission), en dénombrant tous les tirages qui respectent la règle."""
    triples = list(MISSIONS) if equipes == 9 else [None]
    suivies = list(trinomes) + ([] if equipe in trinomes else [equipe])
    loi = {m: Fraction(0) for m in MISSIONS}
    for triple in triples:                          # avec neuf équipes, chaque mission a 1 chance sur 4
        liste = places(triple)
        k = minimum(liste, len(trinomes))
        favorables, total = Counter(), 0
        for choix in permutations(range(len(liste)), len(suivies)):
            missions = [liste[c] for c in choix]
            if regroupes(missions[:len(trinomes)], k):
                total += 1
                favorables[missions[suivies.index(equipe)]] += 1
        for m in MISSIONS:
            loi[m] += Fraction(favorables[m], total) / len(triples)
    return loi


def proportion_regroupee(equipes: int, trinomes: list[int]) -> Fraction:
    """La part des mélanges qui regroupent les trinômes (la même quelle que soit la mission à trois)."""
    liste = places("A1" if equipes == 9 else None)
    k = minimum(liste, len(trinomes))
    choix = list(permutations(range(len(liste)), len(trinomes)))
    bons = sum(regroupes([liste[c] for c in tuple_], k) for tuple_ in choix)
    return Fraction(bons, len(choix))


def afficher_probabilites(equipes: int, trinomes: list[int]) -> None:
    lois = {e: loi_exacte(e, equipes, trinomes) for e in range(1, equipes + 1)}
    if not trinomes:
        print(f"{equipes} équipes, sans trinôme.")
    elif len(trinomes) == 1:
        print(f"{equipes} équipes, dont un trinôme : l'équipe {trinomes[0]}.")
    else:
        print(f"{equipes} équipes, dont {len(trinomes)} trinômes : les équipes {enumeration(trinomes)}.")
    if equipes == 9:
        print("Neuf équipes : une mission, tirée au sort, en accueillera trois.")
    if all(lois[e] == lois[1] for e in lois):
        print("\nChance, pour chaque équipe, binôme ou trinôme, d'obtenir chaque mission :")
        for m, titre in MISSIONS.items():
            p = lois[1][m]
            print(f"  {m} · {titre:22s} P = {p} ≈ {decimal(float(p))}")
    else:
        print("\nChance d'obtenir chaque mission, équipe par équipe :")
        for e, loi in lois.items():
            print(f"  Équipe {e:2d} : " + " ; ".join(f"{m} {loi[m]}" for m in MISSIONS))


def simuler(equipes: int, trinomes: list[int], repetitions: int = 100_000) -> None:
    """Fréquences observées sur de nombreux tirages, à comparer aux probabilités."""
    hasard = random.Random(0)
    suivies = [1] + [t for t in trinomes[:1] if t != 1]
    resultats = {e: Counter() for e in suivies}
    for _ in range(repetitions):
        _, melange, _ = tirer(hasard, equipes, trinomes)
        for e in suivies:
            resultats[e][melange[e - 1]] += 1
    nombre = f"{repetitions:,}".replace(",", " ")
    print(f"\nVérification : {nombre} tirages simulés")
    for e in suivies:
        nature = "trinôme" if e in trinomes else "binôme"
        frequences = " ; ".join(f"{m} {decimal(resultats[e][m] / repetitions)}" for m in MISSIONS)
        print(f"  Équipe {e} ({nature}) : {frequences}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tirage au sort des missions MTH101.")
    parser.add_argument("--equipes", type=int, required=True, help="nombre d'équipes : 8 ou 9")
    parser.add_argument("--trinomes", type=int, nargs="*", default=[], help="numéros des trinômes")
    parser.add_argument("--graine", type=int, required=True, help="la graine, tirée aux dés en séance")
    parser.add_argument("--simuler", action="store_true", help="comparer fréquences et probabilités")
    args = parser.parse_args()

    trinomes = sorted(args.trinomes)
    verifier(args.equipes, trinomes)
    afficher_probabilites(args.equipes, trinomes)
    if args.simuler:
        simuler(args.equipes, trinomes)

    triple, resultat, essais = tirer(random.Random(args.graine), args.equipes, trinomes)
    print(f"\nTirage avec la graine {args.graine} :")
    if triple:
        print(f"  Mission à trois équipes : {triple} · {MISSIONS[triple]}")
    if len(trinomes) > 1:
        p = proportion_regroupee(args.equipes, trinomes)
        print(f"  Trinômes regroupés au mélange n° {essais} ; un mélange sur {1 / p} les regroupe en moyenne."
              if p.numerator == 1 else
              f"  Trinômes regroupés au mélange n° {essais} ; probabilité qu'un mélange les regroupe : {p}.")
    for numero, m in enumerate(resultat, start=1):
        marque = " (trinôme)" if numero in trinomes else ""
        print(f"  Équipe {numero:2d}{marque:10s} → {m} · {MISSIONS[m]}")

    commande = f"python3 tirage-missions.py --equipes {args.equipes}"
    if trinomes:
        commande += " --trinomes " + " ".join(map(str, trinomes))
    print(f"\nPour vérifier : {commande} --graine {args.graine}")
