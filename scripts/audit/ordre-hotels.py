"""Ordre des cinq hôtels pour une requête de l'audit, mission « Recommandé par l'IA ».

À chaque requête, l'ordre dans lequel les cinq hôtels sont présentés à
l'assistant est tiré au sort. Ce script donne cet ordre pour la requête n,
et note la réponse de l'assistant dans le relevé.

Reproductible : la graine, choisie une fois par l'équipe et écrite dans le
plan d'audit avant la première requête, fixe tous les tirages. La même
graine, le même numéro de requête et les mêmes cinq hôtels donnent le même
ordre, sur n'importe quel ordinateur muni de Python 3. Chaque requête a son
propre tirage : les 120 ordres possibles y ont la même chance.

Avant la première requête, remplacez les cinq noms de HOTELS par ceux de
votre plan d'audit.

Usage, à la racine du dépôt :
    python3 projet/protocole/ordre-hotels.py --graine 4821 --requete 1
    python3 projet/protocole/ordre-hotels.py --graine 4821 --toutes 150
    python3 projet/protocole/ordre-hotels.py --graine 4821 --noter 1

Remplacez 4821 par la graine de votre équipe. --requete affiche l'ordre de
la requête 1 ; --toutes, les ordres des requêtes 1 à 150, un par ligne ;
--noter enregistre la réponse de la requête 1 dans
projet/donnees/releve-audit.csv : le script demande l'assistant, la réponse
complète (collée, puis FIN seul sur une ligne), l'hôtel recommandé, le
recours à une recherche web et les remarques. Il ajoute la date, l'heure de
Paris et l'ordre présenté. Bibliothèque standard seule.

Licence : versé dans le domaine public, CC0 1.0
(https://creativecommons.org/publicdomain/zero/1.0/deed.fr).
"""
from __future__ import annotations

import argparse
import csv
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

HOTELS = [
    "Hôtel A",
    "Hôtel B",
    "Hôtel C",
    "Hôtel D",
    "Hôtel E",
]

RELEVE = Path("projet/donnees/releve-audit.csv")
COLONNES = ["numero", "date", "heure", "assistant", "ordre_presente",
            "reponse_complete", "hotel_recommande", "recherche_web", "remarques"]


def ordre(graine: int, requete: int, hotels: list[str]) -> list[str]:
    """L'ordre tiré au sort pour la requête n : un tirage par requête."""
    tirage = random.Random(f"{graine}-{requete}")
    return tirage.sample(hotels, len(hotels))


def maintenant() -> tuple[str, str]:
    """La date et l'heure de Paris ; l'heure UTC, marquée, si le fuseau manque."""
    try:
        from zoneinfo import ZoneInfo
        instant = datetime.now(ZoneInfo("Europe/Paris"))
        return instant.strftime("%Y-%m-%d"), instant.strftime("%H:%M")
    except Exception:
        instant = datetime.now(timezone.utc)
        return instant.strftime("%Y-%m-%d"), instant.strftime("%H:%M") + " UTC"


def demander(question: str, permis: set[str] | None = None, vide: bool = False) -> str:
    """Une réponse d'une ligne, redemandée tant qu'elle n'est pas valable."""
    while True:
        print(question, end=" ", flush=True)
        ligne = sys.stdin.readline()
        if not ligne:
            sys.exit("Saisie interrompue : rien n'a été noté.")
        reponse = ligne.strip()
        if permis is not None and reponse.lower() not in permis:
            print("  Répondez " + " ou ".join(sorted(permis)) + ".")
        elif not reponse and not vide:
            print("  Une réponse est attendue.")
        else:
            return reponse.lower() if permis is not None else reponse


def noter(graine: int, requete: int, chemin: Path) -> None:
    """Ajoute au relevé la ligne de la requête n."""
    if not chemin.parent.is_dir():
        sys.exit(f"Dossier {chemin.parent} introuvable : lancez la commande "
                 "à la racine du dépôt.")
    lignes = []
    if chemin.exists() and chemin.stat().st_size > 0:
        with chemin.open(newline="", encoding="utf-8") as fichier:
            lecteur = csv.DictReader(fichier)
            if lecteur.fieldnames != COLONNES:
                sys.exit(f"{chemin} n'a pas les colonnes attendues :\n"
                         + ",".join(COLONNES))
            lignes = list(lecteur)
    if any(ligne["numero"] == str(requete) for ligne in lignes):
        sys.exit(f"La requête {requete} est déjà dans le relevé : rien n'a été noté.")

    presente = " ; ".join(ordre(graine, requete, HOTELS))
    print(f"Requête {requete}, ordre présenté : {presente}")
    dernier = lignes[-1]["assistant"] if lignes else ""
    assistant = demander("Assistant (nom, et version du modèle s'il l'affiche)"
                         + (f" [Entrée : {dernier}] :" if dernier else " :"),
                         vide=bool(dernier)) or dernier
    print("Collez la réponse complète, puis tapez FIN seul sur une ligne :")
    texte = []
    while True:
        ligne = sys.stdin.readline()
        if not ligne:
            sys.exit("Saisie interrompue : rien n'a été noté.")
        if ligne.rstrip("\r\n") == "FIN":
            break
        texte.append(ligne.rstrip("\r\n"))
    reponse = "\n".join(texte).strip()
    if not reponse:
        sys.exit("Réponse vide : rien n'a été noté.")
    hotel = demander("Hôtel recommandé, selon la définition du plan d'audit :")
    web = demander("La réponse s'appuie-t-elle sur une recherche web ? (oui/non) :",
                   permis={"oui", "non"})
    remarques = demander("Remarques (Entrée si aucune) :", vide=True)
    date, heure = maintenant()

    nouveau = not chemin.exists() or chemin.stat().st_size == 0
    with chemin.open("a", newline="", encoding="utf-8") as fichier:
        ecrivain = csv.writer(fichier)
        if nouveau:
            ecrivain.writerow(COLONNES)
        ecrivain.writerow([requete, date, heure, assistant, presente,
                           reponse, hotel, web, remarques])
    print(f"Requête {requete} notée dans {chemin}.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ordre des cinq hôtels pour une requête de l'audit."
    )
    parser.add_argument("--graine", type=int, required=True,
                        help="la graine écrite dans le plan d'audit")
    groupe = parser.add_mutually_exclusive_group(required=True)
    groupe.add_argument("--requete", type=int,
                        help="afficher l'ordre de la requête n, à partir de 1")
    groupe.add_argument("--toutes", type=int,
                        help="afficher les ordres des requêtes 1 à N")
    groupe.add_argument("--noter", type=int,
                        help="noter dans le relevé la réponse de la requête n")
    args = parser.parse_args()

    if len(HOTELS) != 5 or len(set(HOTELS)) != 5:
        parser.error("HOTELS doit contenir cinq noms, tous différents.")

    if args.requete is not None:
        if args.requete < 1:
            parser.error("le numéro de requête commence à 1.")
        print(f"Requête {args.requete}, graine {args.graine} :")
        for rang, hotel in enumerate(ordre(args.graine, args.requete, HOTELS), 1):
            print(f"  {rang}. {hotel}")
        print("Pour le relevé : " + " ; ".join(ordre(args.graine, args.requete, HOTELS)))
    elif args.toutes is not None:
        if args.toutes < 1:
            parser.error("--toutes attend un nombre de requêtes, à partir de 1.")
        for n in range(1, args.toutes + 1):
            print(f"{n} : " + " ; ".join(ordre(args.graine, n, HOTELS)))
    else:
        if args.noter < 1:
            parser.error("le numéro de requête commence à 1.")
        noter(args.graine, args.noter, RELEVE)


if __name__ == "__main__":
    main()
