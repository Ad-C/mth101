"""Relevé des temps d'attente des deux parcs Disneyland Paris via l'API Queue-Times.

Lancé toutes les 15 minutes par .github/workflows/queue-times.yml. Chaque
passage ajoute une ligne par attraction au fichier du jour,
donnees/queue-times/AAAA-MM-JJ.csv (date de Paris).

Sobriété : une requête par parc et par passage, aucune hors de la plage
horaire ni après la date de fin.

Données : Powered by Queue-Times.com (https://queue-times.com/).
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
import urllib.request
from datetime import date, datetime, time as heure, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

PARCS = {4: "Disneyland Park", 28: "Disney Adventure World"}
URL = "https://queue-times.com/parks/{}/queue_times.json"
PARIS = ZoneInfo("Europe/Paris")
DEBUT, FIN = heure(8, 30), heure(23, 45)          # plage relevée, heure de Paris
DOSSIER = Path(__file__).resolve().parents[1] / "donnees" / "queue-times"
COLONNES = ["releve_utc", "date_paris", "heure_paris", "parc_id", "parc", "zone",
            "attraction_id", "attraction", "ouverte", "attente_min", "maj_queue_times_utc"]
AGENT = "mth101-releve (cours de probabilites ; github.com/Ad-C/mth101)"


def lire(parc_id: int) -> dict:
    requete = urllib.request.Request(URL.format(parc_id), headers={"User-Agent": AGENT})
    for essai in (1, 2):
        try:
            with urllib.request.urlopen(requete, timeout=30) as reponse:
                return json.load(reponse)
        except Exception as erreur:                  # réseau, HTTP, JSON : un second essai
            if essai == 2:
                raise
            print(f"parc {parc_id} : {erreur} ; nouvel essai dans 20 s", file=sys.stderr)
            time.sleep(20)
    raise AssertionError


def attractions(donnees: dict):
    for zone in donnees.get("lands", []):
        for a in zone.get("rides", []):
            yield zone.get("name", ""), a
    for a in donnees.get("rides", []):               # attractions hors zone, s'il y en a
        yield "", a


def main() -> int:
    maintenant = datetime.now(timezone.utc).replace(microsecond=0)
    local = maintenant.astimezone(PARIS)
    fin_collecte = date.fromisoformat(os.environ.get("FIN_COLLECTE", "2026-11-12"))
    if local.date() > fin_collecte:
        print(f"collecte close depuis le {fin_collecte} : aucune requête")
        return 0
    if not DEBUT <= local.time() <= FIN:
        print(f"{local:%H:%M} à Paris, hors plage {DEBUT:%H:%M}-{FIN:%H:%M} : aucune requête")
        return 0

    lignes, echecs = [], 0
    for parc_id, parc in PARCS.items():
        try:
            donnees = lire(parc_id)
        except Exception as erreur:
            print(f"parc {parc_id} ({parc}) : échec, {erreur}", file=sys.stderr)
            echecs += 1
            continue
        for zone, a in attractions(donnees):
            lignes.append({
                "releve_utc": maintenant.isoformat().replace("+00:00", "Z"),
                "date_paris": f"{local:%Y-%m-%d}",
                "heure_paris": f"{local:%H:%M}",
                "parc_id": parc_id,
                "parc": parc,
                "zone": zone,
                "attraction_id": a.get("id"),
                "attraction": a.get("name", "").strip(),
                "ouverte": 1 if a.get("is_open") else 0,
                "attente_min": a.get("wait_time"),
                "maj_queue_times_utc": a.get("last_updated", "").replace(".000Z", "Z"),
            })

    if lignes:
        DOSSIER.mkdir(parents=True, exist_ok=True)
        fichier = DOSSIER / f"{local:%Y-%m-%d}.csv"
        nouveau = not fichier.exists()
        with fichier.open("a", newline="", encoding="utf-8") as f:
            ecrivain = csv.DictWriter(f, fieldnames=COLONNES)
            if nouveau:
                ecrivain.writeheader()
            ecrivain.writerows(lignes)
        print(f"{len(lignes)} lignes ajoutées à {fichier.name}")
    return 1 if echecs == len(PARCS) else 0


if __name__ == "__main__":
    sys.exit(main())
