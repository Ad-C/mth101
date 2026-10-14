---
type: base-connaissances
origine:
- https://ad-c.github.io/mth101/
- https://ad-c.github.io/mth101/seances/seance-01.html
- https://ad-c.github.io/mth101/seances/seance-02-03.html
- https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices.pdf
- https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices-1-a-7-corriges.pdf
- https://ad-c.github.io/mth101/projet.html
- https://ad-c.github.io/mth101/supports/projet/mth101-synthese-missions.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-feuille-de-route-jalon-1.pdf
- https://ad-c.github.io/mth101/supports/seance-04/mth101-seance-04-parcours-lois-discretes.pdf
- https://ad-c.github.io/mth101/supports/polycopie/mth101-carte-du-module.pdf
- https://ad-c.github.io/mth101/kit-tuteur.html
- https://ad-c.github.io/mth101/faq.html
- https://github.com/Ad-C/mth101/tree/main/notebooks
- https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-commande.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-note-de-cadrage.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-kit-partie-1.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-commande.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-note-de-cadrage.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-kit-partie-1.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-commande.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-note-de-cadrage.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-kit-partie-1.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-commande.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-note-de-cadrage.pdf
- https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-kit-partie-1.pdf
depot-public: Ad-C/mth101, df21d35
genere: '2026-10-14'
---

# Base de connaissances du tuteur de MTH101

Ce fichier rassemble les documents publiés pour les étudiants du cours MTH101
(Bachelor IA, 1re année, École 89, 2026-2027), tels qu’ils sont en ligne à la
date de génération. Il ne contient rien d’autre. Il a deux sortes de
parties : la partie commune (le cours, son calendrier, ce qui a été vu, les
exercices du 9 octobre et les corrigés des exercices 1 à 7, le projet, le
jalon 1 du 15 octobre, les aides), puis une partie par mission,
avec la commande du client, la note de cadrage et le kit, partie 1. Chaque
document donne son adresse publique, à citer quand on y renvoie.

Ce qui n’y figure pas n’est pas connu : il se demande à l’intervenant.

<!-- partie: commune -->

# Partie commune

## Accueil

Page : https://ad-c.github.io/mth101/

Cours MTH101 du Bachelor IA, 1re année, de l’École 89, année 2026-2027. Intervenant : Adrien Chiodo.

### Le module

Décider dans l’incertain : calculer des probabilités, reconnaître les lois usuelles, estimer, tester, puis transformer un résultat chiffré en recommandation. Vous travaillez en binôme comme consultants juniors d’une agence de conseil en données, spécialisée dans le tourisme et l’hôtellerie.

### Calendrier

| Date | Séance | Au programme |
|----|----|----|
| Mer. 7/10, matin | 1 | Lancement de l’agence ; probabilités, probabilités conditionnelles, indépendance |
| Ven. 9/10, matin | 2 | Théorème de Bayes ; vote du nom de l’agence |
| Ven. 9/10, après-midi | 3 | Lois de Bernoulli, binomiale et de Poisson ; espérance, variance ; présentation des missions |
| Jeu. 15/10, après-midi | 4, en autonomie | Projet : premier jalon |
| Ven. 23/10, matin | 5 | Loi normale, intuition du théorème central limite |
| Ven. 23/10, après-midi | 6 | Estimation, intervalle de confiance, test de deux proportions |
| Ven. 6/11, après-midi | 7, en autonomie | Projet : second jalon |
| Jeu. 12/11, journée | 8 et 9 | Journée des soutenances |
| Jeu. 28/01, après-midi | 10 | Examen |

### Les séances

Le résumé de chaque séance passée, avec ses supports en PDF, est sur la page [Séances](https://ad-c.github.io/mth101/seances.html).

### Le projet

Les quatre missions de l’agence, leurs documents et le jalon 1 du 15 octobre : page [Projet](https://ad-c.github.io/mth101/projet.html). Pour vous servir d’un assistant IA comme d’un tuteur : le [kit tuteur](https://ad-c.github.io/mth101/kit-tuteur.html).

### Votre dépôt de binôme

Il se crée depuis le modèle [github.com/Ad-C/mth101-modele](https://github.com/Ad-C/mth101-modele), en suivant le guide GitHub distribué en séance.

Une question sur GitHub ou Codespaces : la [FAQ GitHub](https://ad-c.github.io/mth101/faq.html).

### Données

- Relevés de temps d’attente des deux parcs Disneyland Paris : [dossier `donnees/queue-times`](https://github.com/Ad-C/mth101/tree/main/donnees/queue-times). [Powered by Queue-Times.com](https://queue-times.com/).
- Hotel booking demand : N. Antonio, A. de Almeida, L. Nunes, *Data in Brief*, 22 (2019), 41–49, [doi:10.1016/j.dib.2018.11.126](https://doi.org/10.1016/j.dib.2018.11.126), licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr).

### Licences

Supports de cours : © 2026 Adrien Chiodo, [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.fr). Relevés de temps d’attente : conditions de Queue-Times, mention « Powered by Queue-Times.com » obligatoire. Tableaux tirés de Hotel booking demand : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr), avec attribution.

## Séance 1 · mercredi 7 octobre

Page : https://ad-c.github.io/mth101/seances/seance-01.html

**Séance 1, mercredi 7 octobre, matin.** Le lancement de l’agence et du module ; les premières probabilités.

### Ce que nous avons vu

- Le lancement de l’agence : vous y êtes consultants juniors, au service de clients du tourisme et de l’hôtellerie.
- L’introduction aux probabilités et leur vocabulaire, commencés.
- GitHub : vos comptes, le dépôt de votre équipe, votre premier commit.

Les exercices n’ont pas été faits en séance : ils ont été repris le 9 octobre.

### Supports

- [Exercices (PDF)](https://ad-c.github.io/mth101/supports/seance-01/mth101-seance-01-exercices.pdf)
- [Commande 1 (PDF)](https://ad-c.github.io/mth101/supports/seance-01/mth101-seance-01-commande-01.pdf)
- [Guide GitHub (PDF)](https://ad-c.github.io/mth101/supports/seance-01/mth101-seance-01-guide-github.pdf) : les premiers pas, et que faire si ça bloque

## Séances 2 et 3 · vendredi 9 octobre

Page : https://ad-c.github.io/mth101/seances/seance-02-03.html

**Séances 2 et 3, vendredi 9 octobre, journée.** Le théorème de Bayes, commencé le matin ; les missions de l’agence l’après-midi.

### Ce que nous avons vu

- Le matin : le théorème de Bayes, commencé ; la suite est dans les diapositives et les exercices 1 à 7.
- L’après-midi : la présentation des quatre missions, puis leur tirage au sort (page [Projet](https://ad-c.github.io/mth101/projet.html)).

Les lois discrètes, prévues l’après-midi, n’ont pas pu être traitées : elles sont reportées au [parcours en autonomie](https://ad-c.github.io/mth101/supports/seance-04/mth101-seance-04-parcours-lois-discretes.pdf) du jeudi 15 octobre.

### Supports

- [Diapositives du matin (PDF)](https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seance-02-diapos.pdf)
- [Diapositives de l’après-midi (PDF)](https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seance-03-diapos.pdf)
- [Exercices (PDF)](https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices.pdf) : 1 à 7 sur le théorème de Bayes, 8 à 15 avec le parcours du 15 octobre
- [Corrigés des exercices 1 à 7 (PDF)](https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices-1-a-7-corriges.pdf)
- [Notebook de la séance 3](https://github.com/Ad-C/mth101/tree/main/notebooks), à copier dans votre dépôt

### Pour la prochaine fois

- Jeudi 15 octobre, en autonomie : le [parcours sur les lois discrètes](https://ad-c.github.io/mth101/supports/seance-04/mth101-seance-04-parcours-lois-discretes.pdf), 60 minutes, puis le jalon 1 de votre mission, avant 23 h 59. La [feuille de route](https://ad-c.github.io/mth101/supports/projet/mth101-feuille-de-route-jalon-1.pdf) en donne le déroulé.
- D’ici le vendredi 23 octobre, en autonomie : la fin du théorème de Bayes, avec les diapositives du matin, les exercices 1 à 7 et leurs [corrigés](https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices-1-a-7-corriges.pdf), puis le chapitre 2 du polycopié dès sa parution. Un rappel de 20 minutes ouvrira la séance du 23 octobre.

## Le théorème de Bayes : la fin, en autonomie

Le théorème de Bayes a été commencé le vendredi 9 octobre au matin. La fin se travaille en autonomie, d’ici le vendredi 23 octobre, avec :

- les diapositives du 9 octobre au matin : https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seance-02-diapos.pdf ;
- les exercices 1 à 7 du fascicule du 9 octobre : https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices.pdf ;
- leurs corrigés : https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices-1-a-7-corriges.pdf.

Le chapitre 2 du polycopié, « Le théorème de Bayes », n’est pas encore paru : il complétera ces documents dès sa parution.

Un rappel de 20 minutes ouvrira la séance du vendredi 23 octobre.

## Séances 2 et 3 · Exercices

*Théorème de Bayes · Lois discrètes, espérance, variance. Daté du vendredi 9 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices.pdf

Quinze exercices pour la journée. Les exercices 1 à 7 suivent le théorème de Bayes, le matin ; les exercices 8 à 15, les lois discrètes, l’après-midi. Le formulaire et le parcours de consolidation sont en fin de fascicule : si l’on vous l’indique, commencez par le parcours. Ce qui n’est pas fini en séance se termine dans `exercices/seance-02.md` et `exercices/seance-03.md`, dans le dépôt du binôme.

Donnez les probabilités sous forme de fraction quand c’est simple, puis de nombre décimal arrondi au millième. Sauf mention d’une source, les chiffres sont fictifs.

**Les données réelles de ce fascicule** viennent du jeu Hotel booking demand : N. Antonio, A. de Almeida, L. Nunes, « Hotel booking demand datasets », *Data in Brief*, 22 (2019), 41–49, doi:10.1016/j.dib.2018.11.126, licence CC BY 4.0. Deux hôtels portugais, 119 390 réservations, arrivées de juillet 2015 à août 2017. Une réservation y est dite « annulée » quand le client a annulé, ou qu’il ne s’est pas présenté sans prévenir.

### Exercice 1 · Affaires et petit-déjeuner

Dans un hôtel, 30 % des clients voyagent pour affaires. 80 % des clients d’affaires prennent le petit-déjeuner, contre 50 % des autres clients.

1.  Dessinez l’arbre de probabilités.
2.  Calculez la probabilité qu’un client pris au hasard prenne le petit-déjeuner.
3.  Un client prend son petit-déjeuner. Quelle est la probabilité qu’il voyage pour affaires ?
4.  Un client ne prend pas de petit-déjeuner. Même question.

### Exercice 2 · Le pass annuel

Parmi les visiteurs d’un parc de loisirs, 25 % ont un pass annuel. 60 % des détenteurs d’un pass viennent en semaine, contre 20 % des autres visiteurs.

1.  Imaginez 2 000 visiteurs. Dessinez l’arbre des fréquences naturelles : des nombres de visiteurs à chaque nœud.
2.  Combien de visiteurs viennent en semaine ? Combien d’entre eux ont un pass ?
3.  Calculez P(pass \| semaine) et P(pass \| week-end).
4.  Le parc veut proposer une offre de pass annuel à des visiteurs qui n’en ont pas encore. Vaut-il mieux la présenter en semaine ou le week-end ? Donnez deux arguments chiffrés.

### Exercice 3 · La commande 1, par la formule

Source : Hotel booking demand, hôtel urbain. On ne garde de la commande 1 que trois nombres :

- P(agence en ligne) = 0,488 : la part des réservations passées par une agence de voyage en ligne ;
- P(annulée \| agence en ligne) = 0,374 ;
- P(annulée) = 0,417.

1.  Avec la formule de Bayes, calculez P(agence en ligne \| annulée).
2.  Comparez avec votre réponse à la question 3 de la commande 1.
3.  Les agences en ligne annulent moins que la moyenne, et pèsent pourtant 44 % des annulations. Expliquez-le à l’aide de la formule.

### Exercice 4 · Les punaises de lit

Un hôtel fait inspecter ses chambres par un détecteur. Une chambre sur 200 est infestée. Le détecteur signale 95 % des chambres infestées, mais aussi 3 % des chambres saines.

1.  Imaginez 20 000 inspections. Combien de chambres infestées, et combien sont signalées ? Combien de chambres saines sont signalées ?
2.  Une chambre est signalée. Quelle est la probabilité qu’elle soit infestée ?
3.  La direction veut fermer chaque chambre signalée pour la traiter. Sur 100 chambres fermées, combien le seraient à tort, environ ?
4.  *Pour aller plus loin.* Une chambre signalée est inspectée une seconde fois, et de nouveau signalée. On suppose les deux inspections indépendantes. Quelle est maintenant la probabilité qu’elle soit infestée ? Partez de la réponse à la question 2 comme nouveau taux de base.

### Exercice 5 · Les avis cinq étoiles

Sur une plateforme, 10 % des avis sont faux. 90 % des faux avis donnent cinq étoiles, contre 40 % des avis authentiques.

1.  Quelle part des avis donnent cinq étoiles ?
2.  Un avis donne cinq étoiles. Quelle est la probabilité qu’il soit faux ?
3.  Un avis donne moins de cinq étoiles. Même question.
4.  La plateforme envisage de masquer tous les avis cinq étoiles. Qu’en pensez-vous ?

### Exercice 6 · Un modèle, deux hôtels

Un modèle de prédiction des annulations signale 75 % des réservations qui seront annulées ; il signale aussi 10 % de celles qui seront honorées. On l’installe dans deux hôtels. Dans l’hôtel A, 40 % des réservations sont annulées ; dans l’hôtel B, 10 %.

1.  Imaginez 1 000 réservations de l’hôtel A. Combien d’alertes justes, combien de fausses alertes ? Calculez P(annulée \| signalée).
2.  Même question pour l’hôtel B.
3.  Le fournisseur annonce : « 75 % des annulations détectées, seulement 10 % de fausses alertes. » Pourquoi ces deux chiffres ne suffisent-ils pas à dire si une alerte est fiable ?

### Exercice 7 · Vrai ou faux

Justifiez chaque réponse en une phrase.

1.  « 90 % des fraudes au paiement d’un hôtel viennent de cartes étrangères : 90 % des paiements par carte étrangère sont donc frauduleux. »
2.  « Si P(A \| B) = P(B \| A), avec des probabilités non nulles, alors P(A) = P(B). »
3.  « Un contrôle qui ne se trompe que dans 1 % des cas donne une alerte juste 99 fois sur 100. »
4.  « Si un test signale aussi souvent les cas positifs que les cas négatifs, P(B \| A) = P(B \| Ā), il n’apporte aucune information sur A. »

### Exercice 8 · La durée des séjours

Dans un hôtel, le nombre de nuits X d’un séjour suit la loi suivante.

| Nombre de nuits |    1 |    2 |    3 |    4 |   5 |
|-----------------|-----:|-----:|-----:|-----:|----:|
| Probabilité     | 0,35 | 0,25 | 0,20 | 0,15 |   ? |

1.  Complétez le tableau.
2.  Calculez E(X), et interprétez le résultat.
3.  Calculez V(X) par les deux formules du cours, puis σ(X).
4.  L’hôtel attend 120 séjours en novembre. Combien de nuitées peut-il prévoir ?

### Exercice 9 · Deux réservations

Deux réservations sont annulées chacune avec la probabilité 0,37, indépendamment l’une de l’autre. On note X le nombre d’annulations.

1.  Construisez l’arbre, puis donnez la loi de X.
2.  Calculez E(X) et V(X).
3.  Comparez avec 2 × 0,37 et 2 × 0,37 × 0,63. Quelle loi X suit-elle ?

### Exercice 10 · Vingt réservations

Un hôtel suit 20 réservations, annulées chacune avec la probabilité 0,37 : la fréquence observée dans Hotel booking demand.

1.  Pourquoi peut-on dire que le nombre X d’annulations suit la loi binomiale B(20 ; 0,37) ? Quelle hypothèse faut-il faire ?
2.  Calculez P(X = 7). Le nombre de façons de choisir 7 réservations parmi 20 vaut 77 520.
3.  Avec Python, calculez P(X ≤ 5) et P(X ≥ 10).
4.  Calculez E(X) et σ(X).
5.  Le directeur annonce : « 7 annulations sur 20, pas une de plus. » Qu’en pensez-vous ?

### Exercice 11 · Le petit-déjeuner

Un matin, 12 chambres sont occupées, un client par chambre. Chaque client descend prendre le petit-déjeuner avec la probabilité 0,6, indépendamment des autres. On note X le nombre de clients qui descendent.

1.  Quelle est la loi de X ?
2.  Calculez la probabilité que les 12 clients descendent, puis qu’aucun ne descende.
3.  Calculez E(X) et σ(X).
4.  Combien de couverts préparer pour que chacun soit servi au moins 95 matins sur 100 ? Aidez-vous du tableau.

| k        |     6 |     7 |     8 |     9 |    10 |    11 |
|----------|------:|------:|------:|------:|------:|------:|
| P(X ≤ k) | 0,335 | 0,562 | 0,775 | 0,917 | 0,980 | 0,998 |

### Exercice 12 · Binomiale ou pas ?

Pour chaque variable, dites si elle suit une loi binomiale. Si oui, donnez n et p ; sinon, dites quelle condition manque.

1.  Un hôtel envoie un questionnaire à 50 clients ; chacun répond avec la probabilité 0,2, indépendamment des autres. X : le nombre de réponses.
2.  Un client loue un vélo chaque jour d’un séjour de 7 jours avec la probabilité 0,3, indépendamment d’un jour à l’autre. X : le nombre de jours de location.
3.  Un parc tire au sort 3 gagnants parmi 20 visiteurs, dont 8 enfants. X : le nombre d’enfants parmi les gagnants.
4.  X : le nombre de jours de pluie en octobre, dans un parc de loisirs.
5.  X : le nombre de clients arrivés à la réception entre 17 h et 18 h.

### Exercice 13 · La réception

Entre 17 h et 18 h, le nombre X de clients qui arrivent à la réception suit une loi de Poisson de paramètre λ = 6.

1.  Calculez P(X = 0) et P(X = 6).
2.  Avec Python, calculez P(X ≥ 10).
3.  Donnez E(X) et σ(X).
4.  Sur un quart d’heure, le nombre d’arrivées suit une loi de Poisson de paramètre 1,5. Quelle est la probabilité de n’avoir aucune arrivée en 15 minutes ? d’en avoir au moins 3 ?

### Exercice 14 · Les pannes de la nuit

Un hôtel compte 400 chambres. Chaque nuit, chaque chambre signale une panne avec la probabilité 0,005, indépendamment des autres.

1.  Quelle est la loi exacte du nombre X de pannes d’une nuit ? Son espérance ?
2.  Calculez P(X = 0) avec cette loi, puis avec la loi de Poisson de même espérance.
3.  Le technicien de nuit peut traiter deux pannes au plus. Avec la loi de Poisson, quelle est la probabilité qu’une nuit lui en apporte davantage ?

### Exercice 15 · Le tirage au sort

Les quatre missions, deux par thème, sont tirées au sort entre les équipes : chaque équipe a la même chance d’obtenir chacune des places.

1.  Avec huit équipes et deux places par mission, quelle est la probabilité qu’une équipe obtienne la mission qu’elle préfère ? une mission du thème qu’elle préfère ?
2.  Avec neuf équipes, une mission, tirée au sort, a trois places, et les trois autres deux. Quelle est la probabilité qu’une équipe obtienne la mission qu’elle préfère ? Un arbre aide.
3.  Avec huit équipes, chacune note sa mission préférée. Combien d’équipes l’obtiendront, en moyenne ? Justifiez, sans supposer d’indépendance.
4.  Les huit équipes préfèrent toutes la même mission. Combien l’obtiendront ? Comparez avec la question 3.

### Le notebook de simulation

Le notebook `seance-03-simulation-binomiale-poisson.ipynb` se copie depuis github.com/Ad-C/mth101, dossier `notebooks`, dans le dossier `exercices` de votre dépôt. Ses questions « À vous » se traitent dans le notebook.

### Formulaire

**Le théorème de Bayes**, et son dénominateur développé :

`P(A | B) = P(B | A) × P(A) / P(B)`

`P(A | B) = P(B | A) × P(A) / [P(B | A) × P(A) + P(B | non A) × P(non A)]`

**Espérance, variance, écart-type** d’une variable X qui prend les valeurs x₁, …, x_(n) avec les probabilités p₁, …, p_(n) :

`E(X) = x₁ p₁ + x₂ p₂ + … + xₙ pₙ`

`V(X) = (x₁ − E(X))² p₁ + … + (xₙ − E(X))² pₙ`

V(X) = E(X²) − E(X)² ; σ(X) = √V(X), dans l’unité de X.

**Loi de Bernoulli** de paramètre p : E(X) = p ; V(X) = p(1 − p).

**Loi binomiale** B(n ; p) : le nombre de succès parmi n épreuves de Bernoulli identiques et indépendantes.

`P(X = k) = (k parmi n) × p^k × (1 − p)^(n − k)`

`(k parmi n) = n! / (k! × (n − k)!)`

E(X) = np ; V(X) = np(1 − p). En Python : `binom.pmf(k, n, p)`, `binom.cdf(k, n, p)`, `binom.sf(k, n, p)`.

**Loi de Poisson** de paramètre λ : le nombre d’événements indépendants dans un intervalle, à un rythme moyen λ.

`P(X = k) = e^(−λ) × λ^k / k!`

E(X) = V(X) = λ. En Python : `poisson.pmf(k, lam)`, `poisson.cdf(k, lam)`, `poisson.sf(k, lam)`.

### Parcours de consolidation

Cinq exercices courts, un par question du quiz de positionnement du 7 octobre : pourcentages, fractions, lecture d’un tableau. Toute la journée s’appuie sur ces calculs. Faites ceux que l’on vous indique, ou ceux qui vous ont posé problème.

#### C1 · Pourcentage d’une quantité

Un hôtel de 180 chambres est occupé à 80 %.

1.  Combien de chambres sont occupées ?
2.  25 % des chambres occupées sont des suites. Combien de suites sont occupées ?
3.  Quelle part de toutes les chambres de l’hôtel ces suites représentent-elles ?

#### C2 · Hausses et baisses

Le prix d’une nuit passe de 80 € à 92 €.

1.  De quel pourcentage a-t-il augmenté ?
2.  Il baisse ensuite de 15 %. Quel est le nouveau prix ?
3.  A-t-il retrouvé son niveau de départ ? Pourquoi ?

#### C3 · Fractions et pourcentages

1.  Écrivez 3/5, 7/20 et 1/8 sous forme de pourcentage.
2.  Les deux tiers des clients d’un hôtel viennent en couple, et les trois quarts de ces couples réservent en ligne. Quelle fraction de tous les clients sont des couples qui réservent en ligne ? En pourcentage ?

#### C4 · Un pourcentage d’un pourcentage

Dans un parc, 30 % des visiteurs sont étrangers, et 40 % d’entre eux viennent pour la première fois.

1.  Quelle part de tous les visiteurs sont des étrangers venus pour la première fois ?
2.  Un collègue répond « 40 % ». Où est son erreur ?
3.  Sur 5 000 visiteurs, combien de personnes cela représente-t-il ?

#### C5 · Lire un tableau croisé

Clients d’un hôtel un samedi :

|          | Petit-déjeuner | Sans | Total |
|----------|---------------:|-----:|------:|
| Familles |             45 |   15 |    60 |
| Couples  |             36 |   54 |    90 |
| Total    |             81 |   69 |   150 |

1.  Parmi les familles, quelle part prend le petit-déjeuner ?
2.  Parmi les clients qui prennent le petit-déjeuner, quelle part sont des familles ?
3.  Les deux réponses utilisent la même case. Pourquoi diffèrent-elles ?

## Exercices 1 à 7 du 9/10 : corrigés

*Théorème de Bayes. Daté du mercredi 14 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices-1-a-7-corriges.pdf

**Les données réelles de ce fascicule** viennent du jeu Hotel booking demand : N. Antonio, A. de Almeida, L. Nunes, « Hotel booking demand datasets », *Data in Brief*, 22 (2019), 41–49, doi:10.1016/j.dib.2018.11.126, licence CC BY 4.0. Deux hôtels portugais, 119 390 réservations, arrivées de juillet 2015 à août 2017. Une réservation y est dite « annulée » quand le client a annulé, ou qu’il ne s’est pas présenté sans prévenir.

### Exercice 1 · Affaires et petit-déjeuner

Dans un hôtel, 30 % des clients voyagent pour affaires. 80 % des clients d’affaires prennent le petit-déjeuner, contre 50 % des autres clients.

1.  Dessinez l’arbre de probabilités.
2.  Calculez la probabilité qu’un client pris au hasard prenne le petit-déjeuner.
3.  Un client prend son petit-déjeuner. Quelle est la probabilité qu’il voyage pour affaires ?
4.  Un client ne prend pas de petit-déjeuner. Même question.

#### Corrigé

1.  Premier niveau : affaires 0,3 ; autre motif 0,7. Second niveau : sous « affaires », petit-déjeuner 0,8 et sans 0,2 ; sous « autre motif », 0,5 et 0,5.
2.  P(PD) = 0,3 × 0,8 + 0,7 × 0,5 = 0,24 + 0,35 = 0,59.
3.  P(affaires \| PD) = 0,24 / 0,59 ≈ 0,407.
4.  P(affaires \| sans PD) = (0,3 × 0,2) / 0,41 = 0,06 / 0,41 ≈ 0,146. Savoir qu’un client prend le petit-déjeuner fait passer la part des clients d’affaires de 30 % à 41 % ; savoir qu’il n’en prend pas la fait tomber à 15 %.

### Exercice 2 · Le pass annuel

Parmi les visiteurs d’un parc de loisirs, 25 % ont un pass annuel. 60 % des détenteurs d’un pass viennent en semaine, contre 20 % des autres visiteurs.

1.  Imaginez 2 000 visiteurs. Dessinez l’arbre des fréquences naturelles : des nombres de visiteurs à chaque nœud.
2.  Combien de visiteurs viennent en semaine ? Combien d’entre eux ont un pass ?
3.  Calculez P(pass \| semaine) et P(pass \| week-end).
4.  Le parc veut proposer une offre de pass annuel à des visiteurs qui n’en ont pas encore. Vaut-il mieux la présenter en semaine ou le week-end ? Donnez deux arguments chiffrés.

#### Corrigé

1.  500 visiteurs avec un pass : 300 en semaine, 200 le week-end. 1 500 sans pass : 300 en semaine, 1 200 le week-end.
2.  600 en semaine, dont 300 avec un pass.
3.  P(pass \| semaine) = 300 / 600 = 0,5 ; P(pass \| week-end) = 200 / 1 400 ≈ 0,143.
4.  Le week-end : 86 % des visiteurs n’y ont pas de pass (1 200 sur 1 400), contre 50 % en semaine ; et ces visiteurs sans pass y sont quatre fois plus nombreux (1 200 contre 300). Un taux et un volume, comme dans la commande 1.

### Exercice 3 · La commande 1, par la formule

Source : Hotel booking demand, hôtel urbain. On ne garde de la commande 1 que trois nombres :

- P(agence en ligne) = 0,488 : la part des réservations passées par une agence de voyage en ligne ;
- P(annulée \| agence en ligne) = 0,374 ;
- P(annulée) = 0,417.

1.  Avec la formule de Bayes, calculez P(agence en ligne \| annulée).
2.  Comparez avec votre réponse à la question 3 de la commande 1.
3.  Les agences en ligne annulent moins que la moyenne, et pèsent pourtant 44 % des annulations. Expliquez-le à l’aide de la formule.

#### Corrigé

1.  P(agence \| annulée) = 0,374 × 0,488 / 0,417 ≈ 0,438 (0,4377 avec ces arrondis).
2.  C’est le résultat de la commande, 14 491 / 33 102 ≈ 0,438 : la formule retrouve ce que donnait le tableau.
3.  P(agence \| annulée) = P(agence) × P(annulée \| agence) / P(annulée) = 0,488 × (0,374 / 0,417) ≈ 0,488 × 0,897. Le rapport est inférieur à 1 : elles annulent moins que la moyenne, ce qui réduit un peu leur part. Mais elles font près de la moitié des réservations : leur poids reste fort. La part d’un segment, son taux de base, compte autant que son taux d’annulation.

### Exercice 4 · Les punaises de lit

Un hôtel fait inspecter ses chambres par un détecteur. Une chambre sur 200 est infestée. Le détecteur signale 95 % des chambres infestées, mais aussi 3 % des chambres saines.

1.  Imaginez 20 000 inspections. Combien de chambres infestées, et combien sont signalées ? Combien de chambres saines sont signalées ?
2.  Une chambre est signalée. Quelle est la probabilité qu’elle soit infestée ?
3.  La direction veut fermer chaque chambre signalée pour la traiter. Sur 100 chambres fermées, combien le seraient à tort, environ ?
4.  *Pour aller plus loin.* Une chambre signalée est inspectée une seconde fois, et de nouveau signalée. On suppose les deux inspections indépendantes. Quelle est maintenant la probabilité qu’elle soit infestée ? Partez de la réponse à la question 2 comme nouveau taux de base.

#### Corrigé

1.  100 chambres infestées, dont 95 signalées ; 19 900 saines, dont 597 signalées ; 692 signalées en tout.
2.  P(infestée \| signalée) = 95 / 692 ≈ 0,137.
3.  Environ 86 sur 100 : 597 / 692 ≈ 0,863.
4.  0,95 × 0,137 / (0,95 × 0,137 + 0,03 × 0,863) ≈ 0,834. Une seconde inspection indépendante change un signal faible en quasi-certitude. L’indépendance se discute : un détecteur qui se trompe sur une chambre (une odeur, un produit) risque de se tromper encore.

### Exercice 5 · Les avis cinq étoiles

Sur une plateforme, 10 % des avis sont faux. 90 % des faux avis donnent cinq étoiles, contre 40 % des avis authentiques.

1.  Quelle part des avis donnent cinq étoiles ?
2.  Un avis donne cinq étoiles. Quelle est la probabilité qu’il soit faux ?
3.  Un avis donne moins de cinq étoiles. Même question.
4.  La plateforme envisage de masquer tous les avis cinq étoiles. Qu’en pensez-vous ?

#### Corrigé

1.  P(5 étoiles) = 0,1 × 0,9 + 0,9 × 0,4 = 0,09 + 0,36 = 0,45.
2.  P(faux \| 5 étoiles) = 0,09 / 0,45 = 0,2.
3.  P(faux \| moins de 5) = (0,1 × 0,1) / 0,55 ≈ 0,018.
4.  Elle masquerait 45 % des avis, dont 80 % sont authentiques (0,36 sur 0,45), pour écarter 90 % des faux. Cinq étoiles double le risque qu’un avis soit faux (de 10 % à 20 %) : c’est un indice, pas une preuve.

### Exercice 6 · Un modèle, deux hôtels

Un modèle de prédiction des annulations signale 75 % des réservations qui seront annulées ; il signale aussi 10 % de celles qui seront honorées. On l’installe dans deux hôtels. Dans l’hôtel A, 40 % des réservations sont annulées ; dans l’hôtel B, 10 %.

1.  Imaginez 1 000 réservations de l’hôtel A. Combien d’alertes justes, combien de fausses alertes ? Calculez P(annulée \| signalée).
2.  Même question pour l’hôtel B.
3.  Le fournisseur annonce : « 75 % des annulations détectées, seulement 10 % de fausses alertes. » Pourquoi ces deux chiffres ne suffisent-ils pas à dire si une alerte est fiable ?

#### Corrigé

1.  400 annulées, dont 300 signalées ; 600 honorées, dont 60 signalées. P(annulée \| signalée) = 300 / 360 ≈ 0,833.
2.  100 annulées, dont 75 signalées ; 900 honorées, dont 90 signalées. 75 / 165 ≈ 0,455.
3.  La fiabilité d’une alerte, la précision du modèle, dépend du taux de base, propre à chaque hôtel. Le même modèle a raison cinq fois sur six dans l’hôtel A, moins d’une fois sur deux dans l’hôtel B. Vocabulaire : 75 % est le rappel, P(signalée \| annulée) ; la précision est P(annulée \| signalée).

### Exercice 7 · Vrai ou faux

Justifiez chaque réponse en une phrase.

1.  « 90 % des fraudes au paiement d’un hôtel viennent de cartes étrangères : 90 % des paiements par carte étrangère sont donc frauduleux. »
2.  « Si P(A \| B) = P(B \| A), avec des probabilités non nulles, alors P(A) = P(B). »
3.  « Un contrôle qui ne se trompe que dans 1 % des cas donne une alerte juste 99 fois sur 100. »
4.  « Si un test signale aussi souvent les cas positifs que les cas négatifs, P(B \| A) = P(B \| Ā), il n’apporte aucune information sur A. »

#### Corrigé

1.  Faux. La phrase confond P(étrangère \| fraude) et P(fraude \| étrangère) ; la seconde dépend aussi de la rareté des fraudes et de la part des cartes étrangères.
2.  Vrai. P(A \| B) × P(B) = P(A et B) = P(B \| A) × P(A) : si les deux probabilités conditionnelles sont égales et non nulles, P(A) = P(B).
3.  Faux. Tout dépend du taux de base : avec une fraude sur 500, un contrôle presque aussi fiable ne donne qu’une alerte juste sur onze (séance 2).
4.  Vrai. Alors P(A \| B) = P(A) : A et B sont indépendants (séance 1), et observer B ne change rien à la probabilité de A.

## Projet

Page : https://ad-c.github.io/mth101/projet.html

Les quatre missions de l’agence, tirées au sort le 9 octobre. Pour chacune : la commande du client, la note de cadrage et le kit de mission. Les missions tirées sont définitives.

### Jeudi 15 octobre : jalon 1

Une demi-journée en autonomie : un temps de cours, puis le jalon 1 de votre mission.

- [Feuille de route de la demi-journée (PDF)](https://ad-c.github.io/mth101/supports/projet/mth101-feuille-de-route-jalon-1.pdf)
- [Parcours en autonomie : les lois discrètes (PDF)](https://ad-c.github.io/mth101/supports/seance-04/mth101-seance-04-parcours-lois-discretes.pdf), les 60 premières minutes
- [Kit tuteur](https://ad-c.github.io/mth101/kit-tuteur.html) : la consigne pour vous servir d’un assistant IA comme d’un tuteur, et la règle d’usage de l’IA.
- [Carte du module (PDF)](https://ad-c.github.io/mth101/supports/polycopie/mth101-carte-du-module.pdf), à joindre au kit tuteur avec votre commande et votre note de cadrage.

**La règle du jalon 1.** Le protocole doit être synchronisé, donc visible sur github.com, avant le jeudi 15 octobre à 23 h 59. Il est commité avant toute analyse : aucun fichier de `projet/analyses/` ne le précède dans l’historique.

### Les missions

[Les quatre missions, en deux pages (PDF)](https://ad-c.github.io/mth101/supports/projet/mth101-synthese-missions.pdf)

| Mission | Commande | Note de cadrage | Kit, partie 1 |
|----|----|----|----|
| Les annulations | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-commande.pdf) | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-note-de-cadrage.pdf) | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-kit-partie-1.pdf) |
| Recommandé par l’IA | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-commande.pdf) | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-note-de-cadrage.pdf) | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-kit-partie-1.pdf) |
| Le temps d’attente | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-commande.pdf) | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-note-de-cadrage.pdf) | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-kit-partie-1.pdf) |
| Les robots de service | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-commande.pdf) | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-note-de-cadrage.pdf) | [PDF](https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-kit-partie-1.pdf) |

La partie 2 des kits arrive le 23 octobre, avec les jeux de répétition et le lancement de l’omnibus et des audits.

### Le tirage du 9 octobre

Huit équipes, numérotées de 1 à 8 ; les équipes 3 et 6 sont les trinômes. Graine : 8532.

| Équipe      | Mission               |
|-------------|-----------------------|
| 1           | Les annulations       |
| 2           | Les robots de service |
| 3 (trinôme) | Recommandé par l’IA   |
| 4           | Les annulations       |
| 5           | Le temps d’attente    |
| 6 (trinôme) | Recommandé par l’IA   |
| 7           | Le temps d’attente    |
| 8           | Les robots de service |

Pour refaire le tirage, dans le terminal d’un codespace :

``` bash
cd /tmp
curl -fsSL -O https://raw.githubusercontent.com/Ad-C/mth101/main/scripts/tirage-missions.py
python3 tirage-missions.py --equipes 8 --trinomes 3 6 --graine 8532
```

Le script : [`scripts/tirage-missions.py`](https://github.com/Ad-C/mth101/blob/main/scripts/tirage-missions.py), versé dans le domaine public ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr)). Il affiche aussi la chance de chaque équipe d’obtenir chaque mission : 1 sur 4, binôme ou trinôme.

## Les quatre missions de l’agence

*Thème, client, question, données. Daté du vendredi 9 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-synthese-missions.pdf

Synthèse des quatre commandes client, pour la présentation des missions du 9 octobre. Les clients sont fictifs ; les données sont réelles chaque fois que c’est possible, et citées comme telles. Chaque commande détaille ses données, leur licence et les jalons.

### Thème A · Séjourner

Hôtels et restaurants.

| Mission | Client (fictif) | Question du client | Données de départ |
|----|----|----|----|
| A1 · Les annulations | La direction d’un hôtel | « Une part importante de nos réservations est annulée. Faut-il imposer un acompte non remboursable, et combien de chambres pouvons-nous survendre ? » | Hotel booking demand : 119 390 réservations réelles de deux hôtels portugais, 2015–2017 (CC BY 4.0) |
| A2 · Recommandé par l’IA | La direction d’un hôtel | « Nos clients demandent de plus en plus conseil à des assistants IA. Qu’est-ce qui les pousse à recommander notre hôtel ? » | Un audit d’assistant IA mené par le binôme : au moins 200 requêtes, ordre des hôtels tiré au sort |

### Thème C · Une journée de loisirs

Grands sites de loisirs et de patrimoine.

| Mission | Client (fictif) | Question du client | Données de départ |
|----|----|----|----|
| C1 · Le temps d’attente | Un grand site de loisirs | « Quel temps d’attente afficher, et quel jour conseiller à nos visiteurs ? » | Relevés réels des temps d’attente de deux parcs de Disneyland Paris, toutes les 15 minutes, via Queue-Times |
| C2 · Les robots de service | La direction de la restauration d’un grand site de loisirs | « Un robot de service dans nos points de restauration : gadget, économie ou aide au personnel ? Et comment l’annoncer à nos visiteurs ? » | L’omnibus de l’agence ; études publiées sur l’acceptation des robots de service |

### Pour toutes les missions

Toutes les missions partagent le même livrable : un écrit qui répète le protocole sur données simulées, et une proposition d’action en soutenance le 12 novembre. Toutes placent une question dans l’omnibus de l’agence, questionnaire anonyme commun.

Attributions des données :

- Hotel booking demand : N. Antonio, A. de Almeida, L. Nunes, « Hotel booking demand datasets », *Data in Brief*, 22 (2019), 41–49, doi:10.1016/j.dib.2018.11.126, licence CC BY 4.0.
- Temps d’attente : Powered by [Queue-Times.com](https://queue-times.com/). Les parcs ne sont pas le client et ne sont associés ni au cours ni aux missions.

## Jeudi 15 octobre · Feuille de route

*Une demi-journée en autonomie, jusqu’au jalon 1. Daté du mardi 13 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-feuille-de-route-jalon-1.pdf

Une demi-journée en équipe, sans l’intervenant : un temps de cours, puis le jalon 1 de votre mission. Cette feuille vaut pour les quatre missions ; le kit de votre mission, partie 1, en donne le détail.

### 1. Le déroulé

| Durée | Quoi | Avec quoi |
|----|----|----|
| 60 min | Cours : les lois discrètes | Le « Parcours en autonomie : les lois discrètes », adresse ci-dessous |
| 10 min | Pause |  |
| 40 min | Projet : le benchmark | Kit, section 3 : trois à cinq sources, citées |
| 40 min | Projet : le protocole | Kit, section 1 : huit rubriques, une page |
| 30 min | Projet : la question pour l’omnibus | Kit, section 2 ; pour « Recommandé par l’IA », le plan de l’audit aussi |
| 30 min | Validation et synchronisation | La liste de contrôle ci-dessous |

Le parcours, avec son mode d’emploi minute par minute : <https://ad-c.github.io/mth101/supports/seance-04/mth101-seance-04-parcours-lois-discretes.pdf>. Ce qui n’y tient pas en 60 minutes se finit chez soi. Répartissez-vous le benchmark, mais rédigez le protocole ensemble : chacun doit pouvoir l’expliquer.

**La liste de contrôle**, avant de partir :

1.  `projet/protocole/protocole.md` : les huit rubriques sont remplies, sur une page.
2.  `projet/protocole/omnibus.md` : les deux versions, mot pour mot, et les réponses possibles. Pour « Recommandé par l’IA », aussi `projet/protocole/plan-audit.md`.
3.  Le benchmark : trois à cinq sources, citées en entier, dans un fichier du dépôt.
4.  `projet/analyses/` ne contient que son `README.md`.
5.  Chaque membre a commité depuis son propre compte, ou figure comme co-auteur (FAQ, question 8).
6.  Tout est validé, puis synchronisé : plus rien en attente dans **Contrôle de code source**.
7.  Sur github.com, depuis le navigateur, le protocole apparaît dans `projet/protocole/`.
8.  Le codespace est arrêté.

**La règle du jalon 1.** Le protocole doit être synchronisé, donc visible sur github.com, avant le jeudi 15/10 à 23 h 59. Il est commité avant toute analyse : aucun fichier de `projet/analyses/` ne le précède dans l’historique. Vérifiez sur github.com que votre commit y est arrivé.

### 2. Ce qu’on continue chez soi

- Les exercices laissés pour la maison le 7 et le 9/10, et la fin du parcours sur les lois discrètes.
- Les chapitres du polycopié, à mesure de leur parution.
- Le benchmark, au-delà des premiers repères du kit.
- La préparation des données : kit, section 4.

### 3. Les livrables et l’arrivée des données

| Date | Ce que vous rendez | Ce qui arrive |
|----|----|----|
| Jeu. 15/10, 23 h 59 | Jalon 1 : protocole, question d’omnibus, benchmark initial ; plan de l’audit pour « Recommandé par l’IA » |  |
| Ven. 23/10 |  | Votre jeu de répétition ; lancement de l’omnibus et des audits |
| Ven. 6/11 | Jalon 2 : analyses, simulateur, plan de la soutenance |  |
| Mar. 10/11 | L’écrit du volet 1 (date à confirmer) |  |
| Jeu. 12/11 | La soutenance |  |

Les relevés de temps d’attente, eux, arrivent chaque jour jusqu’au 12/11.

### 4. Où trouver de l’aide

- **Une difficulté avec GitHub** : la FAQ du cours, <https://ad-c.github.io/mth101/faq.html>.
- **Comprendre une notion, vérifier un raisonnement** : le kit tuteur, pour vous servir d’un assistant IA comme d’un tuteur, <https://ad-c.github.io/mth101/kit-tuteur.html>. L’IA est permise pour comprendre et vérifier, pas pour produire les livrables à la place de l’équipe (note de cadrage, section 7).
- **Une question sur la mission ou sur le cours** : l’intervenant, par e-mail, adrien.chiodo@ecole-89.com.
- **Les supports** : sur la page du cours, <https://ad-c.github.io/mth101/>, page « Projet » pour les documents des missions. Ils seront aussi déposés sur Brightspace, la nouvelle plateforme de l’école, quand elle sera ouverte.

## Parcours en autonomie

*Les lois discrètes · Jeudi 15 octobre, 60 minutes. Daté du jeudi 15 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/seance-04/mth101-seance-04-parcours-lois-discretes.pdf

**Avant de commencer.** Ouvrez votre codespace et synchronisez-le, pour récupérer ce que votre équipe a poussé. Si ce n’est pas déjà fait, tapez une fois dans un terminal (menu **Terminal**, **Nouveau terminal**) : `git config --global pull.rebase false`. Sans ce réglage, la synchronisation échoue dès que deux membres de l’équipe ont commité chacun de leur côté (FAQ du cours, question 3).

Les lois discrètes n’ont pas pu être traitées le 9 octobre : ce parcours les reprend, seul ou en équipe, en 60 minutes. Il ne demande que lire un tableau, multiplier et additionner des probabilités.

**Les chiffres.** 0,37 et 0,278 (hôtel de villégiature) sont les fréquences d’annulation observées dans Hotel booking demand : N. Antonio, A. de Almeida, L. Nunes, *Data in Brief*, 22 (2019), 41–49, doi:10.1016/j.dib.2018.11.126, licence CC BY 4.0. Les autres sont fictifs.

### Le mode d’emploi

| Minutes | Ce que vous faites |
|----|----|
| 0 à 20 | Lire le cours (section 1), crayon en main : refaites chaque exemple avant d’en lire la solution. |
| 20 à 40 | Les exercices 8, 10 et 13 (section 2). |
| 40 à 52 | Le notebook de la séance 3 (section 3) : la question « À vous » 1. |
| 52 à 60 | L’auto-évaluation (section 4), puis son corrigé. |

**Chez soi**, avant le 23 octobre : les exercices 9, 11, 12, 14 et 15, et les questions « À vous » 2 à 5. Les corrigés sont à la fin, après une page de séparation.

**De l’aide.** Une notion qui résiste : le kit tuteur, <https://ad-c.github.io/mth101/kit-tuteur.html>, qui fait d’un assistant IA un tuteur. Une question qui reste : l’intervenant, adrien.chiodo@ecole-89.com.

### 1. Le cours

#### 1.1 Variable aléatoire et loi de probabilité

Une **variable aléatoire** est un nombre qui dépend du hasard : le nombre d’annulations parmi 20 réservations, ou de nuits d’un séjour. On la note X.

Sa **loi de probabilité** est la liste de ses valeurs possibles, chacune avec sa probabilité. Chaque probabilité est comprise entre 0 et 1, et leur somme vaut 1 : il se passe toujours quelque chose.

**Exemple résolu : deux réservations.** Chacune est annulée avec la probabilité 0,37, indépendamment de l’autre. X, le nombre d’annulations, vaut 0, 1 ou 2.

1.  X = 0 : les deux sont honorées, 0,63 × 0,63 ≈ 0,397.
2.  X = 1 : deux chemins dans l’arbre, annulée puis honorée, ou honorée puis annulée : 2 × 0,37 × 0,63 ≈ 0,466.
3.  X = 2 : 0,37 × 0,37 ≈ 0,137.
4.  Vérification : 0,397 + 0,466 + 0,137 = 1.

#### 1.2 Espérance, variance, écart-type

L’**espérance** est la moyenne des valeurs, chacune pesée par sa probabilité : la moyenne que l’on observerait sur un très grand nombre de répétitions.

`E(X) = x₁ p₁ + x₂ p₂ + … + xₙ pₙ`

La **variance** mesure la dispersion autour de l’espérance : la moyenne des carrés des écarts. Le carré empêche les écarts positifs et négatifs de s’annuler.

`V(X) = (x₁ − E(X))² p₁ + … + (xₙ − E(X))² pₙ`

Plus rapide : V(X) = E(X²) − E(X)². L’**écart-type** σ(X) = √V(X) s’exprime dans l’unité de X ; la variance, dans son carré.

**Exemple résolu : la durée d’un séjour.**

| Nombre de nuits |   1 |   2 |   3 |   4 |
|-----------------|----:|----:|----:|----:|
| Probabilité     | 0,4 | 0,3 | 0,2 | 0,1 |

1.  E(X) = 1 × 0,4 + 2 × 0,3 + 3 × 0,2 + 4 × 0,1 = 2 : un séjour dure 2 nuits en moyenne. Sur 500 séjours, on attend environ 1 000 nuitées.
2.  Par la définition : V(X) = (1 − 2)² × 0,4 + 0 + (3 − 2)² × 0,2 + (4 − 2)² × 0,1 = 0,4 + 0,2 + 0,4 = 1.
3.  Par la formule rapide : E(X²) = 1 × 0,4 + 4 × 0,3 + 9 × 0,2 + 16 × 0,1 = 5, et V(X) = 5 − 2² = 1. On soustrait le carré de l’espérance, pas l’espérance.
4.  σ(X) = √1 = 1 nuit.

L’espérance n’est pas forcément une valeur possible : 2,3 nuits en moyenne, par exemple. Elle dit le niveau, l’écart-type la dispersion : une décision a besoin des deux.

#### 1.3 La loi de Bernoulli

Une épreuve, deux issues : une réservation est annulée ou non. X vaut 1 pour l’issue que l’on compte, appelée « succès » même si c’est une annulation, et 0 sinon. X vaut 1 avec la probabilité p, 0 avec la probabilité 1 − p. Alors E(X) = p et V(X) = p(1 − p).

**Exemple résolu : une réservation**, annulée avec la probabilité 0,37.

1.  E(X) = 0 × 0,63 + 1 × 0,37 = 0,37.
2.  V(X) = (0 − 0,37)² × 0,63 + (1 − 0,37)² × 0,37 = 0,2331, soit bien 0,37 × 0,63.
3.  σ(X) = √0,2331 ≈ 0,483.

#### 1.4 La loi binomiale

On répète n épreuves de Bernoulli **identiques**, de même probabilité de succès p, et **indépendantes** : l’issue de l’une ne change rien aux autres. Le nombre X de succès suit la loi binomiale B(n ; p).

`P(X = k) = (k parmi n) × p^k × (1 − p)^(n − k)`

Le coefficient se lit « k parmi n » : c’est le nombre de façons de placer les k succès parmi les n épreuves. n! se lit « factorielle n » : 1 × 2 × … × n, avec 0! = 1. En Python, `math.comb(20, 7)` donne 77 520.

`(k parmi n) = n! / (k! × (n − k)!)`

**Exemple résolu : trois réservations**, annulées chacune avec la probabilité 0,37. Quelle est la probabilité d’une seule annulation ?

1.  Les chemins à une annulation : AHH, HAH et HHA (A annulée, H honorée). Il y en a 3 : « 1 parmi 3 » vaut 3.
2.  Chaque chemin a la même probabilité : 0,37 × 0,63 × 0,63.
3.  P(X = 1) = 3 × 0,37 × 0,63² ≈ 0,441.

**Espérance et variance** : E(X) = np et V(X) = np(1 − p). X est la somme de n variables de Bernoulli, et l’espérance d’une somme est la somme des espérances, même sans indépendance. Pour 200 réservations de l’hôtel de villégiature, avec p = 0,278 : E(X) = 55,6 et σ(X) = √(200 × 0,278 × 0,722) ≈ 6,3. On attend 56 annulations, à 6 près environ.

**En Python**, avec 20 réservations et p = 0,37 :

``` python
from scipy.stats import binom

binom.pmf(7, 20, 0.37)   # P(X = 7), environ 0,181
binom.cdf(9, 20, 0.37)   # P(X <= 9)
binom.sf(9, 20, 0.37)    # P(X > 9), donc P(X >= 10), environ 0,165
```

`pmf` donne la probabilité d’une valeur, `cdf` la probabilité cumulée P(X ≤ k), `sf` le complément P(X \> k). Python écrit 0.37, avec un point.

**Une hypothèse à vérifier.** La loi binomiale suppose des épreuves indépendantes et de même probabilité. Une cause commune, une grève ou une tempête, peut lier les réservations : la loi binomiale ne s’applique plus telle quelle. Une hypothèse se justifie avant de servir.

#### 1.5 La loi de Poisson

Elle compte des événements indépendants, qui arrivent à un rythme moyen connu, λ (« lambda »), dans un intervalle : les clients qui arrivent à la réception en une heure, les appels au standard en une matinée. Aucun nombre d’épreuves n’est fixé : X peut valoir 0, 1, 2… sans limite haute.

`P(X = k) = e^(−λ) × λ^k / k!`

e vaut environ 2,718 ; en Python, `math.exp(-6)` calcule e⁻⁶. Alors E(X) = λ et V(X) = λ.

**Exemple résolu : la réception**, entre 17 h et 18 h, avec λ = 6 arrivées par heure.

1.  P(X = 0) = e⁻⁶ × 6⁰ / 0! = e⁻⁶ ≈ 0,002 : une heure sans aucune arrivée, presque jamais.
2.  P(X = 2) = e⁻⁶ × 6² / 2! = 18 e⁻⁶ ≈ 0,045.
3.  P(X ≥ 10) : `poisson.sf(9, 6)` ≈ 0,084, environ une heure sur douze.
4.  E(X) = 6 et σ(X) = √6 ≈ 2,45.

**De la binomiale à Poisson.** Beaucoup d’épreuves et un succès rare : la loi binomiale B(n ; p) est alors très proche de la loi de Poisson de paramètre λ = np. L’exercice 14 le montre sur les pannes d’un hôtel. En Python : `from scipy.stats import poisson`, puis `poisson.pmf(k, lam)`, `poisson.cdf(k, lam)` et `poisson.sf(k, lam)`, comme pour la binomiale.

### 2. Les exercices

Ils sont dans le fascicule d’exercices du 9 octobre, sur la page du cours : <https://ad-c.github.io/mth101/supports/seance-02-03/mth101-seances-02-03-exercices.pdf>. Calculatrice, ou Python dans votre codespace. Les trois premiers en séance ; les cinq suivants chez soi, dans cet ordre.

| Exercice | Ce qu’il fait travailler | Si vous bloquez, relisez |
|----|----|----|
| 8 · La durée des séjours | Espérance, variance par les deux formules | 1.2 et son exemple |
| 10 · Vingt réservations | La loi binomiale, sa formule, Python | 1.4 ; « 7 parmi 20 » est donné |
| 13 · La réception | La loi de Poisson | 1.5 et son exemple |
| 9 · Deux réservations | Une loi par un arbre ; reconnaître une binomiale | 1.1, puis 1.4 |
| 11 · Le petit-déjeuner | Binomiale et probabilité cumulée | 1.4, « En Python » |
| 12 · Binomiale ou pas ? | Les conditions de la loi binomiale | 1.4, « Une hypothèse à vérifier » ; 1.5 |
| 14 · Les pannes de la nuit | De la binomiale à Poisson | 1.5, dernier paragraphe |
| 15 · Le tirage au sort | Bernoulli, espérance d’une somme | 1.3 ; 1.4, « Espérance et variance » |

### 3. Le notebook de la séance 3

S’il n’est pas déjà dans votre dépôt, copiez-le, depuis le terminal :

``` bash
N=seance-03-simulation-binomiale-poisson.ipynb
curl -fsSL -o exercices/$N \
  https://raw.githubusercontent.com/Ad-C/mth101/main/notebooks/$N
```

Ouvrez-le, puis **Exécuter tout**. Dans le premier graphique, les barres (fréquences de 10 000 séries simulées de 20 réservations) et les points (probabilités de la loi B(20 ; 0,37)) se superposent ; la moyenne et la variance simulées sont proches de np et de np(1 − p). Simuler permet de vérifier un calcul, ou de s’en passer quand il manque.

En séance, la question « À vous » 1 ; chez soi, les questions 2 à 5 ; puis **Valider** et **Synchroniser les modifications**. Sans Codespaces : le lien « Ouvrir dans Colab » du README de `notebooks`.

### 4. L’auto-évaluation

Cinq questions courtes, sans aide, en huit minutes.

1.  Une variable X vaut 0, 1 ou 2. P(X = 0) = 0,5 et P(X = 1) = 0,3. Que vaut P(X = 2) ? Calculez E(X).
2.  Une variable de Bernoulli a pour paramètre p = 0,2. Que valent E(X) et V(X) ?
3.  Dix clients réservent chacun le dîner avec la probabilité 0,3, indépendamment les uns des autres. Quelle est la loi du nombre X de dîners réservés ? Calculez E(X) et σ(X).
4.  Le nombre d’appels au standard en une heure suit une loi de Poisson de paramètre 4. Que valent E(X) et V(X) ? Calculez P(X = 0).
5.  Vrai ou faux : « L’espérance d’une variable aléatoire est toujours l’une de ses valeurs possibles. »

**Arrêtez-vous ici.** Les corrigés commencent à la page suivante.

Cherchez d’abord : un corrigé lu sans avoir cherché ne laisse presque rien. Si vous bloquez, relisez le passage du cours que donne le tableau des exercices, ou demandez au kit tuteur un indice, pas la solution.

### Les corrigés

#### Exercice 8 · La durée des séjours

1.  1 − (0,35 + 0,25 + 0,20 + 0,15) = 0,05.
2.  E(X) = 0,35 + 0,50 + 0,60 + 0,60 + 0,25 = 2,3 : un séjour dure 2,3 nuits en moyenne.
3.  Par la définition : 1,69 × 0,35 + 0,09 × 0,25 + 0,49 × 0,20 + 2,89 × 0,15 + 7,29 × 0,05 = 1,51. Par la formule rapide : E(X²) = 6,8, et 6,8 − 2,3² = 1,51. σ(X) = √1,51 ≈ 1,23 nuit.
4.  Environ 120 × 2,3 = 276 nuitées.

#### Exercice 10 · Vingt réservations

1.  20 épreuves de Bernoulli de même probabilité 0,37, dont on compte les succès. Il faut supposer les réservations indépendantes : l’hypothèse se justifie, ou se discute.
2.  77 520 × 0,37⁷ × 0,63¹³ ≈ 0,181.
3.  `binom.cdf(5, 20, 0.37)` ≈ 0,191 ; `binom.sf(9, 20, 0.37)` ≈ 0,165.
4.  E(X) = 20 × 0,37 = 7,4 ; V(X) = 7,4 × 0,63 = 4,662 ; σ(X) ≈ 2,16.
5.  7 est la valeur la plus probable, mais elle ne se réalise qu’environ une fois sur cinq (0,181). Une fois sur six, il y aura au moins 10 annulations : une prévision s’accompagne de sa dispersion.

#### Exercice 13 · La réception

1.  P(X = 0) = e⁻⁶ ≈ 0,002 ; P(X = 6) = e⁻⁶ × 6⁶ / 6! ≈ 0,161.
2.  `poisson.sf(9, 6)` ≈ 0,084.
3.  E(X) = 6 ; σ(X) = √6 ≈ 2,45.
4.  e^(−1,5) ≈ 0,223 ; 1 − P(X = 0) − P(X = 1) − P(X = 2) ≈ 0,191. Le paramètre suit la durée : 6 arrivées par heure, 1,5 par quart d’heure.

#### Exercice 9 · Deux réservations

1.  P(X = 0) = 0,63² ≈ 0,397 ; P(X = 1) = 2 × 0,37 × 0,63 ≈ 0,466 ; P(X = 2) = 0,37² ≈ 0,137.
2.  E(X) = 0,4662 + 2 × 0,1369 = 0,74 ; E(X²) = 0,4662 + 4 × 0,1369 = 1,0138, d’où V(X) = 1,0138 − 0,74² = 0,4662.
3.  Ce sont np et np(1 − p) : X suit la loi binomiale B(2 ; 0,37).

#### Exercice 11 · Le petit-déjeuner

1.  B(12 ; 0,6).
2.  0,6¹² ≈ 0,0022 ; 0,4¹² ≈ 0,000017.
3.  E(X) = 7,2 ; V(X) = 12 × 0,6 × 0,4 = 2,88 ; σ(X) ≈ 1,70.
4.  10 couverts : P(X ≤ 10) ≈ 0,980, quand P(X ≤ 9) ≈ 0,917 reste sous 0,95. Préparer la moyenne, 7 couverts, laisserait des clients sans couvert plus de deux matins sur cinq : P(X ≥ 8) = 1 − 0,562 = 0,438.

#### Exercice 12 · Binomiale ou pas ?

1.  Oui : B(50 ; 0,2).
2.  Oui : B(7 ; 0,3).
3.  Non : le tirage se fait sans remise, la probabilité de tirer un enfant change d’un gagnant à l’autre ; les épreuves ne sont pas indépendantes.
4.  Non : la pluie d’un jour rend plus probable celle du lendemain, et la probabilité varie au fil du mois.
5.  Non : aucun nombre d’épreuves n’est fixé. C’est un cas pour la loi de Poisson.

#### Exercice 14 · Les pannes de la nuit

1.  B(400 ; 0,005) ; E(X) = 400 × 0,005 = 2.
2.  0,995⁴⁰⁰ ≈ 0,1347 ; e⁻² ≈ 0,1353.
3.  P(X ≥ 3) = 1 − e⁻² × (1 + 2 + 2) = 1 − 5 e⁻² ≈ 0,323 : une nuit sur trois environ. La loi binomiale donne aussi 0,323.

#### Exercice 15 · Le tirage au sort

1.  2/8 = 1/4 ; 4/8 = 1/2.
2.  Premier niveau de l’arbre : la mission préférée est celle à trois places (1/4), ou non (3/4). Second niveau : 3/9, ou 2/9. Formule des probabilités totales : 1/4 × 3/9 + 3/4 × 2/9 = 3/36 + 6/36 = 1/4.
3.  Chaque équipe obtient sa mission avec la probabilité 1/4 : une épreuve de Bernoulli. Le nombre d’équipes servies est la somme de ces huit épreuves, et l’espérance d’une somme est la somme des espérances, même sans indépendance : 8 × 1/4 = 2.
4.  Exactement deux, toujours : même espérance, 2, mais aucune dispersion.

#### Le notebook

1.  Par la simulation, environ 0,16 ; valeur exacte, `binom.sf(9, n, p)` ≈ 0,165.
2.  E(X) = 200 × 0,278 = 55,6 ; σ(X) = √(200 × 0,278 × 0,722) ≈ 6,34. Une simulation de 10 000 week-ends donne des valeurs proches.
3.  Environ 0,043 ; `poisson.sf(10, lam)` ≈ 0,0426.
4.  k = 10 : P(X ≤ 9) ≈ 0,916 reste sous 0,95, P(X ≤ 10) ≈ 0,957 ; `poisson.ppf(0.95, lam)` renvoie 10.
5.  Moins proches : P(X = 0) vaut 0,1285 contre 0,1353, P(X = 2) 0,2777 contre 0,2707. Avec 40 épreuves et p = 0,05, les épreuves sont moins nombreuses et le succès moins rare : l’approximation se dégrade.

#### L’auto-évaluation

1.  P(X = 2) = 1 − 0,5 − 0,3 = 0,2 ; E(X) = 0 × 0,5 + 1 × 0,3 + 2 × 0,2 = 0,7. Sinon, relisez 1.1 et 1.2.
2.  E(X) = 0,2 et V(X) = 0,2 × 0,8 = 0,16. Sinon, relisez 1.3.
3.  B(10 ; 0,3) ; E(X) = 3 ; V(X) = 2,1, d’où σ(X) ≈ 1,45. Sinon, relisez 1.4.
4.  E(X) = V(X) = 4 ; P(X = 0) = e⁻⁴ ≈ 0,018. Sinon, relisez 1.5.
5.  Faux : un séjour peut durer 2,3 nuits en moyenne (exercice 8). Sinon, relisez 1.2.

## MTH101 · Carte du module

*Ce que vous allez apprendre, dans quel ordre, et à quoi ça sert. Daté du vendredi 9 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/polycopie/mth101-carte-du-module.pdf

Cette carte donne une vue d’ensemble du module, presque sans formule. Les définitions, les méthodes et les exercices corrigés viennent ensuite, dans les chapitres du polycopié.

### Décider sans tout savoir

Un hôtel ne sait pas combien de clients descendront demain au petit-déjeuner. Une application ne sait pas si sa nouvelle page fera mieux que l’ancienne. Un filtre anti-spam ne sait pas si un message est indésirable : il calcule une probabilité. Il faut pourtant décider.

Ce module vous apprend à mesurer l’incertitude, puis à l’expliquer à qui doit trancher. C’est le travail de l’agence de conseil en données dont vous êtes les consultants juniors : chaque commande se termine par une réponse chiffrée et une recommandation.

### Six objectifs, en clair

Les six objectifs du module, tels que le syllabus les formule, et ce qu’ils veulent dire.

| N° | Objectif du syllabus | En clair |
|----|----|----|
| 1 | Calculer des probabilités conditionnelles et appliquer le théorème de Bayes. | Mettre à jour une probabilité quand une information arrive. |
| 2 | Identifier et mobiliser les lois de Bernoulli, binomiale, Poisson et normale. | Reconnaître les formes de hasard qui reviennent partout, et s’en servir. |
| 3 | Calculer et interpréter espérance, variance et écart-type. | Dire à quoi s’attendre en moyenne, et de combien la réalité peut s’en écarter. |
| 4 | Estimer un paramètre et construire un intervalle de confiance à 95 %. | Tirer un chiffre d’un échantillon, avec sa marge d’erreur. |
| 5 | Mettre en œuvre et interpréter un test d’hypothèse simple pour comparer deux proportions. | Juger si l’écart entre deux pourcentages dépasse ce que le hasard produit couramment. |
| 6 | Formuler une recommandation business argumentée à partir de résultats probabilistes et statistiques. | En faire un conseil clair, qu’un client non spécialiste peut suivre. |

### Le parcours

Le cours tient en une matinée et deux journées, du 7 au 23 octobre. Les après-midi en autonomie et la journée du 12 novembre sont consacrés aux missions.

| Date | Au programme | Chapitre |
|----|----|----|
| Mer. 7/10, matin | Probabilités, probabilités conditionnelles, indépendance | 1 |
| Ven. 9/10, matin | Le théorème de Bayes | 2 |
| Ven. 9/10, après-midi | Lois de Bernoulli, binomiale et de Poisson ; espérance, variance, écart-type | 3 |
| Jeu. 15/10, après-midi | En autonomie : les missions |  |
| Ven. 23/10, matin | Loi normale, intuition du théorème central limite | 4 |
| Ven. 23/10, après-midi | Estimation, intervalle de confiance à 95 %, test de deux proportions | 5 |
| Ven. 6/11, après-midi | En autonomie : les missions |  |
| Jeu. 12/11, journée | Soutenances |  |
| Jeu. 28/01, après-midi | Examen individuel, commun avec MTH102 |  |

Les chapitres 1 à 3 paraissent dans les jours qui suivent leur séance, le chapitre 1 avec une annexe, la boîte à outils. Les chapitres 4 et 5 paraissent avant le 23 octobre : vous pourrez les lire avant le cours. Le chapitre 6 relie les résultats à la décision. Il paraît avant le 6 novembre, pour préparer les soutenances. Un kit de révision suivra, avant l’examen, dont la forme vous sera communiquée.

### Comment se lit un chapitre

Tous les chapitres suivent le même plan.

1.  Une situation de l’agence : la question d’un client du tourisme.
2.  Le cœur mathématique : définitions, propriétés, méthode. C’est la partie qui prépare l’examen.
3.  Côté IA et data : le même outil dans les métiers que vous préparez.
4.  Ailleurs aussi : le même raisonnement dans la vie courante.
5.  Méthodes et pièges : les erreurs classiques, et comment les éviter.
6.  Des exercices gradués, corrigés en fin de chapitre.
7.  Pour aller plus loin : des ressources libres d’accès.

La boîte à outils rassemble les bases de calcul dont tout le reste dépend : fractions, pourcentages, symbole somme, notation des ensembles, lecture d’un tableau. Les chapitres y renvoient au moment où ils s’en servent.

**Les chiffres.** Les chiffres réels sont toujours donnés avec leur source. Les autres sont inventés pour l’exemple, et signalés comme tels.

### Les six chapitres, en mots

#### Chapitre 1 · Probabilités et probabilités conditionnelles

Une probabilité mesure la part des cas où un événement se produit, quand on répète l’expérience un grand nombre de fois. Une information change cette part : c’est la probabilité conditionnelle, « A sachant B ». L’ordre compte : la probabilité de A sachant B n’est pas celle de B sachant A. Deux événements sont indépendants quand savoir que l’un s’est produit ne change rien aux chances de l’autre. Multiplier leurs probabilités suppose cette indépendance, et il faut la justifier.

*À quoi ça sert.* À l’agence, à lire un tableau croisé sans se tromper de ligne ni de colonne. Côté IA, la précision et le rappel d’un modèle sont deux probabilités conditionnelles, prises dans un sens puis dans l’autre. Ailleurs, la météo : les jours où l’on annonce 70 % de risque de pluie, il devrait pleuvoir environ 7 fois sur 10.

#### Chapitre 2 · Le théorème de Bayes

Le théorème de Bayes retourne une probabilité conditionnelle : de la probabilité d’un indice sachant une cause, il tire celle de la cause sachant l’indice. Son résultat dépend beaucoup de la fréquence de départ, le « taux de base ». Un test fiable à 99 % peut ainsi produire une majorité de fausses alertes quand ce qu’il cherche est rare. Pour ne pas s’y perdre, raisonnez sur des effectifs, 10 000 cas par exemple, plutôt que sur des pourcentages.

*À quoi ça sert.* À l’agence, à juger ce que vaut une alerte, comme celle d’un système qui signale les réservations suspectes. Côté IA, c’est le principe des filtres anti-spam dits bayésiens, et la raison pour laquelle la précision d’un modèle dépend de la rareté de ce qu’il cherche. Ailleurs, c’est la bonne façon de lire un test médical positif.

#### Chapitre 3 · Lois discrètes ; espérance, variance, écart-type

Une variable aléatoire associe un nombre au résultat d’une expérience. La loi de Bernoulli décrit une épreuve à deux issues, oui ou non. La loi binomiale compte les succès sur un nombre fixé d’épreuves indépendantes de même probabilité. La loi de Poisson compte des événements qui surviennent au hasard, à un rythme moyen connu, pendant une durée donnée. L’espérance est la moyenne que l’on obtiendrait en répétant l’expérience un très grand nombre de fois. La variance et l’écart-type mesurent la dispersion autour de cette moyenne, l’écart-type dans la même unité que le résultat.

*À quoi ça sert.* À l’agence, à prévoir combien de clients viendront au petit-déjeuner, et avec quelle marge. Côté IA, à modéliser les conversions d’un test A/B ou le nombre de requêtes reçues par un serveur. Ailleurs, à modéliser le nombre de bonnes réponses d’un QCM rempli au hasard, ou de buts dans un match de football.

#### Chapitre 4 · Loi normale et théorème central limite

La loi normale, la courbe en cloche, est entièrement décrite par sa moyenne et son écart-type. Environ 95 % de ses valeurs tombent à moins de deux écarts-types de la moyenne. Le théorème central limite explique pourquoi on la rencontre si souvent : la moyenne d’un grand nombre d’observations indépendantes, tirées d’une même loi, suit à peu près une loi normale, même quand chaque observation n’en suit pas une. C’est grâce à lui qu’on pourra dire, au chapitre 5, avec quelle précision une moyenne ou un pourcentage est connu.

*À quoi ça sert.* À l’agence, à comprendre pourquoi la dépense moyenne de 200 clients d’un restaurant varie bien moins que la dépense d’un seul. Côté IA, le taux de bonnes réponses d’un modèle sur un jeu de test est une moyenne : le théorème aide à dire de combien il peut varier d’un jeu de test à l’autre.

#### Chapitre 5 · Estimation, intervalle de confiance, test de deux proportions

Un échantillon donne une estimation, un autre en donnerait une autre. L’intervalle de confiance à 95 % encadre la valeur inconnue par une méthode qui, appliquée à de nombreux échantillons, la capture environ 95 fois sur 100. La précision se paie en données : pour diviser la marge d’erreur par deux, il faut quatre fois plus d’observations. Le test de deux proportions pose une question précise : si les deux groupes avaient en réalité le même taux, un écart aussi grand que celui observé serait-il courant ? Enfin, pour savoir si une action produit un effet, on tire au sort qui la reçoit : c’est le principe du test A/B.

*À quoi ça sert.* À l’agence, à estimer la part des clients qui jugent acceptable un prix variant selon la demande, et à comparer deux groupes de clients. Côté IA, à évaluer un modèle avec sa marge d’erreur. Jev, présenté le 15 septembre 2026 par TypeSafe AI, répond par une probabilité plutôt que par un texte, et son fabricant le dit calibré : quand il annonce 90 %, il devrait avoir raison environ 9 fois sur 10. Le vérifier, c’est estimer une proportion avec son intervalle de confiance. Ailleurs, c’est la marge d’erreur d’un sondage.

#### Chapitre 6 · De la donnée à la décision : recommander sous incertitude

Ce que le client attend, c’est de savoir quoi faire. Une bonne recommandation le dit, avec le degré de certitude qui va avec, et précise ce qui ferait changer d’avis. Elle distingue un écart établi par les données d’un écart assez grand pour compter dans les affaires du client. Elle annonce ses limites sans se cacher derrière.

*À quoi ça sert.* À l’agence, aux commandes, à l’écrit des missions et aux soutenances. Côté IA, à décider, chiffres à l’appui, s’il faut remplacer un modèle en service par sa nouvelle version.

### Pour prendre de l’avance

Ces ressources sont libres d’accès. Elles montrent les mêmes idées autrement : en animations, en vidéos courtes, en code Python.

| Ressource | Ce que vous y trouverez | Chapitres |
|----|----|----|
| Khan Academy, en français : fr.khanacademy.org/math/statistics-probability | Des vidéos et des exercices corrigés, à votre rythme. | 1 à 5 |
| La statistique expliquée à mon chat, YouTube, en français | Des vidéos de quelques minutes : variables aléatoires, lois, théorème central limite. | 3 et 4 |
| Monsieur Phi, « La loi de Bayes (1/2) », YouTube, en français | Le raisonnement bayésien en douze minutes. | 2 |
| Seeing Theory, université Brown : seeing-theory.brown.edu, en anglais | Des visualisations interactives : on lance pièces et dés, et l’on voit les lois apparaître. | 1 à 5 |
| OpenIntro Statistics : openintro.org/book/os, en anglais | Un manuel d’introduction gratuit en PDF, riche en exercices. | 1 à 5 |
| Think Stats, Allen B. Downey : greenteapress.com/wp/think-stats-3e, en anglais | Probabilités et statistique pour programmeurs Python, en carnets Jupyter à exécuter en ligne. | 3 à 5 |

## Kit tuteur

Page : https://ad-c.github.io/mth101/kit-tuteur.html

Un assistant IA peut vous aider à comprendre une notion ou à vérifier un raisonnement, s’il joue le rôle d’un tuteur et non celui d’un sous-traitant. Cette page donne la consigne à lui confier, le fichier à lui joindre, et les règles de son usage dans le cours.

*Mise à jour : 14 octobre 2026.*

### La règle d’usage de l’IA

- L’IA est permise pour comprendre et vérifier, pas pour produire les livrables à la place de l’équipe.
- L’écrit se termine par une courte déclaration d’usage : les outils, et pour quoi faire.
- Chacun doit savoir expliquer tout ce que l’équipe rend.

L’assistant peut se tromper : en cas de doute, ce sont les documents du cours et l’intervenant qui font foi.

### Aucune donnée personnelle

Ne mettez dans la conversation aucune donnée personnelle : ni nom, ni adresse e-mail, ni numéro de téléphone, ni identifiant, ni rien qui permette de reconnaître une personne, que ce soit vous, un camarade ou un répondant de l’omnibus. Aucun mot de passe non plus.

### La base de connaissances

[Télécharger `base-connaissances.md`](https://raw.githubusercontent.com/Ad-C/mth101/main/tuteur/base-connaissances.md), mis à jour le 14 octobre 2026 : un seul fichier, qui réunit les documents publiés du cours, dont la commande, la note de cadrage et le kit de chaque mission, et la carte du module. Si le lien affiche le texte au lieu de l’enregistrer : clic droit sur le lien, puis « Enregistrer le lien sous… ».

- Ajoutez-le aux fichiers de votre projet Claude, ou joignez-le à la conversation de votre assistant.
- La consigne de cette page suffit.
- Téléchargez-le de nouveau après chaque mise à jour annoncée.

### En trois étapes

1.  **Ouvrez votre assistant IA**, dans une nouvelle conversation.
2.  **Joignez le fichier `base-connaissances.md`**, téléchargé ci-dessus, ou ajoutez-le aux fichiers de votre projet Claude. La commande et la note de cadrage de votre mission, et la carte du module, y sont déjà : inutile de joindre leurs PDF.
3.  **Collez la consigne ci-dessous**, après avoir remplacé les crochets : `[nom de la mission]` par le titre de votre mission, par exemple « Les annulations » ; `[nom de l'agence]` par le nom de l’agence, ou effacez-le, crochets compris, tant que ce nom n’est pas annoncé.

### La consigne

La consigne, telle qu’elle est donnée à copier sur la page :

```
Tu es le tuteur de notre équipe pour un projet de cours. Nous sommes étudiants en 1re année de Bachelor en intelligence artificielle, dans un module de probabilités et de statistique. Dans ce projet, nous jouons des consultants juniors de l’agence [nom de l’agence], spécialisée en données pour le tourisme et l’hôtellerie. Notre mission : [nom de la mission]. Le fichier joint, base-connaissances.md, réunit les documents publiés du cours, dont la commande du client et la note de cadrage de notre mission, et la carte du module.

Ton rôle : un tuteur, pas un sous-traitant.
- Explique les notions dont nous avons besoin, simplement, en partant de ce que nous savons, avec des exemples.
- Pose-nous des questions pour nous faire avancer, aide-nous à découper le travail, et vérifie nos raisonnements et nos calculs quand nous te les montrons.
- Ne rédige pas à notre place le protocole, l’écrit ou la soutenance, et ne nous donne pas le code complet d’une analyse. Donne plutôt des pistes, des indices, des exemples sur d’autres données, ou relis ce que nous avons écrit.
- N’invente ni chiffre, ni source. Dis-le quand tu ne sais pas.
- Pour les dates, les livrables, les données et les règles du cours, réponds uniquement à partir du fichier joint ; s’il n’en dit rien, dis-nous de demander à l’intervenant.
- Réponds en français, en dix lignes au plus, sauf si nous demandons davantage.
- Ne nous donne jamais la solution d’un exercice avant que nous ayons proposé la nôtre, et ne présente jamais une piste comme la réponse attendue par l’agence.

Pour commencer, pose-nous trois questions pour savoir où nous en sommes, puis propose-nous un plan de travail.
```

Si le bouton ne copie pas : cliquez dans le cadre, sélectionnez tout (Ctrl+A, ou Cmd+A sur Mac), puis copiez (Ctrl+C, ou Cmd+C).

## FAQ GitHub

Page : https://ad-c.github.io/mth101/faq.html

Les questions posées sur GitHub et Codespaces, avec leur réponse. Les libellés sont ceux de VS Code en français ; ceux de github.com restent en anglais. Le guide GitHub distribué en séance reste la référence pour les premiers pas.

*Mise à jour : 9 octobre 2026.*

**Une fois dans chaque nouveau codespace** : dans un terminal (menu ☰, **Terminal**, **Nouveau terminal**), tapez `git config --global pull.rebase false`. Sans ce réglage, la synchronisation échoue dès que vous et votre binôme avez commité chacun de votre côté (question 3).

### 1. Je vois le commit de mon binôme sur github.com, mais je ne peux pas modifier le fichier

La page d’un commit montre le dépôt figé à ce moment-là : elle sert à lire les changements, et le crayon y est grisé.

Pour modifier le fichier, passez par votre codespace, et faites-y d’abord entrer le commit de votre binôme. En bas à gauche, juste à droite de `main`, cliquez sur l’icône aux deux flèches en cercle (infobulle « Synchroniser les changements »). Le fichier se met à jour ; complétez-le.

Votre codespace ne se met jamais à jour tout seul : synchronisez en arrivant.

Après votre premier push, VS Code propose d’exécuter périodiquement « git fetch » : répondez **Oui**. Il vous signalera les commits de votre binôme (`1↓` à côté des deux flèches, en bas à gauche) ; il restera à synchroniser. Question fermée par erreur : roue dentée **Gérer**, **Paramètres**, cherchez `autofetch` et mettez la valeur sur `true`.

### 2. Enregistrer, Valider, Synchroniser : quelle différence ?

- **Enregistrer** met le fichier à jour dans votre codespace, et nulle part ailleurs. Dans le navigateur, l’enregistrement se fait aussi tout seul, après un court délai.
- **Valider** (le commit) prend une photo datée du dépôt, à votre nom. Elle reste dans votre codespace.
- **Synchroniser** envoie vos commits sur GitHub et rapatrie ceux de votre binôme.

Tant que vous n’avez pas synchronisé, ni votre binôme ni l’intervenant ne voient votre travail.

En arrivant, synchronisez. En partant, validez, synchronisez, puis arrêtez le codespace.

### 3. La synchronisation affiche une erreur

- **« Nettoyez l’arborescence de travail de votre dépôt avant l’extraction »** : vous avez des modifications non validées. Cliquez d’abord sur **Valider**, puis synchronisez.
- **Un message qui commence par « Git : »**, dont le détail (**Afficher la sortie de commande**) parle de *divergent branches* : vous et votre binôme avez commité chacun de votre côté. Dans un terminal (menu ☰, **Terminal**, **Nouveau terminal**), tapez `git config --global pull.rebase false`, une fois par codespace, puis synchronisez de nouveau.
- **« Il existe des conflits de fusion »** : vous avez modifié les mêmes lignes. Ouvrez le fichier listé sous **Fusionner les changements**. Au-dessus de chaque bloc en conflit, choisissez **Accepter la modification actuelle** (la vôtre), **Accepter la modification entrante** (celle de votre binôme) ou **Accepter les deux modifications**. Relisez et enregistrez. Cliquez ensuite sur **Continuer** (pendant une fusion, c’est le nom du bouton **Valider**), puis synchronisez. Si le conflit porte sur un notebook (`.ipynb`), ne validez rien et prévenez l’intervenant.

Pour l’éviter, synchronisez en arrivant, et ne modifiez pas un même fichier à deux en même temps, surtout un notebook.

### 4. Mon binôme ne voit pas le dépôt (erreur 404)

Il doit accepter l’invitation, connecté avec son propre compte :

- depuis le mail reçu ;
- ou sur `https://github.com/<compte du propriétaire>/mth101/invitations`, bouton **Accept invitation**.

Une invitation expire sept jours après son envoi. Passé ce délai, le propriétaire du dépôt invite de nouveau : **Settings**, **Collaborators**, **Add people**.

Une erreur 404 vient aussi, souvent, d’une connexion avec un autre compte.

### 5. Comment savoir si je suis dans le bon codespace ?

Sur <https://github.com/codespaces>, chaque codespace indique son dépôt. Le vôtre doit être celui de votre binôme, `<compte du propriétaire>/mth101`. Ce ne doit être ni `Ad-C/mth101` (le dépôt du cours, qui porte le même nom), ni `Ad-C/mth101-modele`. Dans le terminal, `git remote -v` affiche la même adresse.

Trois signes d’alerte :

- le panneau **Contrôle de code source** propose **Publier Branch** (c’est bien le libellé) ;
- l’icône en bas à gauche est un nuage ;
- vos commits n’arrivent pas dans le dépôt de l’équipe.

Dans un codespace ouvert sur un dépôt où vous ne pouvez pas écrire, un commit fait depuis le panneau **Contrôle de code source** crée une copie publique (un *fork*) sous votre compte, sans rien vous demander.

Dans tous les cas : n’effacez rien et prévenez l’intervenant. Ouvrez ensuite le bon codespace depuis la page du dépôt de l’équipe : **Code**, onglet **Codespaces**.

### 6. Le notebook ne s’exécute pas, ou ne trouve pas pandas

En haut à droite du notebook : **Sélectionner le noyau**, puis **Python Environments**, puis **Python 3.12**.

S’il manque encore une bibliothèque, tapez dans un terminal, à la racine du dépôt :

``` bash
pip3 install --user -r requirements.txt
```

Elle installe les mêmes bibliothèques que le codespace à sa création. Relancez ensuite **Exécuter tout**.

### 7. Mon codespace s’est arrêté. Combien de temps puis-je l’utiliser ?

Un codespace s’arrête seul après 30 minutes d’inactivité. Rien n’est perdu : rouvrez-le depuis <https://github.com/codespaces>.

Le quota gratuit, environ 60 heures par mois, est décompté sur le compte de la personne qui a créé le codespace. En fin de séance, arrêtez-le : **…**, puis **Stop codespace**.

Gardez un seul codespace par dépôt et supprimez les autres : **…**, puis **Delete**. Un codespace occupe de l’espace même arrêté. Un codespace inutilisé pendant 30 jours est supprimé, avec tout ce qui n’a pas été synchronisé.

### 8. On a travaillé à deux sur un seul ordinateur : comment apparaître tous les deux ?

Le commit porte le nom du compte connecté. Pour créditer l’autre, terminez le message de commit par une ligne vide, puis une ligne de co-auteur :

```
Commande 2 : calculs et recommandation

Co-authored-by: Prénom <12345678+login@users.noreply.github.com>
```

Chacun trouve son adresse sur <https://github.com/settings/emails>, sous *Keep my email addresses private*, et la donne une fois à son binôme. Le commit s’affiche alors avec ses deux auteurs.

Plus simple : alternez au clavier, et chacun valide ce qu’il a écrit.

### 9. Comment pré-enregistrer notre protocole ?

Écrivez-le dans un fichier du dossier `projet/protocole/`, par exemple `protocole.md`. Validez et synchronisez avant d’ajouter quoi que ce soit dans `projet/analyses/`. Vérifiez ensuite sur github.com qu’il apparaît bien dans le dossier.

Le `README.md` déjà présent vient du modèle : ce n’est pas votre protocole. Toute modification ultérieure reste visible, et datée, dans l’historique.

### 10. Comment l’intervenant suit-il les dépôts ?

Chaque semaine, et à chaque jalon, il lit l’historique de votre dépôt : les dates, les auteurs, les fichiers. Il regarde trois choses :

- la régularité du travail ;
- la présence de chaque membre ;
- le respect des jalons, par exemple, au 15 octobre, un protocole commité avant toute analyse.

Le nombre de commits n’est pas une note : en multiplier de tout petits n’apporte rien. Si un membre n’apparaît plus depuis une semaine, l’intervenant pose la question à l’équipe : c’est une question, pas une sanction. Pour un travail à deux sur un seul écran, voir la question 8.

Ses notes de suivi restent chez lui, hors de tout dépôt, et sont supprimées à la fin de la période d’évaluation.

Une question qui n’est pas ici ? Posez-la en séance : elle rejoindra cette page.

## Notebooks

Page : https://github.com/Ad-C/mth101/tree/main/notebooks

Les notebooks des séances, à copier dans le dossier `exercices/` du dépôt de votre binôme, puis à compléter et à pousser avec vos réponses.

### Séance 3 · Simuler les lois binomiale et de Poisson

Dans le terminal de votre codespace, à la racine de votre dépôt, collez :

``` bash
curl -fsSL -o exercices/seance-03-simulation-binomiale-poisson.ipynb https://raw.githubusercontent.com/Ad-C/mth101/main/notebooks/seance-03-simulation-binomiale-poisson.ipynb
```

Ouvrez ensuite `exercices/seance-03-simulation-binomiale-poisson.ipynb`, puis **Exécuter tout**. À la fin : commit et push.

Si Codespaces ne répond pas : [ouvrir le notebook dans Google Colab](https://colab.research.google.com/github/Ad-C/mth101/blob/main/notebooks/seance-03-simulation-binomiale-poisson.ipynb) (compte Google requis ; enregistrez une copie avant de le modifier).

### Licence

Les notebooks de ce dossier sont versés dans le domaine public, [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr) : copiez-les et modifiez-les librement.

## Adresses utiles

- La page du cours : https://ad-c.github.io/mth101/
- Les résumés des séances passées, avec leurs supports : https://ad-c.github.io/mth101/seances.html
- Le projet (commandes, notes de cadrage, kits, feuille de route, tirage) : https://ad-c.github.io/mth101/projet.html
- Le kit tuteur et la règle d’usage de l’IA : https://ad-c.github.io/mth101/kit-tuteur.html
- La FAQ GitHub : https://ad-c.github.io/mth101/faq.html
- Le dépôt du cours, qui se consulte sans y écrire : https://github.com/Ad-C/mth101
- Le dépôt modèle, d’où chaque équipe a créé son dépôt privé : https://github.com/Ad-C/mth101-modele
- Les notebooks des séances, à copier dans le dossier exercices/ de son dépôt : https://github.com/Ad-C/mth101/tree/main/notebooks
- Les relevés de temps d’attente : https://github.com/Ad-C/mth101/tree/main/donnees/queue-times (Powered by Queue-Times.com)
- L’intervenant, Adrien Chiodo : adrien.chiodo@ecole-89.com
- Brightspace, la nouvelle plateforme de l’école : les supports y seront aussi déposés quand elle sera ouverte.

<!-- partie: a1-annulations -->

# Mission « Les annulations »

## Mission A1 · Les annulations

*Le vrai coût d’une chambre vide. Daté du vendredi 9 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-commande.pdf

Thème A, « Séjourner » : hôtels et restaurants. Commande transmise à l’agence par son associé.

### Le client

La direction d’un hôtel (client fictif). Une part de ses réservations est annulée trop tard pour que la chambre soit revendue. Deux leviers sont sur la table : exiger un acompte non remboursable, et accepter plus de réservations qu’il n’y a de chambres, au risque de devoir reloger ailleurs un client qui arrive.

> « Une part importante de nos réservations est annulée. Faut-il imposer un acompte non remboursable, et combien de chambres pouvons-nous survendre ? »

### Ce que l’agence doit livrer

**Un écrit : la répétition du protocole (volet 1).** Avant de mener une expérience chez un client, l’agence la répète sur des données simulées, pour vérifier sa chaîne d’analyse et la taille d’échantillon nécessaire. Le 23 octobre, votre binôme reçoit son propre jeu de données simulé. Vous y menez l’analyse prévue par votre protocole : estimation, intervalle de confiance à 95 %, test de comparaison de deux proportions, conclusion. Quatre à six pages, selon la grille commune de l’agence : question, données, effet estimé, intervalle de confiance, test, importance pratique, limites, recommandation, condition de réexamen.

**Une proposition d’action, en soutenance le 12 novembre** (10 minutes d’exposé, 8 de questions) :

1.  **La problématique** du client, formulée dans ses mots.
2.  **Le benchmark** : études publiées, pratiques documentées du secteur, données ouvertes analysées par vous.
3.  **Le modèle de décision** : un simulateur de surbooking (loi binomiale) que le jury peut manipuler. Combien de réservations accepter au-delà du nombre de chambres, selon le coût d’un client à reloger et celui d’une chambre vide, à partir des taux d’annulation tardive estimés par segment de clientèle.
4.  **Le protocole proposé** : le test A/B qui trancherait la question chez le client (métrique, tirage au sort, taille d’échantillon, durée, règle de décision).

### Les données de départ

Faute de données du client, l’agence s’appuie sur les réservations réelles de deux hôtels portugais : 119 390 réservations, dans un hôtel de villégiature en Algarve et un hôtel urbain à Lisbonne, pour des arrivées du 1^(er) juillet 2015 au 31 août 2017. Ce ne sont pas les chiffres du client : la recommandation doit le dire. Une réservation « annulée » y inclut les clients absents sans prévenir.

Source : N. Antonio, A. de Almeida, L. Nunes, « Hotel booking demand datasets », *Data in Brief*, 22 (2019), 41–49, doi:10.1016/j.dib.2018.11.126. Licence CC BY 4.0 : tout rendu qui utilise ces données cite cette source.

### Les jalons

| Date | Étape |
|----|----|
| Jeu. 15/10 | Jalon 1 : benchmark initial, question omnibus, protocole pré-enregistré |
| Ven. 23/10 | Remise du jeu de répétition ; lancement de l’omnibus |
| Ven. 6/11 | Jalon 2 : analyses, simulateur, préparation de la soutenance |
| Mar. 10/11 | Remise de l’écrit (date à confirmer) |
| Jeu. 12/11 | Soutenances |

### Ce que vous proposerez au jalon 1

- **Votre question pour l’omnibus de l’agence.** L’omnibus est un questionnaire anonyme commun à toute l’agence, diffusé à partir du 23 octobre. Chaque mission y place une question en deux versions, attribuées au hasard aux répondants : la comparaison des deux versions doit éclairer la question du client.
- **Votre protocole**, pré-enregistré par un commit dans votre dépôt avant toute analyse. C’est lui que vous répéterez sur le jeu simulé, puis que vous proposerez au client.

## Les annulations · Note de cadrage

*Le vrai coût d’une chambre vide. Daté du vendredi 9 octobre 2026, mise à jour le 13 octobre.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-note-de-cadrage.pdf

De l’associé de l’agence à l’équipe chargée de la mission. La commande dit ce que veut le client ; cette note, ce que l’agence attend de vous et comment vous y prendre. Gardez les deux sous la main.

### 1. En un coup d’œil

- **Thème** : « Séjourner », hôtels et restaurants.
- **Mission** : Les annulations, le vrai coût d’une chambre vide.
- **Client** : la direction d’un hôtel (client fictif).
- **Sa question** : « Une part importante de nos réservations est annulée. Faut-il imposer un acompte non remboursable, et combien de chambres pouvons-nous survendre ? »
- **Votre objectif** : éclairer les deux décisions du client, l’acompte et la survente, par une analyse chiffrée, un simulateur et un protocole de test.

### 2. Les enjeux

Une chambre restée vide une nuit est un revenu perdu pour de bon : elle ne se stocke pas. Or l’annulation gratuite est devenue un argument de vente des plateformes de réservation, et une annulation de dernière minute laisse peu de temps pour revendre la chambre. Les hôtels ont deux parades, que les compagnies aériennes pratiquent aussi : faire payer d’avance une partie des clients, et accepter plus de réservations qu’ils n’ont de places. Chacune a un prix. En fixer le niveau est l’un des métiers du *revenue management*, et c’est une affaire de probabilités.

### 3. Les mathématiques en jeu

| Notion du cours | Vue le | Dans la mission |
|----|----|----|
| Probabilités conditionnelles | 7/10, reprise le 9/10 | La probabilité d’annulation selon les caractéristiques d’une réservation |
| Loi binomiale | 9/10, après-midi | Le nombre de clients qui se présentent, parmi les réservations acceptées |
| Espérance, variance, écart-type | 9/10, après-midi | Le coût attendu d’un niveau de survente, et sa dispersion |
| Loi normale ; intervalle de confiance à 95 %, test de deux proportions | 23/10 | L’écrit du volet 1 ; le protocole proposé au client |
| De la donnée à la décision | Avant le 6/11 | La recommandation (polycopié, chapitre 6) |

### 4. Les données

Les réservations réelles de deux hôtels portugais, décrites dans la commande avec leur source et leur licence (CC BY 4.0) : tout rendu qui les utilise cite l’article. Le jeu est publié avec l’article, qui décrit chacune de ses variables : <https://doi.org/10.1016/j.dib.2018.11.126>.

Ce que l’équipe produit elle-même : **sa question pour l’omnibus de l’agence**, en deux versions attribuées au hasard, proposée au jalon 1 ; les réponses arrivent à partir du 23/10. Le même jour, vous recevez votre propre jeu de données simulé, pour l’écrit du volet 1.

### 5. Des pistes de réflexion

Celles qu’un consultant se pose avant de chiffrer. À vous d’en trouver d’autres.

1.  Que gagne l’hôtel à exiger un acompte non remboursable, et que risque-t-il d’y perdre ?
2.  Que vaut, pour votre client, l’expérience de deux hôtels portugais de 2015–2017 ?
3.  Comment hôtels et plateformes de réservation présentent-ils leurs conditions d’annulation ?
4.  Quels autres leviers un hôtel a-t-il contre les annulations tardives ?
5.  Dans votre test chez le client, qui verra quelle offre, pendant combien de temps, et quel résultat vous fera conclure ?
6.  Que doit savoir la direction pour décider : un chiffre, une marge, une règle de conduite ?

### 6. Ce qu’on attend

#### Les livrables

- **Le protocole** : une page, pré-enregistrée dans `projet/protocole/`.
- **La question pour l’omnibus** : deux versions, attribuées au hasard.
- **Le benchmark** : trois à cinq sources, citées.
- **Le simulateur** : un notebook dans `projet/simulateur/`, avec deux ou trois paramètres que le jury peut faire varier.
- **L’écrit du volet 1** : quatre à six pages, selon la grille commune de la commande.
- **La soutenance** : 10 minutes d’exposé, 8 de questions.

#### Trois niveaux

Ils reprennent ce que l’agence regarde : la justesse des calculs, la qualité de la recommandation, la clarté, l’honnêteté sur les limites et le simulateur.

**Le socle, ce qu’il faut pour valider.**

- Le protocole est pré-enregistré à temps et complet : métrique, tirage au sort, taille d’échantillon, durée, règle de décision.
- L’écrit suit la grille commune, et ses calculs sont justes.
- Le simulateur tourne : pour un nombre de chambres et un nombre de réservations acceptées, il donne la probabilité de devoir reloger au moins un client.
- La recommandation répond aux deux questions du client, et dit d’où viennent les chiffres.

**Un très bon travail.**

- Les taux qui nourrissent le simulateur sont estimés sur les données, avec leur intervalle de confiance, et non posés à la main.
- Chaque résultat est traduit dans la langue du client : des chambres, des nuits, des euros.
- Le benchmark est confronté à vos propres chiffres : ce qui concorde, ce qui diffère, et pourquoi.
- Chaque limite est nommée, avec ce qu’elle change à la recommandation.

**Un excellent travail.**

- La recommandation tient en une règle de survente que le service des réservations peut appliquer telle quelle, avec la condition qui la ferait réviser.
- En séance, le jury fait varier les paramètres sans aide et voit la décision changer.
- L’équipe va au-delà de la commande, et le justifie : une source de plus, ou la preuve qu’un résultat tient quand une hypothèse change.
- Une notion difficile devient claire pour un non-spécialiste, en une minute.

Une équipe de trois vise au moins un élément du niveau « excellent ».

### 7. L’organisation

**Des rôles suggérés** : données et simulateur ; benchmark et protocole ; rédaction et soutenance. Un rôle par membre dans une équipe de trois ; à deux, partagez le troisième. Chacun relit le travail des autres, et doit pouvoir répondre le 12/11 à une question sur n’importe quelle partie. **Chacun commite depuis son propre compte** : l’historique du dépôt montre qui a fait quoi.

| Date | Ce qui est attendu |
|----|----|
| Jeu. 15/10 | Jalon 1 : protocole, question d’omnibus, benchmark initial |
| Ven. 23/10 | Jeu simulé à analyser selon votre protocole ; omnibus lancé |
| Ven. 6/11 | Jalon 2 : analyses, simulateur qui tourne, plan de la soutenance |
| Mar. 10/11 | Remise de l’écrit du volet 1 (date à confirmer) |
| Jeu. 12/11 | Soutenance devant un jury, auquel des professionnels pourront se joindre |

**La règle du jalon 1.** Le protocole doit être synchronisé, donc visible sur github.com, avant le jeudi 15/10 à 23 h 59. Il est commité avant toute analyse : aucun fichier de `projet/analyses/` ne le précède dans l’historique. Vérifiez sur github.com que votre commit y est arrivé.

**L’usage de l’IA.** Elle est permise pour comprendre et vérifier, pas pour produire les livrables à la place de l’équipe. L’écrit se termine par une courte déclaration d’usage (outils, et pour quoi faire). Chacun doit savoir expliquer tout ce que l’équipe rend. Kit tuteur et FAQ GitHub : <https://ad-c.github.io/mth101/>.

### 8. Pour démarrer ce week-end

1.  Lisez la commande et cette note ensemble, et notez vos questions au client.
2.  Lisez, dans l’article du jeu de données, la description des variables.
3.  Créez `projet/protocole/protocole.md` et rédigez-en une première version.

## Les annulations · Kit, partie 1

*Préparer le jalon 1 : protocole, omnibus, benchmark, données. Daté du mardi 13 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-a1-annulations-kit-partie-1.pdf

Le kit donne les outils de la mission ; la commande et la note de cadrage restent les références. Cette première partie prépare le jalon 1 du jeudi 15/10. La seconde arrivera le 23/10, avec votre jeu de répétition et le lancement de l’omnibus.

### 1. Le modèle de protocole

Le protocole décrit le test que vous proposeriez au client : ce que vous mesurerez, et comment vous déciderez, écrit avant d’avoir vu un seul résultat. Copiez les huit titres ci-dessous dans `projet/protocole/protocole.md`, et remplissez chacun en quelques lignes : le tout tient sur une page.

1.  **La question de décision.** La décision que le client prendra selon votre résultat, en une phrase.
2.  **L’hypothèse.** Ce que vous pensez trouver, et pourquoi.
3.  **La métrique.** Une proportion, mesurée de la même façon dans les deux groupes, et sa définition exacte : ce qui compte, et à quel moment.
4.  **L’unité tirée au sort.** Ce qui reçoit l’une ou l’autre version, une personne ou une période par exemple, et la façon dont le hasard est tiré.
5.  **La taille d’échantillon visée.** Un ordre de grandeur suffit à ce stade : quelques dizaines, centaines ou milliers d’unités par groupe ? Le cours du 23/10 vous donnera de quoi la calculer.
6.  **La durée.** Combien de temps le test tournera chez le client, et pourquoi.
7.  **La règle de décision.** Quel résultat vous fera recommander quoi.
8.  **Les limites prévues.** Ce que votre test ne pourra pas dire.

**Pour votre mission.** La commande pose deux questions, l’acompte et la survente : dites laquelle votre test tranche.

Toute modification ultérieure du protocole reste visible, et datée, dans l’historique du dépôt (FAQ, question 9).

### 2. La question pour l’omnibus

L’omnibus est le questionnaire anonyme commun à toute l’agence, diffusé à partir du 23/10. Votre question y figure en deux versions : chaque répondant reçoit l’une ou l’autre, au hasard, et vous comparez les réponses d’une version à l’autre.

1.  **Deux versions, une seule différence.** Mêmes mots, même ordre, mêmes réponses possibles, sauf l’élément que vous testez.
2.  **Une formulation neutre.** Rien qui pousse vers une réponse : ni adjectif qui juge, ni « ne pensez-vous pas que… ».
3.  **Une réponse fermée.** Deux ou trois réponses fixées, par exemple « Oui » et « Non » : chacune se compte, et donne une proportion par version.
4.  **Une question courte, lisible par tous.** Lue en moins de vingt secondes, sans rien connaître du client ; rien qui permette d’identifier le répondant.

Au jalon 1, commitez dans `projet/protocole/omnibus.md` : les deux versions, mot pour mot ; les réponses possibles ; en une phrase, ce que leur comparaison apprendra au client. L’agence assemble les questions des quatre missions en un seul questionnaire, et peut vous demander de retoucher la vôtre.

**Pour votre mission.** La comparaison des deux versions doit éclairer l’une des deux décisions du client. Choisissez une situation de réservation que chacun peut imaginer, sans connaître l’hôtel.

### 3. Les premiers repères de benchmark

Des références sûres, pour commencer. Votre benchmark les complète par vos propres recherches : études publiées, pratiques documentées du secteur, données ouvertes. Pour chaque source, notez qui l’a écrite, quand, et sur quelles données ; citez-la en entier. Gardez-les dans un fichier du dépôt, par exemple `projet/benchmark.md`.

- Service-public.fr, « Acompte, avance, arrhes et avoir : quelles différences ? », fiche vérifiée le 5 août 2025, <https://www.service-public.gouv.fr/particuliers/vosdroits/F31187>. Ce que dit le droit français d’une somme versée d’avance, quand votre client parle d’« acompte ».
- M. Kmiecik, N. Antonio, « Cancel, rebook, save: Revenue leakage from price cuts in hotels », *International Journal of Hospitality Management*, 135 (2026), 104647, doi:10.1016/j.ijhm.2026.104647, en accès libre (CC BY 4.0). Ce que coûtent les annulations gratuites quand des clients annulent pour réserver de nouveau moins cher, sur plus de deux millions de réservations portugaises.
- S. E. Kimes, « Yield management: A tool for capacity-considered service firms », *Journal of Operations Management*, 8(4) (1989), 348–363, doi:10.1016/0272-6963(89)90035-1 ; version de l’autrice en accès libre : <https://hdl.handle.net/1813/72066>. Le texte fondateur du *revenue management* : vendre une capacité fixe qui ne se stocke pas.
- S. Ivanov, *Hotel Revenue Management: From Theory to Practice*, Varna, Zangador, 2014, en accès libre : <https://ssrn.com/abstract=2447337>. Un manuel de *revenue management* hôtelier : cherchez-y la survente (*overbooking*) et les conditions d’annulation.

### 4. Les données de départ

**Où.** Dans l’annexe de l’article qui décrit le jeu, en accès libre : N. Antonio, A. de Almeida, L. Nunes, « Hotel booking demand datasets », *Data in Brief*, 22 (2019), 41–49, <https://doi.org/10.1016/j.dib.2018.11.126>. L’archive contient deux fichiers : `H1.csv`, l’hôtel de villégiature (40 060 réservations), et `H2.csv`, l’hôtel urbain (79 330). L’article décrit chaque variable : lisez-le d’abord.

**Comment les ouvrir.** Dans le terminal du codespace, à la racine du dépôt :

``` bash
curl -fsSL -o projet/donnees/hotel-booking-demand.zip \
  https://ars.els-cdn.com/content/image/1-s2.0-S2352340918315191-mmc2.zip
```

Notez la source et la date dans `projet/donnees/README.md`. Puis, après le jalon, dans un notebook de `projet/analyses/` :

``` python
import zipfile
import pandas as pd

archive = zipfile.ZipFile("../donnees/hotel-booking-demand.zip")
villegiature = pd.read_csv(archive.open("H1.csv"))
urbain = pd.read_csv(archive.open("H2.csv"))
```

Certaines valeurs texte sont complétées par des espaces : `.str.strip()` les retire.

**Sous quelle licence.** CC BY 4.0 : tout rendu qui utilise ces données cite l’article.

Votre question d’omnibus vous apportera d’autres réponses, après la collecte qui commence le 23/10.

**Avant le protocole, aucune analyse.** Rien n’entre dans `projet/analyses/` avant que le protocole soit commité et synchronisé (règle du jalon 1, note de cadrage, section 7).

<!-- partie: a2-recommandation-ia -->

# Mission « Recommandé par l’IA »

## Mission A2 · Recommandé par l’IA

*Quel hôtel l’IA recommande-t-elle ? Daté du vendredi 9 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-commande.pdf

Thème A, « Séjourner » : hôtels et restaurants. Commande transmise à l’agence par son associé.

### Le client

La direction d’un hôtel (client fictif). Avant de réserver, des voyageurs demandent maintenant conseil à des assistants IA. La direction veut comprendre ce qui fait qu’un assistant recommande un hôtel plutôt qu’un autre, et comment présenter le sien.

> « Nos clients demandent de plus en plus conseil à des assistants IA. Qu’est-ce qui les pousse à recommander notre hôtel ? »

### Ce que l’agence doit livrer

**Un écrit : la répétition du protocole (volet 1).** Avant de mener une expérience chez un client, l’agence la répète sur des données simulées, pour vérifier sa chaîne d’analyse et la taille d’échantillon nécessaire. Le 23 octobre, votre binôme reçoit son propre jeu de données simulé. Vous y menez l’analyse prévue par votre protocole : estimation, intervalle de confiance à 95 %, test de comparaison de deux proportions, conclusion. Quatre à six pages, selon la grille commune de l’agence : question, données, effet estimé, intervalle de confiance, test, importance pratique, limites, recommandation, condition de réexamen.

**Une proposition d’action, en soutenance le 12 novembre** (10 minutes d’exposé, 8 de questions) :

1.  **La problématique** du client, formulée dans ses mots.
2.  **Le benchmark** : études publiées, pratiques documentées du secteur, données ouvertes analysées par vous.
3.  **Le modèle de décision** : la probabilité qu’un hôtel soit recommandé, avec son intervalle de confiance ; l’effet de sa position dans la liste soumise à l’assistant ; un simulateur de part de recommandations, que le jury peut manipuler.
4.  **Le protocole proposé** : le test A/B qui trancherait la question chez le client (métrique, tirage au sort, taille d’échantillon, durée, règle de décision).

### Les données de départ

Des données que vous produirez vous-mêmes, par un audit. Au moins 200 requêtes demandent à un assistant IA, interrogé par programme, de choisir entre cinq hôtels fictifs aux caractéristiques fixées, présentés dans un ordre tiré au sort. L’assistant interrogé et la manière d’y accéder vous seront précisés au lancement des audits, le 23 octobre.

- Les réponses collectées sont les données du binôme ; les conditions d’utilisation du fournisseur de l’assistant s’appliquent.
- Les résultats portent sur le modèle interrogé par programme, qui peut différer de l’assistant grand public du même fournisseur : votre recommandation le dit.

### Les jalons

| Date | Étape |
|----|----|
| Jeu. 15/10 | Jalon 1 : benchmark initial, question omnibus, protocole pré-enregistré |
| Ven. 23/10 | Remise du jeu de répétition ; lancement de l’omnibus et de votre audit |
| Ven. 6/11 | Jalon 2 : analyses, simulateur, préparation de la soutenance |
| Mar. 10/11 | Remise de l’écrit (date à confirmer) |
| Jeu. 12/11 | Soutenances |

### Ce que vous proposerez au jalon 1

- **Votre question pour l’omnibus de l’agence.** L’omnibus est un questionnaire anonyme commun à toute l’agence, diffusé à partir du 23 octobre. Chaque mission y place une question en deux versions, attribuées au hasard aux répondants : la comparaison des deux versions doit éclairer la question du client.
- **Votre protocole**, pré-enregistré par un commit dans votre dépôt avant toute analyse. C’est lui que vous répéterez sur le jeu simulé, puis que vous proposerez au client.

## Recommandé par l’IA · Note de cadrage

*Quel hôtel l’IA recommande-t-elle ? Daté du vendredi 9 octobre 2026, mise à jour le 13 octobre.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-note-de-cadrage.pdf

De l’associé de l’agence à l’équipe chargée de la mission. La commande dit ce que veut le client ; cette note, ce que l’agence attend de vous et comment vous y prendre. Gardez les deux sous la main.

### 1. En un coup d’œil

- **Thème** : « Séjourner », hôtels et restaurants.
- **Mission** : Recommandé par l’IA, quel hôtel l’IA recommande-t-elle ?
- **Client** : la direction d’un hôtel (client fictif).
- **Sa question** : « Nos clients demandent de plus en plus conseil à des assistants IA. Qu’est-ce qui les pousse à recommander notre hôtel ? »
- **Votre objectif** : mesurer, par un audit, ce qui fait recommander un hôtel par un assistant IA, et en tirer pour le client une façon de présenter le sien.

### 2. Les enjeux

Le client le constate : avant de réserver, ses clients demandent conseil à des assistants IA. Pour un hôtel, c’est un canal nouveau, qu’il ne maîtrise pas : l’assistant choisit à la place du voyageur, et explique son choix. Comprendre ce qui fait recommander un hôtel devient donc une question commerciale. Le sujet est récent et les études encore rares : une mesure faite avec méthode a de la valeur pour le client.

### 3. Les mathématiques en jeu

| Notion du cours | Vue le | Dans la mission |
|----|----|----|
| Probabilités conditionnelles | 7/10, reprise le 9/10 | La probabilité d’être recommandé selon la place de l’hôtel dans la liste |
| Lois de Bernoulli et binomiale | 9/10, après-midi | Le nombre de recommandations d’un hôtel sur une série de requêtes |
| Loi normale ; intervalle de confiance à 95 %, test de deux proportions | 23/10 | La probabilité d’être recommandé et son intervalle ; l’écrit du volet 1 ; le protocole |
| De la donnée à la décision | Avant le 6/11 | La recommandation (polycopié, chapitre 6) |

### 4. Les données

Vous les produisez vous-mêmes, par l’audit que décrit la commande : au moins 200 requêtes, l’ordre des hôtels tiré au sort. L’assistant interrogé et la manière d’y accéder vous seront précisés le 23/10 ; les conditions d’utilisation de son fournisseur s’appliquent.

Ce que l’équipe produit elle-même : **le plan de l’audit** au jalon 1 (demande soumise, hôtels proposés, tirage de l’ordre, définition d’une recommandation, nombre de requêtes), puis les réponses à partir du 23/10 ; **sa question pour l’omnibus**, en deux versions. Le 23/10, vous recevez aussi votre jeu de données simulé, pour l’écrit du volet 1.

### 5. Des pistes de réflexion

Celles qu’un consultant se pose avant de chiffrer. À vous d’en trouver d’autres.

1.  Qu’appellerez-vous « recommander » : être cité en premier, seul, ou parmi d’autres ?
2.  Quelles caractéristiques d’un hôtel votre client peut-il réellement changer ?
3.  Comment formuler la demande pour qu’elle ressemble à celle d’un vrai voyageur ?
4.  Par rapport à quoi jugerez-vous qu’une part de recommandations est élevée ?
5.  Que fera la direction de votre résultat, et quel résultat la ferait changer de stratégie ?
6.  Qu’est-ce qui encadre l’interrogation d’un assistant par programme ?

### 6. Ce qu’on attend

#### Les livrables

- **Le protocole** : une page, pré-enregistrée dans `projet/protocole/`.
- **Le plan de l’audit**, et **la question pour l’omnibus** en deux versions, attribuées au hasard.
- **Le benchmark** : trois à cinq sources, citées.
- **Le simulateur** : un notebook dans `projet/simulateur/`, avec deux ou trois paramètres que le jury peut faire varier.
- **L’écrit du volet 1** : quatre à six pages, selon la grille commune de la commande.
- **La soutenance** : 10 minutes d’exposé, 8 de questions.

#### Trois niveaux

Ils reprennent ce que l’agence regarde : la justesse des calculs, la qualité de la recommandation, la clarté, l’honnêteté sur les limites et le simulateur.

**Le socle, ce qu’il faut pour valider.**

- Le protocole est pré-enregistré à temps et complet : métrique, tirage au sort, taille d’échantillon, durée, règle de décision.
- L’audit est mené et documenté : toutes ses réponses sont conservées.
- L’écrit suit la grille commune, et ses calculs sont justes.
- Le simulateur tourne ; la recommandation répond au client et dit d’où viennent les chiffres.

**Un très bon travail.**

- La probabilité d’être recommandé et l’effet de la place dans la liste sont estimés, chacun avec son intervalle de confiance.
- Chaque résultat est traduit pour le client : sur 100 voyageurs, combien se voient proposer son hôtel ?
- Le benchmark est confronté à vos propres mesures : ce qui concorde, ce qui diffère, et pourquoi.
- Chaque limite est nommée, avec ce qu’elle change à la recommandation.

**Un excellent travail.**

- La recommandation dit au client quoi changer dans sa présentation, avec le gain attendu, sa marge, et la condition qui la ferait réviser.
- En séance, le jury fait varier les paramètres sans aide et voit la décision changer.
- L’équipe va au-delà de la commande, et le justifie : une source de plus, ou la preuve qu’un résultat tient quand une hypothèse change.
- Une notion difficile devient claire pour un non-spécialiste, en une minute.

Une équipe de trois vise au moins un élément du niveau « excellent ».

### 7. L’organisation

**Des rôles suggérés** : données et simulateur ; benchmark et protocole ; rédaction et soutenance. Un rôle par membre dans une équipe de trois ; à deux, partagez le troisième. Chacun relit le travail des autres, et doit pouvoir répondre le 12/11 à une question sur n’importe quelle partie. **Chacun commite depuis son propre compte** : l’historique du dépôt montre qui a fait quoi.

| Date | Ce qui est attendu |
|----|----|
| Jeu. 15/10 | Jalon 1 : protocole, plan de l’audit, question d’omnibus, benchmark initial |
| Ven. 23/10 | Jeu simulé à analyser selon votre protocole ; audit et omnibus lancés |
| Ven. 6/11 | Jalon 2 : analyses, simulateur qui tourne, plan de la soutenance |
| Mar. 10/11 | Remise de l’écrit du volet 1 (date à confirmer) |
| Jeu. 12/11 | Soutenance devant un jury, auquel des professionnels pourront se joindre |

**La règle du jalon 1.** Le protocole doit être synchronisé, donc visible sur github.com, avant le jeudi 15/10 à 23 h 59. Il est commité avant toute analyse : aucun fichier de `projet/analyses/` ne le précède dans l’historique. Vérifiez sur github.com que votre commit y est arrivé.

**L’usage de l’IA.** Elle est permise pour comprendre et vérifier, pas pour produire les livrables à la place de l’équipe. L’écrit se termine par une courte déclaration d’usage (outils, et pour quoi faire). Chacun doit savoir expliquer tout ce que l’équipe rend. Kit tuteur et FAQ GitHub : <https://ad-c.github.io/mth101/>.

### 8. Pour démarrer ce week-end

1.  Lisez la commande et cette note ensemble, et notez vos questions au client.
2.  Rédigez la demande qu’un voyageur ferait à un assistant pour choisir un hôtel.
3.  Créez `projet/protocole/protocole.md` et rédigez-en une première version.

## Recommandé par l’IA · Kit, partie 1

*Préparer le jalon 1 : protocole, omnibus, benchmark, données. Daté du mardi 13 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-a2-recommandation-ia-kit-partie-1.pdf

Le kit donne les outils de la mission ; la commande et la note de cadrage restent les références. Cette première partie prépare le jalon 1 du jeudi 15/10. La seconde arrivera le 23/10, avec votre jeu de répétition et le lancement de l’audit et de l’omnibus.

### 1. Le modèle de protocole

Le protocole décrit le test que vous proposeriez au client : ce que vous mesurerez, et comment vous déciderez, écrit avant d’avoir vu un seul résultat. Copiez les huit titres ci-dessous dans `projet/protocole/protocole.md`, et remplissez chacun en quelques lignes : le tout tient sur une page.

1.  **La question de décision.** La décision que le client prendra selon votre résultat, en une phrase.
2.  **L’hypothèse.** Ce que vous pensez trouver, et pourquoi.
3.  **La métrique.** Une proportion, mesurée de la même façon dans les deux groupes, et sa définition exacte : ce qui compte, et à quel moment.
4.  **L’unité tirée au sort.** Ce qui reçoit l’une ou l’autre version, une personne ou une période par exemple, et la façon dont le hasard est tiré.
5.  **La taille d’échantillon visée.** Un ordre de grandeur suffit à ce stade : quelques dizaines, centaines ou milliers d’unités par groupe ? Le cours du 23/10 vous donnera de quoi la calculer.
6.  **La durée.** Combien de temps le test tournera chez le client, et pourquoi.
7.  **La règle de décision.** Quel résultat vous fera recommander quoi.
8.  **Les limites prévues.** Ce que votre test ne pourra pas dire.

**Pour votre mission.** Le protocole est le test que vous proposeriez au client ; l’audit, lui, produit vos propres données (section 2).

Toute modification ultérieure du protocole reste visible, et datée, dans l’historique du dépôt (FAQ, question 9).

### 2. Le plan de l’audit et l’omnibus

#### Le plan de l’audit

L’audit produit vos données : au moins 200 requêtes, qui demandent à un assistant IA de choisir entre cinq hôtels fictifs, présentés dans un ordre tiré au sort (commande). Son plan se commite au jalon 1, dans `projet/protocole/plan-audit.md`, en six rubriques :

1.  **La demande soumise.** Le texte exact, celui qu’un voyageur pourrait écrire, et ce qui y est fixé.
2.  **Les cinq hôtels.** Un nom fictif pour chacun, et les caractéristiques que l’assistant lira (prix, emplacement, avis des clients, services…), fixées d’avance.
3.  **Le tirage de l’ordre.** Comment l’ordre des hôtels est tiré au sort à chaque requête. Le script du tirage des missions, sur la page « Projet » du site, en donne un exemple.
4.  **Ce qui compte comme une recommandation.** Être cité en premier, seul, ou parmi d’autres : une définition, écrite avant la première requête.
5.  **Le nombre de requêtes.** Au moins 200, et leur répartition.
6.  **Ce que vous conservez.** Toutes les réponses, en entier, avec l’ordre présenté et la date de chaque requête.

L’assistant interrogé et la manière d’y accéder vous seront précisés le 23/10 : rédigez le plan sans attendre.

#### La question pour l’omnibus

Votre note de cadrage la demande aussi au jalon 1. L’omnibus est le questionnaire anonyme commun à toute l’agence, diffusé à partir du 23/10. Votre question y figure en deux versions : chaque répondant reçoit l’une ou l’autre, au hasard, et vous comparez les réponses d’une version à l’autre.

1.  **Deux versions, une seule différence.** Mêmes mots, même ordre, mêmes réponses possibles, sauf l’élément que vous testez.
2.  **Une formulation neutre.** Rien qui pousse vers une réponse : ni adjectif qui juge, ni « ne pensez-vous pas que… ».
3.  **Une réponse fermée.** Deux ou trois réponses fixées, par exemple « Oui » et « Non » : chacune se compte, et donne une proportion par version.
4.  **Une question courte, lisible par tous.** Lue en moins de vingt secondes, sans rien connaître du client ; rien qui permette d’identifier le répondant.

Au jalon 1, commitez dans `projet/protocole/omnibus.md` : les deux versions, mot pour mot ; les réponses possibles ; en une phrase, ce que leur comparaison apprendra au client. L’agence assemble les questions des quatre missions en un seul questionnaire, et peut vous demander de retoucher la vôtre.

**Pour votre mission.** La comparaison des deux versions doit éclairer la question du client, du côté des voyageurs.

### 3. Les premiers repères de benchmark

Des références sûres, pour commencer. Votre benchmark les complète par vos propres recherches : études publiées, pratiques documentées du secteur, données ouvertes. Pour chaque source, notez qui l’a écrite, quand, et sur quelles données ; citez-la en entier. Gardez-les dans un fichier du dépôt, par exemple `projet/benchmark.md`.

- R. Kohavi, D. Tang, Y. Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*, Cambridge University Press, 2020, doi:10.1017/9781108653985 (ouvrage payant). La référence des tests A/B, pour votre protocole : métrique, tirage au sort, taille d’échantillon, durée.
- Q. Ye, R. Law, B. Gu, « The impact of online user reviews on hotel room sales », *International Journal of Hospitality Management*, 28(1) (2009), 180–182, doi:10.1016/j.ijhm.2008.06.011 (article court, payant ; résumé en accès libre). Ce que pèsent les avis en ligne sur les réservations d’un hôtel, chez des voyageurs qui choisissent eux-mêmes.
- C. K. Anderson, « The Impact of Social Media on Lodging Performance », Cornell Center for Hospitality Research, novembre 2012, en accès libre : <https://hdl.handle.net/1813/71194>. La réputation en ligne d’un hôtel et ses performances.

### 4. Les données de départ

Rien à télécharger avant le 23/10 : vos données sont les réponses de l’audit, et celles de votre question d’omnibus, recueillies à partir de cette date. L’assistant interrogé et la manière d’y accéder vous seront précisés le 23/10 ; les conditions d’utilisation de son fournisseur s’appliqueront.

Les réponses collectées sont les données de l’équipe : conservez-les dans `projet/donnees/`, avec leur provenance dans le README du dossier.

**Avant le protocole, aucune analyse.** Rien n’entre dans `projet/analyses/` avant que le protocole soit commité et synchronisé (règle du jalon 1, note de cadrage, section 7).

<!-- partie: c1-temps-attente -->

# Mission « Le temps d’attente »

## Mission C1 · Le temps d’attente

*Combien de temps allez-vous attendre ? Daté du vendredi 9 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-commande.pdf

Thème C, « Une journée de loisirs » : grands sites de loisirs et de patrimoine. Commande transmise à l’agence par son associé.

### Le client

Un grand site de loisirs (client fictif). Ses visiteurs organisent leur journée d’après les temps d’attente affichés à l’entrée des attractions. Le site veut afficher un temps juste, et conseiller les jours où venir.

> « Quel temps d’attente afficher, et quel jour conseiller à nos visiteurs ? »

### Ce que l’agence doit livrer

**Un écrit : la répétition du protocole (volet 1).** Avant de mener une expérience chez un client, l’agence la répète sur des données simulées, pour vérifier sa chaîne d’analyse et la taille d’échantillon nécessaire. Le 23 octobre, votre binôme reçoit son propre jeu de données simulé. Vous y menez l’analyse prévue par votre protocole : estimation, intervalle de confiance à 95 %, test de comparaison de deux proportions, conclusion. Quatre à six pages, selon la grille commune de l’agence : question, données, effet estimé, intervalle de confiance, test, importance pratique, limites, recommandation, condition de réexamen.

**Une proposition d’action, en soutenance le 12 novembre** (10 minutes d’exposé, 8 de questions) :

1.  **La problématique** du client, formulée dans ses mots.
2.  **Le benchmark** : études publiées, pratiques documentées du secteur, données ouvertes analysées par vous.
3.  **Le modèle de décision** : la distribution des attentes par jour et par heure, la probabilité d’attendre plus de 60 minutes, et un simulateur de file d’attente qui montre comment l’attente évolue quand l’affluence augmente ; le jury peut le manipuler.
4.  **Le protocole proposé** : le test A/B qui trancherait la question chez le client (métrique, tirage au sort, taille d’échantillon, durée, règle de décision).

### Les données de départ

Des relevés réels des temps d’attente affichés dans deux parcs : Disneyland Park et Disney Adventure World, à Disneyland Paris. L’agence les collecte par l’API publique de Queue-Times, toutes les 15 minutes de 8 h à minuit, depuis le 5 octobre et jusqu’au 12 novembre 2026. Les parcs ne sont pas le client : leurs données servent de cas réel comparable, et ils ne sont associés ni au cours ni à la mission.

- Un fichier CSV par jour, une ligne par attraction et par relevé, dans le dépôt public du cours : github.com/Ad-C/mth101, dossier `donnees/queue-times`.
- Le README de ce dossier décrit les colonnes, et les trous et retards connus de la série.

**Powered by [Queue-Times.com](https://queue-times.com/).** L’API est gratuite, à condition d’afficher cette mention, avec un lien vers queue-times.com : tout rendu qui utilise ces données la porte (notebook, graphique, simulateur, poster, diapositive).

### Les jalons

| Date | Étape |
|----|----|
| Jeu. 15/10 | Jalon 1 : benchmark initial, question omnibus, protocole pré-enregistré |
| Ven. 23/10 | Remise du jeu de répétition ; lancement de l’omnibus |
| Ven. 6/11 | Jalon 2 : analyses, simulateur, préparation de la soutenance |
| Mar. 10/11 | Remise de l’écrit (date à confirmer) |
| Jeu. 12/11 | Soutenances |

### Ce que vous proposerez au jalon 1

- **Votre question pour l’omnibus de l’agence.** L’omnibus est un questionnaire anonyme commun à toute l’agence, diffusé à partir du 23 octobre. Chaque mission y place une question en deux versions, attribuées au hasard aux répondants : la comparaison des deux versions doit éclairer la question du client.
- **Votre protocole**, pré-enregistré par un commit dans votre dépôt avant toute analyse. C’est lui que vous répéterez sur le jeu simulé, puis que vous proposerez au client.

## Le temps d’attente · Note de cadrage

*Combien de temps allez-vous attendre ? Daté du vendredi 9 octobre 2026, mise à jour le 13 octobre.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-note-de-cadrage.pdf

De l’associé de l’agence à l’équipe chargée de la mission. La commande dit ce que veut le client ; cette note, ce que l’agence attend de vous et comment vous y prendre. Gardez les deux sous la main.

### 1. En un coup d’œil

- **Thème** : « Une journée de loisirs », grands sites de loisirs et de patrimoine.
- **Mission** : Le temps d’attente, combien de temps allez-vous attendre ?
- **Client** : un grand site de loisirs (client fictif).
- **Sa question** : « Quel temps d’attente afficher, et quel jour conseiller à nos visiteurs ? »
- **Votre objectif** : dire au client, chiffres à l’appui, quel temps afficher et quels jours conseiller, à partir des relevés réels de l’agence, d’un simulateur et d’un protocole de test.

### 2. Les enjeux

Dans un grand site de loisirs, une bonne part de la journée se passe dans les files. Le temps affiché à l’entrée d’une attraction guide les choix des visiteurs, et le jour choisi pour venir décide de toute leur journée. Les grands parcs affichent déjà les attentes en direct, aux attractions et dans leurs applications : la question n’est plus de savoir s’il faut afficher, mais quoi, et comment conseiller.

### 3. Les mathématiques en jeu

| Notion du cours | Vue le | Dans la mission |
|----|----|----|
| Probabilités conditionnelles | 7/10, reprise le 9/10 | L’attente selon le jour et l’heure |
| Espérance, variance, écart-type | 9/10, après-midi | Le niveau et la dispersion des attentes |
| Loi normale, théorème central limite | 23/10, matin | La précision d’une estimation tirée de nombreux relevés |
| Estimation, intervalle de confiance à 95 %, test de deux proportions | 23/10, après-midi | La probabilité d’attendre plus de 60 minutes, avec son intervalle ; l’écrit du volet 1 ; le protocole |
| De la donnée à la décision | Avant le 6/11 | La recommandation (polycopié, chapitre 6) |

### 4. Les données

Les relevés réels de l’agence, décrits dans la commande : un fichier CSV par jour, dans le dépôt public du cours (github.com/Ad-C/mth101, dossier `donnees/queue-times`), dont le README décrit les colonnes. La collecte continue jusqu’au 12/11. **Powered by [Queue-Times.com](https://queue-times.com/)** : tout rendu qui utilise ces données porte cette mention, avec un lien.

Ce que l’équipe produit elle-même : **sa question pour l’omnibus de l’agence**, en deux versions attribuées au hasard, proposée au jalon 1 ; les réponses arrivent à partir du 23/10. Le même jour, vous recevez votre propre jeu de données simulé, pour l’écrit du volet 1.

### 5. Des pistes de réflexion

Celles qu’un consultant se pose avant de chiffrer. À vous d’en trouver d’autres.

1.  À quoi sert le temps affiché, pour le visiteur et pour le site ?
2.  Qu’est-ce qu’un « bon jour » pour un visiteur, et comment le mesureriez-vous ?
3.  Comment les grands sites communiquent-ils aujourd’hui sur l’attente ?
4.  Que pourraient vous apprendre les répondants de l’omnibus que les relevés ne disent pas ?
5.  Dans votre test chez le client, que comparerez-vous, sur quelles attractions, pendant combien de temps, et quel résultat vous fera conclure ?
6.  Comment un jury non spécialiste comprendra-t-il en une minute ce que montre votre simulateur ?

### 6. Ce qu’on attend

#### Les livrables

- **Le protocole** : une page, pré-enregistrée dans `projet/protocole/`.
- **La question pour l’omnibus** : deux versions, attribuées au hasard.
- **Le benchmark** : trois à cinq sources, citées.
- **Le simulateur** : un notebook dans `projet/simulateur/`, avec deux ou trois paramètres que le jury peut faire varier.
- **L’écrit du volet 1** : quatre à six pages, selon la grille commune de la commande.
- **La soutenance** : 10 minutes d’exposé, 8 de questions.

#### Trois niveaux

Ils reprennent ce que l’agence regarde : la justesse des calculs, la qualité de la recommandation, la clarté, l’honnêteté sur les limites et le simulateur.

**Le socle, ce qu’il faut pour valider.**

- Le protocole est pré-enregistré à temps et complet : métrique, tirage au sort, taille d’échantillon, durée, règle de décision.
- L’écrit suit la grille commune, et ses calculs sont justes.
- Le simulateur tourne : le jury y choisit l’affluence et voit l’attente qui en résulte.
- La recommandation répond aux deux questions du client, avec la mention de Queue-Times.

**Un très bon travail.**

- La probabilité d’attendre plus de 60 minutes est estimée pour plusieurs jours et heures, chaque fois avec son intervalle de confiance.
- Chaque résultat est traduit pour le visiteur : à quelle heure arriver, combien de temps prévoir.
- Le benchmark est confronté à vos propres chiffres : ce qui concorde, ce qui diffère, et pourquoi.
- Chaque limite est nommée, avec ce qu’elle change à la recommandation.

**Un excellent travail.**

- Le conseil au visiteur tient en une phrase que le site pourrait afficher, avec la condition qui le ferait réviser.
- En séance, le jury fait varier les paramètres sans aide et voit la décision changer.
- L’équipe va au-delà de la commande, et le justifie : une source de plus, ou la preuve qu’un résultat tient quand une hypothèse change.
- Une notion difficile devient claire pour un non-spécialiste, en une minute.

Une équipe de trois vise au moins un élément du niveau « excellent ».

### 7. L’organisation

**Des rôles suggérés** : données et simulateur ; benchmark et protocole ; rédaction et soutenance. Un rôle par membre dans une équipe de trois ; à deux, partagez le troisième. Chacun relit le travail des autres, et doit pouvoir répondre le 12/11 à une question sur n’importe quelle partie. **Chacun commite depuis son propre compte** : l’historique du dépôt montre qui a fait quoi.

| Date | Ce qui est attendu |
|----|----|
| Jeu. 15/10 | Jalon 1 : protocole, question d’omnibus, benchmark initial |
| Ven. 23/10 | Jeu simulé à analyser selon votre protocole ; omnibus lancé |
| Ven. 6/11 | Jalon 2 : analyses, simulateur qui tourne, plan de la soutenance |
| Mar. 10/11 | Remise de l’écrit du volet 1 (date à confirmer) |
| Jeu. 12/11 | Soutenance devant un jury, auquel des professionnels pourront se joindre |

**La règle du jalon 1.** Le protocole doit être synchronisé, donc visible sur github.com, avant le jeudi 15/10 à 23 h 59. Il est commité avant toute analyse : aucun fichier de `projet/analyses/` ne le précède dans l’historique. Vérifiez sur github.com que votre commit y est arrivé.

**L’usage de l’IA.** Elle est permise pour comprendre et vérifier, pas pour produire les livrables à la place de l’équipe. L’écrit se termine par une courte déclaration d’usage (outils, et pour quoi faire). Chacun doit savoir expliquer tout ce que l’équipe rend. Kit tuteur et FAQ GitHub : <https://ad-c.github.io/mth101/>.

### 8. Pour démarrer ce week-end

1.  Lisez la commande et cette note ensemble, et notez vos questions au client.
2.  Lisez le README des relevés, dans le dépôt public du cours.
3.  Créez `projet/protocole/protocole.md` et rédigez-en une première version.

## Le temps d’attente · Kit, partie 1

*Préparer le jalon 1 : protocole, omnibus, benchmark, données. Daté du mardi 13 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-c1-temps-attente-kit-partie-1.pdf

Le kit donne les outils de la mission ; la commande et la note de cadrage restent les références. Cette première partie prépare le jalon 1 du jeudi 15/10. La seconde arrivera le 23/10, avec votre jeu de répétition et le lancement de l’omnibus.

### 1. Le modèle de protocole

Le protocole décrit le test que vous proposeriez au client : ce que vous mesurerez, et comment vous déciderez, écrit avant d’avoir vu un seul résultat. Copiez les huit titres ci-dessous dans `projet/protocole/protocole.md`, et remplissez chacun en quelques lignes : le tout tient sur une page.

1.  **La question de décision.** La décision que le client prendra selon votre résultat, en une phrase.
2.  **L’hypothèse.** Ce que vous pensez trouver, et pourquoi.
3.  **La métrique.** Une proportion, mesurée de la même façon dans les deux groupes, et sa définition exacte : ce qui compte, et à quel moment.
4.  **L’unité tirée au sort.** Ce qui reçoit l’une ou l’autre version, une personne ou une période par exemple, et la façon dont le hasard est tiré.
5.  **La taille d’échantillon visée.** Un ordre de grandeur suffit à ce stade : quelques dizaines, centaines ou milliers d’unités par groupe ? Le cours du 23/10 vous donnera de quoi la calculer.
6.  **La durée.** Combien de temps le test tournera chez le client, et pourquoi.
7.  **La règle de décision.** Quel résultat vous fera recommander quoi.
8.  **Les limites prévues.** Ce que votre test ne pourra pas dire.

**Pour votre mission.** La commande pose deux questions, le temps à afficher et le jour à conseiller : dites laquelle votre test tranche.

Toute modification ultérieure du protocole reste visible, et datée, dans l’historique du dépôt (FAQ, question 9).

### 2. La question pour l’omnibus

L’omnibus est le questionnaire anonyme commun à toute l’agence, diffusé à partir du 23/10. Votre question y figure en deux versions : chaque répondant reçoit l’une ou l’autre, au hasard, et vous comparez les réponses d’une version à l’autre.

1.  **Deux versions, une seule différence.** Mêmes mots, même ordre, mêmes réponses possibles, sauf l’élément que vous testez.
2.  **Une formulation neutre.** Rien qui pousse vers une réponse : ni adjectif qui juge, ni « ne pensez-vous pas que… ».
3.  **Une réponse fermée.** Deux ou trois réponses fixées, par exemple « Oui » et « Non » : chacune se compte, et donne une proportion par version.
4.  **Une question courte, lisible par tous.** Lue en moins de vingt secondes, sans rien connaître du client ; rien qui permette d’identifier le répondant.

Au jalon 1, commitez dans `projet/protocole/omnibus.md` : les deux versions, mot pour mot ; les réponses possibles ; en une phrase, ce que leur comparaison apprendra au client. L’agence assemble les questions des quatre missions en un seul questionnaire, et peut vous demander de retoucher la vôtre.

**Pour votre mission.** La comparaison des deux versions doit éclairer l’une des deux questions du client. Choisissez une situation de visite que chacun peut imaginer.

### 3. Les premiers repères de benchmark

Des références sûres, pour commencer. Votre benchmark les complète par vos propres recherches : études publiées, pratiques documentées du secteur, données ouvertes. Pour chaque source, notez qui l’a écrite, quand, et sur quelles données ; citez-la en entier. Gardez-les dans un fichier du dépôt, par exemple `projet/benchmark.md`.

- Queue-Times, « Theme Park Wait Times API », <https://queue-times.com/pages/api>. D’où viennent les relevés de l’agence, à quelle fréquence ils sont mis à jour, et la mention qu’ils imposent.
- TEA et AECOM, *2023 Theme Index and Museum Index: The Global Attractions Attendance Report*, 2024, en accès libre : <https://aecom.com/wp-content/uploads/documents/reports/AECOM-Theme-Index-2023.pdf>. La fréquentation des grands parcs du monde et d’Europe : l’ordre de grandeur des foules qu’accueille votre client.
- R. Kohavi, D. Tang, Y. Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*, Cambridge University Press, 2020, doi:10.1017/9781108653985 (ouvrage payant). La référence des tests A/B, pour votre protocole : métrique, tirage au sort, taille d’échantillon, durée.

### 4. Les données de départ

**Où.** Dans le dépôt public du cours, dossier `donnees/queue-times` : <https://github.com/Ad-C/mth101/tree/main/donnees/queue-times>. Un fichier CSV par jour, `AAAA-MM-JJ.csv`, une ligne par attraction et par relevé ; un relevé toutes les 15 minutes, de 8 h à minuit, jusqu’au 12/11. Lisez d’abord le README du dossier : les colonnes, et la façon dont les relevés sont faits.

**Comment les ouvrir.** Rien à télécharger : pandas lit un fichier par son adresse, comme le montre le README. Pour plusieurs jours, après le jalon, dans un notebook de `projet/analyses/` :

``` python
import pandas as pd

base = ("https://raw.githubusercontent.com/"
        "Ad-C/mth101/main/donnees/queue-times/")
jours = pd.date_range("2026-10-05", "2026-10-14").strftime("%Y-%m-%d")
releves = pd.concat(pd.read_csv(base + j + ".csv") for j in jours)
```

Le fichier du jour se complète jusqu’à minuit : relancez la lecture pour avoir les derniers relevés.

**Sous quelle licence.** Les conditions de Queue-Times : la mention « Powered by Queue-Times.com », avec un lien vers <https://queue-times.com/>, figure dans tout rendu qui utilise ces données (notebook, graphique, simulateur, diapositive).

Votre question d’omnibus vous apportera d’autres réponses, après la collecte qui commence le 23/10.

**Avant le protocole, aucune analyse.** Rien n’entre dans `projet/analyses/` avant que le protocole soit commité et synchronisé (règle du jalon 1, note de cadrage, section 7).

<!-- partie: c2-robots-de-service -->

# Mission « Les robots de service »

## Mission C2 · Les robots de service

*Robots et IA au service des visiteurs. Daté du vendredi 9 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-commande.pdf

Thème C, « Une journée de loisirs » : grands sites de loisirs et de patrimoine. Commande transmise à l’agence par son associé.

### Le client

La direction de la restauration d’un grand site de loisirs (client fictif). Elle envisage d’installer un robot de service dans ses points de restauration. Avant d’investir, elle veut savoir comment ses visiteurs le percevraient, et comment le leur présenter.

> « Un robot de service dans nos points de restauration : gadget, économie ou aide au personnel ? Et comment l’annoncer à nos visiteurs ? »

### Ce que l’agence doit livrer

**Un écrit : la répétition du protocole (volet 1).** Avant de mener une expérience chez un client, l’agence la répète sur des données simulées, pour vérifier sa chaîne d’analyse et la taille d’échantillon nécessaire. Le 23 octobre, votre binôme reçoit son propre jeu de données simulé. Vous y menez l’analyse prévue par votre protocole : estimation, intervalle de confiance à 95 %, test de comparaison de deux proportions, conclusion. Quatre à six pages, selon la grille commune de l’agence : question, données, effet estimé, intervalle de confiance, test, importance pratique, limites, recommandation, condition de réexamen.

**Une proposition d’action, en soutenance le 12 novembre** (10 minutes d’exposé, 8 de questions) :

1.  **La problématique** du client, formulée dans ses mots.
2.  **Le benchmark** : études publiées, pratiques documentées du secteur, données ouvertes analysées par vous.
3.  **Le modèle de décision** : un simulateur de la décision de déploiement, qui croise les coûts et le taux d’acceptation des visiteurs, avec son intervalle de confiance ; le jury peut le manipuler.
4.  **Le protocole proposé** : le test A/B qui trancherait la question chez le client (métrique, tirage au sort, taille d’échantillon, durée, règle de décision).

### Les données de départ

**L’omnibus de l’agence est le cœur de la mission.** Votre question y recueille les avis des répondants, en deux versions tirées au sort, à partir du 23 octobre. Le questionnaire est anonyme : aucune donnée qui permette d’identifier un répondant.

**Les études publiées sur l’acceptation des robots de service**, à commencer par le modèle de Wirtz et al. : « Brave new world: service robots in the frontline », *Journal of Service Management*, 29(5) (2018), 907–931, doi:10.1108/JOSM-04-2018-0119. Les coûts d’un robot se documentent dans le benchmark, sources citées.

### Les jalons

| Date | Étape |
|----|----|
| Jeu. 15/10 | Jalon 1 : benchmark initial, question omnibus, protocole pré-enregistré |
| Ven. 23/10 | Remise du jeu de répétition ; lancement de l’omnibus |
| Ven. 6/11 | Jalon 2 : analyses, simulateur, préparation de la soutenance |
| Mar. 10/11 | Remise de l’écrit (date à confirmer) |
| Jeu. 12/11 | Soutenances |

### Ce que vous proposerez au jalon 1

- **Votre question pour l’omnibus de l’agence.** L’omnibus est un questionnaire anonyme commun à toute l’agence, diffusé à partir du 23 octobre. Chaque mission y place une question en deux versions, attribuées au hasard aux répondants : la comparaison des deux versions doit éclairer la question du client.
- **Votre protocole**, pré-enregistré par un commit dans votre dépôt avant toute analyse. C’est lui que vous répéterez sur le jeu simulé, puis que vous proposerez au client.

## Les robots de service · Note de cadrage

*Robots et IA au service des visiteurs. Daté du vendredi 9 octobre 2026, mise à jour le 13 octobre.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-note-de-cadrage.pdf

De l’associé de l’agence à l’équipe chargée de la mission. La commande dit ce que veut le client ; cette note, ce que l’agence attend de vous et comment vous y prendre. Gardez les deux sous la main.

### 1. En un coup d’œil

- **Thème** : « Une journée de loisirs », grands sites de loisirs et de patrimoine.
- **Mission** : Les robots de service, robots et IA au service des visiteurs.
- **Client** : la direction de la restauration d’un grand site de loisirs (client fictif).
- **Sa question** : « Un robot de service dans nos points de restauration : gadget, économie ou aide au personnel ? Et comment l’annoncer à nos visiteurs ? »
- **Votre objectif** : éclairer la décision de déploiement et la façon de l’annoncer, par l’omnibus, un benchmark et un simulateur de décision.

### 2. Les enjeux

Des robots de service circulent déjà dans des restaurants et des hôtels. Pour la restauration d’un grand site de loisirs, qui sert beaucoup de repas en peu de temps, l’idée est tentante. Elle coûte cher, et l’accueil que lui feront les visiteurs n’est pas acquis. Avant d’investir, la direction veut décider sur des faits, et savoir comment présenter le robot si elle l’adopte.

### 3. Les mathématiques en jeu

| Notion du cours | Vue le | Dans la mission |
|----|----|----|
| Probabilités conditionnelles | 7/10, reprise le 9/10 | La proportion de réponses positives, selon la version de la question reçue |
| Loi de Bernoulli | 9/10, après-midi | Chaque réponse à votre question, positive ou non |
| Espérance | 9/10, après-midi | Le gain attendu d’un déploiement |
| Loi normale ; intervalle de confiance à 95 %, test de deux proportions | 23/10 | Le taux d’acceptation et son intervalle ; la comparaison des deux versions ; l’écrit du volet 1 ; le protocole |
| De la donnée à la décision | Avant le 6/11 | La recommandation (polycopié, chapitre 6) |

### 4. Les données

L’omnibus de l’agence est le cœur de la mission, comme le dit la commande : votre question y est posée en deux versions, attribuées au hasard, à partir du 23/10. Le reste vient du benchmark : les études publiées sur l’acceptation des robots de service, à commencer par le modèle de Wirtz et al. cité dans la commande, et les coûts d’un robot, sources citées.

Ce que l’équipe produit elle-même : **sa question pour l’omnibus**, en deux versions, proposée au jalon 1 : c’est votre principale source de données. Le 23/10, vous recevez aussi votre propre jeu de données simulé, pour l’écrit du volet 1.

### 5. Des pistes de réflexion

Celles qu’un consultant se pose avant de chiffrer. À vous d’en trouver d’autres.

1.  Que fait concrètement un robot de service dans un point de restauration, et que ne sait-il pas faire ?
2.  Combien coûte un robot, à l’achat ou à la location, et que doit-il rapporter ou faire économiser pour valoir la dépense ?
3.  Où trouve-t-on déjà des robots de service, et que disent les études publiées sur leur acceptation ?
4.  Parmi les raisons d’accepter un robot que distingue le modèle de Wirtz et al., lesquelles comptent dans un restaurant de site de loisirs ?
5.  Qu’est-ce qui pourrait faire changer d’avis la direction, dans un sens ou dans l’autre ?
6.  Dans votre test chez le client, que comparerez-vous, où, pendant combien de temps, et quel résultat vous fera conclure ?

### 6. Ce qu’on attend

#### Les livrables

- **Le protocole** : une page, pré-enregistrée dans `projet/protocole/`.
- **La question pour l’omnibus** : deux versions, attribuées au hasard.
- **Le benchmark** : trois à cinq sources, citées.
- **Le simulateur** : un notebook dans `projet/simulateur/`, avec deux ou trois paramètres que le jury peut faire varier.
- **L’écrit du volet 1** : quatre à six pages, selon la grille commune de la commande.
- **La soutenance** : 10 minutes d’exposé, 8 de questions.

#### Trois niveaux

Ils reprennent ce que l’agence regarde : la justesse des calculs, la qualité de la recommandation, la clarté, l’honnêteté sur les limites et le simulateur.

**Le socle, ce qu’il faut pour valider.**

- Le protocole est pré-enregistré à temps et complet : métrique, tirage au sort, taille d’échantillon, durée, règle de décision.
- L’écrit suit la grille commune, et ses calculs sont justes.
- Le simulateur tourne : il croise un coût et un taux d’acceptation, et dit si le déploiement vaut la dépense.
- La recommandation répond aux deux questions du client, et dit d’où viennent les chiffres.

**Un très bon travail.**

- Le taux d’acceptation du simulateur est une estimation sourcée, avec son intervalle de confiance, et non un chiffre posé à la main.
- Les coûts viennent de sources citées, et leur incertitude est dite.
- Le benchmark est confronté à vos propres chiffres : ce qui concorde, ce qui diffère, et pourquoi.
- Chaque limite est nommée, avec ce qu’elle change à la recommandation.

**Un excellent travail.**

- Le simulateur montre à partir de quel taux d’acceptation le robot vaut la dépense ; la recommandation dit la condition qui la ferait réviser.
- En séance, le jury fait varier les paramètres sans aide et voit la décision changer.
- L’équipe va au-delà de la commande, et le justifie : une source de plus, ou la preuve qu’un résultat tient quand une hypothèse change.
- Une notion difficile devient claire pour un non-spécialiste, en une minute.

Une équipe de trois vise au moins un élément du niveau « excellent ».

### 7. L’organisation

**Des rôles suggérés** : données et simulateur ; benchmark et protocole ; rédaction et soutenance. Un rôle par membre dans une équipe de trois ; à deux, partagez le troisième. Chacun relit le travail des autres, et doit pouvoir répondre le 12/11 à une question sur n’importe quelle partie. **Chacun commite depuis son propre compte** : l’historique du dépôt montre qui a fait quoi.

| Date | Ce qui est attendu |
|----|----|
| Jeu. 15/10 | Jalon 1 : protocole, question d’omnibus, benchmark initial |
| Ven. 23/10 | Jeu simulé à analyser selon votre protocole ; omnibus lancé |
| Ven. 6/11 | Jalon 2 : analyses, simulateur qui tourne, plan de la soutenance |
| Mar. 10/11 | Remise de l’écrit du volet 1 (date à confirmer) |
| Jeu. 12/11 | Soutenance devant un jury, auquel des professionnels pourront se joindre |

**La règle du jalon 1.** Le protocole doit être synchronisé, donc visible sur github.com, avant le jeudi 15/10 à 23 h 59. Il est commité avant toute analyse : aucun fichier de `projet/analyses/` ne le précède dans l’historique. Vérifiez sur github.com que votre commit y est arrivé.

**L’usage de l’IA.** Elle est permise pour comprendre et vérifier, pas pour produire les livrables à la place de l’équipe. L’écrit se termine par une courte déclaration d’usage (outils, et pour quoi faire). Chacun doit savoir expliquer tout ce que l’équipe rend. Kit tuteur et FAQ GitHub : <https://ad-c.github.io/mth101/>.

### 8. Pour démarrer ce week-end

1.  Lisez la commande et cette note ensemble, et notez vos questions au client.
2.  Trouvez l’article de Wirtz et al. cité dans la commande, et repérez ce que son modèle d’acceptation distingue.
3.  Créez `projet/protocole/protocole.md` et rédigez-en une première version.

## Les robots de service · Kit, partie 1

*Préparer le jalon 1 : protocole, omnibus, benchmark, données. Daté du mardi 13 octobre 2026.* PDF : https://ad-c.github.io/mth101/supports/projet/mth101-c2-robots-de-service-kit-partie-1.pdf

Le kit donne les outils de la mission ; la commande et la note de cadrage restent les références. Cette première partie prépare le jalon 1 du jeudi 15/10. La seconde arrivera le 23/10, avec votre jeu de répétition et le lancement de l’omnibus.

### 1. Le modèle de protocole

Le protocole décrit le test que vous proposeriez au client : ce que vous mesurerez, et comment vous déciderez, écrit avant d’avoir vu un seul résultat. Copiez les huit titres ci-dessous dans `projet/protocole/protocole.md`, et remplissez chacun en quelques lignes : le tout tient sur une page.

1.  **La question de décision.** La décision que le client prendra selon votre résultat, en une phrase.
2.  **L’hypothèse.** Ce que vous pensez trouver, et pourquoi.
3.  **La métrique.** Une proportion, mesurée de la même façon dans les deux groupes, et sa définition exacte : ce qui compte, et à quel moment.
4.  **L’unité tirée au sort.** Ce qui reçoit l’une ou l’autre version, une personne ou une période par exemple, et la façon dont le hasard est tiré.
5.  **La taille d’échantillon visée.** Un ordre de grandeur suffit à ce stade : quelques dizaines, centaines ou milliers d’unités par groupe ? Le cours du 23/10 vous donnera de quoi la calculer.
6.  **La durée.** Combien de temps le test tournera chez le client, et pourquoi.
7.  **La règle de décision.** Quel résultat vous fera recommander quoi.
8.  **Les limites prévues.** Ce que votre test ne pourra pas dire.

**Pour votre mission.** La commande pose deux questions, l’intérêt d’un robot et la façon de l’annoncer : dites laquelle votre test tranche.

Toute modification ultérieure du protocole reste visible, et datée, dans l’historique du dépôt (FAQ, question 9).

### 2. La question pour l’omnibus

L’omnibus est le questionnaire anonyme commun à toute l’agence, diffusé à partir du 23/10. Votre question y figure en deux versions : chaque répondant reçoit l’une ou l’autre, au hasard, et vous comparez les réponses d’une version à l’autre.

1.  **Deux versions, une seule différence.** Mêmes mots, même ordre, mêmes réponses possibles, sauf l’élément que vous testez.
2.  **Une formulation neutre.** Rien qui pousse vers une réponse : ni adjectif qui juge, ni « ne pensez-vous pas que… ».
3.  **Une réponse fermée.** Deux ou trois réponses fixées, par exemple « Oui » et « Non » : chacune se compte, et donne une proportion par version.
4.  **Une question courte, lisible par tous.** Lue en moins de vingt secondes, sans rien connaître du client ; rien qui permette d’identifier le répondant.

Au jalon 1, commitez dans `projet/protocole/omnibus.md` : les deux versions, mot pour mot ; les réponses possibles ; en une phrase, ce que leur comparaison apprendra au client. L’agence assemble les questions des quatre missions en un seul questionnaire, et peut vous demander de retoucher la vôtre.

**Pour votre mission.** L’omnibus est votre principale source de données (commande) : soignez cette question plus que tout le reste. La comparaison des deux versions doit éclairer l’une des deux questions du client.

### 3. Les premiers repères de benchmark

Des références sûres, pour commencer. Votre benchmark les complète par vos propres recherches : études publiées, pratiques documentées du secteur, données ouvertes. Pour chaque source, notez qui l’a écrite, quand, et sur quelles données ; citez-la en entier. Gardez-les dans un fichier du dépôt, par exemple `projet/benchmark.md`.

- J. Wirtz et al., « Brave new world: service robots in the frontline », *Journal of Service Management*, 29(5) (2018), 907–931, doi:10.1108/JOSM-04-2018-0119, en accès libre (CC BY 4.0). Le modèle d’acceptation des robots de service, cité par la commande.
- Fédération internationale de robotique (IFR), « Global Sales of Professional Service Robots Surge 24% », communiqué du 30 septembre 2026, <https://ifr.org/ifr-press-releases/news/global-sales-of-professional-service-robots-surge-24-percent>. Le marché mondial des robots de service professionnels, dont ceux de l’hôtellerie, selon la fédération des fabricants : des chiffres de la profession, à citer comme tels.
- L. Lu, R. Cai, D. Gursoy, « Developing and validating a service robot integration willingness scale », *International Journal of Hospitality Management*, 80 (2019), 36–51, doi:10.1016/j.ijhm.2019.01.005 (payant ; résumé en accès libre). Comment des chercheurs mesurent, en hôtellerie et en restauration, la disposition des clients à accueillir un robot.

### 4. Les données de départ

**Les réponses à votre question d’omnibus**, recueillies à partir du 23/10 : votre principale source. Le questionnaire est anonyme ; les réponses vous seront transmises après la collecte : rangez-les dans `projet/donnees/`.

**Les études publiées sur l’acceptation des robots de service**, à commencer par Wirtz et al. (section 3), sous licence CC BY 4.0 ; chaque étude se cite en entier, avec son DOI. Les coûts d’un robot se documentent dans le benchmark, sources citées.

**Avant le protocole, aucune analyse.** Rien n’entre dans `projet/analyses/` avant que le protocole soit commité et synchronisé (règle du jalon 1, note de cadrage, section 7).
