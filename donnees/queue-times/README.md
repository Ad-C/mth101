# Temps d'attente des parcs Disneyland Paris

**[Powered by Queue-Times.com](https://queue-times.com/)**

Relevés réels des temps d'attente affichés dans les deux parcs Disneyland
Paris (Disneyland Park et Disney Adventure World), obtenus par l'API publique
de Queue-Times. Ce sont les données d'un parc réel, citées comme telles ;
les parcs ne sont associés ni au cours ni à son projet.

## Comment les relevés sont faits

- Toutes les 15 minutes, aux minutes 4, 19, 34 et 49, de 8 h à minuit
  (heure de Paris), jusqu'au 12 novembre 2026 : une requête par parc, pas
  davantage.
- Un service de planification externe, cron-job.org, lance chaque relevé
  sur GitHub : `scripts/releve_queue_times.py`, exécuté par
  `.github/workflows/queue-times.yml`, ajoute les relevés au fichier du jour
  et les commite.
- **Avant le 5 octobre**, les relevés dépendaient de la planification de
  GitHub, qui accusait des heures de retard : le fichier du 4 octobre n'en
  compte que deux, à 18 h 18 et à 21 h 42. La régularité commence le
  5 octobre.
- Un relevé peut encore manquer, ou partir avec quelques minutes de retard
  quand GitHub tarde à lui attribuer une machine. La colonne `releve_utc`
  donne toujours l'instant réel du relevé, jamais l'heure prévue.
- Si un seul des deux parcs répond, le relevé ne contient que les
  attractions de ce parc.
- Queue-Times rafraîchit ses données environ toutes les 5 minutes ; la
  colonne `maj_queue_times_utc` dit de quand date chaque valeur.

## Trous et retards connus

La série n'est pas parfaitement régulière, comme la plupart des données
réelles. Les écarts connus au 6 octobre 2026 :

| Jour | Relevés | Ce qui s'est passé |
|---|---|---|
| 4 octobre | 2 | Avant le déclencheur externe : relevés à 18 h 18 et à 21 h 42 seulement. |
| 5 octobre | 62 sur 64 | Incident de GitHub Actions, déclaré par GitHub à 21 h 11 (heure de Paris) : retards dans l'attribution des machines. Les relevés prévus à 22 h 04 et à 22 h 34 manquent : aucune machine ne les a pris en charge. Ceux de 21 h 34, 21 h 49, 22 h 19, 23 h 04 et 23 h 19 sont partis avec 5 à 10 minutes de retard, à 21 h 44, 21 h 59, 22 h 24, 23 h 14 et 23 h 24. |

Les fichiers font foi : un écart de plus de 15 minutes entre deux valeurs
successives de `releve_utc`, dans un même fichier, signale un trou.

## Les fichiers

Un fichier par jour, `AAAA-MM-JJ.csv` (date de Paris), une ligne par
attraction et par relevé.

| Colonne | Contenu |
|---|---|
| `releve_utc` | Instant du relevé, en temps universel (UTC) |
| `date_paris`, `heure_paris` | Le même instant, en heure de Paris |
| `parc_id`, `parc` | Identifiant Queue-Times et nom du parc |
| `zone` | Zone du parc (*land*) |
| `attraction_id`, `attraction` | Identifiant Queue-Times et nom de l'attraction |
| `ouverte` | 1 si l'attraction est ouverte, 0 sinon |
| `attente_min` | Temps d'attente affiché, en minutes (0 quand l'attraction est fermée) |
| `maj_queue_times_utc` | Dernière mise à jour de la valeur chez Queue-Times (UTC) |

Une même attraction peut apparaître deux fois sous deux noms : la file
normale et la file « Single Rider ».

## Lire les données en Python

```python
import pandas as pd

url = "https://raw.githubusercontent.com/Ad-C/mth101/main/donnees/queue-times/2026-10-06.csv"
releves = pd.read_csv(url)
ouvertes = releves[releves["ouverte"] == 1]
print(ouvertes.groupby("attraction")["attente_min"].mean().sort_values())
```

## Conditions d'utilisation

L'API de Queue-Times est gratuite, à condition d'afficher bien en vue la
mention « Powered by Queue-Times.com » avec un lien vers
<https://queue-times.com/>. **Tout rendu qui utilise ou affiche ces données
(notebook, graphique, simulateur, poster, diapositive) porte cette mention.**

Ces relevés restent soumis aux conditions de Queue-Times : la licence des
supports de cours (CC BY-NC-ND 4.0) ne les couvre pas.
