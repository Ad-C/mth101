---
title: Projet
---

[Accueil](./) · [Séances](seances.html) · **Projet** · [Kit tuteur](kit-tuteur.html) · [FAQ GitHub](faq.html) · [Dépôt GitHub](https://github.com/Ad-C/mth101)

Les quatre missions de l'agence, tirées au sort le 9 octobre. Pour chacune : la commande du client, la note de cadrage et le kit de mission. Les missions tirées sont définitives.

## Jeudi 15 octobre : jalon 1

Une demi-journée en autonomie : un temps de cours, puis le jalon 1 de votre mission.

- [Feuille de route de la demi-journée (PDF)](supports/projet/mth101-feuille-de-route-jalon-1.pdf)
- [Parcours en autonomie : les lois discrètes (PDF)](supports/seance-04/mth101-seance-04-parcours-lois-discretes.pdf), les 60 premières minutes
- [Kit tuteur](kit-tuteur.html) : la consigne pour vous servir d'un assistant IA comme d'un tuteur, et la règle d'usage de l'IA.
- [Carte du module (PDF)](supports/polycopie/mth101-carte-du-module.pdf), à joindre au kit tuteur avec votre commande et votre note de cadrage.
- [Chapitre 1 du polycopié : probabilités et probabilités conditionnelles (PDF)](supports/polycopie/mth101-chapitre-01-probabilites-conditionnelles.pdf) et [ses corrigés (PDF)](supports/polycopie/mth101-chapitre-01-corriges.pdf), avec son annexe, [la boîte à outils (PDF)](supports/polycopie/mth101-boite-a-outils.pdf) : les bases de calcul du polycopié ; les réponses de ses questions éclair sont dans les corrigés du chapitre 1.
- [Chapitre 2 du polycopié : le théorème de Bayes (PDF)](supports/polycopie/mth101-chapitre-02-theoreme-de-bayes.pdf) et [ses corrigés (PDF)](supports/polycopie/mth101-chapitre-02-corriges.pdf), à travailler en autonomie d'ici le vendredi 23 octobre.
- [Chapitre 3 du polycopié : lois discrètes ; espérance, variance, écart-type (PDF)](supports/polycopie/mth101-chapitre-03-lois-discretes.pdf) et [ses corrigés (PDF)](supports/polycopie/mth101-chapitre-03-corriges.pdf), qui reprend le parcours du jeudi 15 octobre et va plus loin.
- [Chapitre 4 du polycopié : loi normale et théorème central limite (PDF)](supports/polycopie/mth101-chapitre-04-loi-normale.pdf) et [ses corrigés (PDF)](supports/polycopie/mth101-chapitre-04-corriges.pdf), pour la séance du vendredi 23 octobre au matin.
- [Chapitre 5 du polycopié : estimation, intervalle de confiance, test de deux proportions (PDF)](supports/polycopie/mth101-chapitre-05-estimation-tests.pdf) et [ses corrigés (PDF)](supports/polycopie/mth101-chapitre-05-corriges.pdf), pour la séance du vendredi 23 octobre après-midi.

**La règle du jalon 1.** Le protocole doit être synchronisé, donc visible sur github.com, avant le jeudi 15 octobre à 23 h 59. Il est commité avant toute analyse : aucun fichier de `projet/analyses/` ne le précède dans l'historique.

## Les missions

[Les quatre missions, en deux pages (PDF)](supports/projet/mth101-synthese-missions.pdf)

| Mission | Commande | Note de cadrage | Kit, partie 1 |
|---|---|---|---|
| Les annulations | [PDF](supports/projet/mth101-a1-annulations-commande.pdf) | [PDF](supports/projet/mth101-a1-annulations-note-de-cadrage.pdf) | [PDF](supports/projet/mth101-a1-annulations-kit-partie-1.pdf) |
| Recommandé par l'IA | [PDF](supports/projet/mth101-a2-recommandation-ia-commande.pdf) | [PDF](supports/projet/mth101-a2-recommandation-ia-note-de-cadrage.pdf) | [PDF](supports/projet/mth101-a2-recommandation-ia-kit-partie-1.pdf) |
| Le temps d'attente | [PDF](supports/projet/mth101-c1-temps-attente-commande.pdf) | [PDF](supports/projet/mth101-c1-temps-attente-note-de-cadrage.pdf) | [PDF](supports/projet/mth101-c1-temps-attente-kit-partie-1.pdf) |
| Les robots de service | [PDF](supports/projet/mth101-c2-robots-de-service-commande.pdf) | [PDF](supports/projet/mth101-c2-robots-de-service-note-de-cadrage.pdf) | [PDF](supports/projet/mth101-c2-robots-de-service-kit-partie-1.pdf) |

La partie 2 des kits arrive le 23 octobre, avec les jeux de répétition et le lancement de l'omnibus et des audits.

## Le tirage du 9 octobre

Huit équipes, numérotées de 1 à 8 ; les équipes 3 et 6 sont les trinômes. Graine : 8532.

| Équipe | Mission |
|---|---|
| 1 | Les annulations |
| 2 | Les robots de service |
| 3 (trinôme) | Recommandé par l'IA |
| 4 | Les annulations |
| 5 | Le temps d'attente |
| 6 (trinôme) | Recommandé par l'IA |
| 7 | Le temps d'attente |
| 8 | Les robots de service |

Pour refaire le tirage, dans le terminal d'un codespace :

```bash
cd /tmp
curl -fsSL -O https://raw.githubusercontent.com/Ad-C/mth101/main/scripts/tirage-missions.py
python3 tirage-missions.py --equipes 8 --trinomes 3 6 --graine 8532
```

Le script : [`scripts/tirage-missions.py`](https://github.com/Ad-C/mth101/blob/main/scripts/tirage-missions.py), versé dans le domaine public ([CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.fr)). Il affiche aussi la chance de chaque équipe d'obtenir chaque mission : 1 sur 4, binôme ou trinôme.
