# Temps d'attente des parcs Disneyland Paris

**[Powered by Queue-Times.com](https://queue-times.com/)**

Relevés réels des temps d'attente affichés dans les deux parcs Disneyland
Paris (Disneyland Park et Disney Adventure World), obtenus par l'API publique
de Queue-Times. Ce sont les données d'un parc réel, citées comme telles ;
les parcs ne sont associés ni au cours ni à son projet.

## Comment les relevés sont faits

- Toutes les 15 minutes, de 8 h 30 à 23 h 45 (heure de Paris), du
  4 octobre au 12 novembre 2026 : une requête par parc, pas davantage.
- Un programme planifié sur GitHub (`scripts/releve_queue_times.py`, lancé
  par `.github/workflows/queue-times.yml`) ajoute les relevés au fichier du
  jour et les commite.
- Les passages peuvent être retardés, parfois de beaucoup, ou sautés :
  l'écart entre deux relevés n'est pas toujours de 15 minutes. C'est une
  propriété des données à prendre en compte ; la colonne `releve_utc` donne
  l'instant réel de chaque relevé.
- Queue-Times rafraîchit ses données environ toutes les 5 minutes ; la
  colonne `maj_queue_times_utc` dit de quand date chaque valeur.

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
