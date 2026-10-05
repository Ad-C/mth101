# MTH101 · Probabilités, distributions et aide à la décision

Dépôt public du cours MTH101 du Bachelor IA, 1re année, de l'École 89, année
2026-2027. Intervenant : Adrien Chiodo.

**La page du cours : <https://ad-c.github.io/mth101/>**

## Le module

Décider dans l'incertain : calculer des probabilités, reconnaître les lois
usuelles, estimer, tester, puis transformer un résultat chiffré en
recommandation. Vous travaillez en binôme comme consultants juniors d'une
agence de conseil en données, spécialisée dans le tourisme et l'hôtellerie,
qui reçoit des commandes de clients du secteur.

Six objectifs :

1. Calculer des probabilités conditionnelles et appliquer le théorème de Bayes.
2. Identifier et mobiliser les lois de Bernoulli, binomiale, Poisson et normale.
3. Calculer et interpréter espérance, variance et écart-type.
4. Estimer un paramètre et construire un intervalle de confiance à 95 %.
5. Mettre en œuvre et interpréter un test d'hypothèse simple pour comparer deux proportions.
6. Formuler une recommandation business argumentée à partir de résultats probabilistes et statistiques.

## Calendrier

| Date | Séance | Au programme |
|---|---|---|
| Mer. 7/10, matin | 1 | Lancement de l'agence ; probabilités, probabilités conditionnelles, indépendance |
| Ven. 9/10, matin | 2 | Théorème de Bayes ; vote du nom de l'agence |
| Ven. 9/10, après-midi | 3 | Lois de Bernoulli, binomiale et de Poisson ; espérance, variance ; présentation des missions |
| Jeu. 15/10, après-midi | 4, en autonomie | Projet : premier jalon |
| Ven. 23/10, matin | 5 | Loi normale, intuition du théorème central limite |
| Ven. 23/10, après-midi | 6 | Estimation, intervalle de confiance, test de deux proportions |
| Ven. 6/11, après-midi | 7, en autonomie | Projet : second jalon |
| Jeu. 12/11, journée | 8 et 9 | Journée des soutenances |
| Jeu. 28/01, après-midi | 10 | Examen |

Chaque séance en présence consacre une partie de son temps au projet.

## Ce que contient ce dépôt

- `docs/` : la page du cours, publiée sur GitHub Pages : supports en PDF et
  résumé de chaque séance passée.
- `donnees/queue-times/` : des relevés de temps d'attente, constitués pour le
  projet (voir le `README` du dossier).
  [Powered by Queue-Times.com](https://queue-times.com/).
- `scripts/` et `.github/workflows/` : le programme qui fait ces relevés.

Ce dépôt se consulte ; vous n'y écrivez pas. Votre travail vit dans le dépôt
privé de votre binôme, créé depuis le modèle
<https://github.com/Ad-C/mth101-modele> en suivant le guide GitHub distribué
en séance.

## Données utilisées dans le cours

- **Hotel booking demand** : N. Antonio, A. de Almeida, L. Nunes, « Hotel
  booking demand datasets », *Data in Brief*, 22 (2019), 41–49,
  [doi:10.1016/j.dib.2018.11.126](https://doi.org/10.1016/j.dib.2018.11.126).
  Licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr).
- **Temps d'attente** : [Powered by Queue-Times.com](https://queue-times.com/).

## Licences

Une licence par composant :

- **Supports de cours** (pages de `docs/` et PDF de `docs/supports/`) :
  © 2026 Adrien Chiodo,
  [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.fr).
  Vous pouvez les partager en citant l'auteur, sans usage commercial ni
  version modifiée.
- **Relevés de temps d'attente** (`donnees/queue-times/`) : données de
  Queue-Times, soumises à ses conditions ; la mention
  « [Powered by Queue-Times.com](https://queue-times.com/) », avec un lien,
  est obligatoire dans tout rendu qui les utilise.
- **Tableaux tirés de Hotel booking demand** (dans les supports) : chiffres
  calculés à partir du jeu de N. Antonio, A. de Almeida et L. Nunes (2019),
  sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) ;
  toute réutilisation cite cette source.
- **Programme de relevé** (`scripts/` et `.github/`) : versé dans le domaine
  public, [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr).
