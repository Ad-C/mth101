---
title: FAQ GitHub
---

[Accueil](./) · [Séances](seances.html) · **FAQ GitHub** · [Dépôt GitHub](https://github.com/Ad-C/mth101)

Les questions posées sur GitHub et Codespaces, avec leur réponse. Les libellés sont ceux de VS Code en français ; ceux de github.com restent en anglais. Le guide GitHub distribué en séance reste la référence pour les premiers pas.

*Mise à jour : 9 octobre 2026.*

## 1. Je vois le commit de mon binôme sur github.com, mais je ne peux pas modifier le fichier

La page d'un commit montre le dépôt figé à ce moment-là : on y lit, on n'y écrit pas, et le crayon y est grisé.

Pour modifier le fichier, passez par votre codespace, et faites-y d'abord entrer le commit de votre binôme. En bas à gauche, juste à droite de `main`, cliquez sur l'icône aux deux flèches en cercle (infobulle « Synchroniser les changements »). Le fichier se met à jour ; complétez-le.

Votre codespace ne se met jamais à jour tout seul : synchronisez en arrivant.

## 2. Enregistrer, Valider, Synchroniser : quelle différence ?

- **Enregistrer** met le fichier à jour dans votre codespace, et nulle part ailleurs. Dans le navigateur, l'enregistrement se fait aussi tout seul, après un court délai.
- **Valider** (le commit) prend une photo datée du dépôt, à votre nom. Elle reste dans votre codespace.
- **Synchroniser** envoie vos commits sur GitHub et rapatrie ceux de votre binôme.

Tant que vous n'avez pas synchronisé, ni votre binôme ni l'intervenant ne voient votre travail.

En arrivant, synchronisez. En partant, validez, synchronisez, puis arrêtez le codespace.

## 3. La synchronisation affiche une erreur

- **« Nettoyez l'arborescence de travail de votre dépôt avant l'extraction »** : vous avez des modifications non validées. Cliquez d'abord sur **Valider**, puis synchronisez.
- **Un message qui commence par « Git : »**, dont le détail (**Afficher la sortie de commande**) parle de *divergent branches* : vous et votre binôme avez commité chacun de votre côté. Ouvrez un terminal (menu ☰, **Terminal**, **Nouveau terminal**). Tapez une fois `git config --global pull.rebase false`, puis synchronisez de nouveau.
- **« Il existe des conflits de fusion »** : vous avez modifié les mêmes lignes. Ouvrez le fichier listé sous **Fusionner les changements**. Au-dessus de chaque bloc en conflit, choisissez **Accepter la modification actuelle** (la vôtre), **Accepter la modification entrante** (celle de votre binôme) ou **Accepter les deux modifications**. Relisez et enregistrez. Cliquez ensuite sur **Continuer** (pendant une fusion, c'est le nom du bouton **Valider**), puis synchronisez. Si le conflit porte sur un notebook (`.ipynb`), ne validez rien et prévenez l'intervenant.

Pour l'éviter, synchronisez en arrivant, et ne modifiez pas un même fichier à deux en même temps, surtout un notebook.

## 4. Mon binôme ne voit pas le dépôt (erreur 404)

Il doit accepter l'invitation, connecté avec son propre compte :
- depuis le mail reçu ;
- ou sur `https://github.com/<compte du propriétaire>/mth101/invitations`, bouton **Accept invitation**.

Une invitation expire sept jours après son envoi. Passé ce délai, le propriétaire du dépôt invite de nouveau : **Settings**, **Collaborators**, **Add people**.

Une erreur 404 vient aussi, souvent, d'une connexion avec un autre compte.

## 5. Comment savoir si je suis dans le bon codespace ?

Sur <https://github.com/codespaces>, chaque codespace indique son dépôt. Le vôtre doit être celui de votre binôme, `<compte du propriétaire>/mth101`. Ce ne doit être ni `Ad-C/mth101` (le dépôt du cours, qui porte le même nom), ni `Ad-C/mth101-modele`. Dans le terminal, `git remote -v` affiche la même adresse.

Trois signes d'alerte :
- le panneau **Contrôle de code source** propose **Publier Branch** (c'est bien le libellé) ;
- l'icône en bas à gauche est un nuage ;
- vos commits n'arrivent pas dans le dépôt de l'équipe.

Dans un codespace ouvert sur un dépôt où vous ne pouvez pas écrire, un commit crée une copie publique (un *fork*) sous votre compte, sans rien vous demander.

Dans tous les cas : n'effacez rien et prévenez l'intervenant. Ouvrez ensuite le bon codespace depuis la page du dépôt de l'équipe : **Code**, onglet **Codespaces**.

## 6. Le notebook ne s'exécute pas, ou ne trouve pas pandas

En haut à droite du notebook : **Sélectionner le noyau**, puis **Python Environments**, puis **Python 3.12**.

S'il manque encore une bibliothèque, tapez dans un terminal, à la racine du dépôt :

```bash
pip3 install --user -r requirements.txt
```

C'est la commande que le codespace lance à sa création. Relancez ensuite **Exécuter tout**.

## 7. Mon codespace s'est arrêté. Combien de temps puis-je l'utiliser ?

Un codespace s'arrête seul après 30 minutes d'inactivité. Rien n'est perdu : rouvrez-le depuis <https://github.com/codespaces>.

Le quota gratuit, environ 60 heures par mois, est décompté sur le compte de la personne qui a créé le codespace. En fin de séance, arrêtez-le : **…**, puis **Stop codespace**.

Gardez un seul codespace par dépôt et supprimez les autres : **…**, puis **Delete**. Un codespace occupe de l'espace même arrêté. Un codespace inutilisé pendant 30 jours est supprimé, avec tout ce qui n'a pas été synchronisé.

## 8. On a travaillé à deux sur un seul ordinateur : comment apparaître tous les deux ?

Le commit porte le nom du compte connecté. Pour créditer l'autre, terminez le message de commit par une ligne vide, puis une ligne de co-auteur :

```text
Commande 2 : calculs et recommandation

Co-authored-by: Prénom <12345678+login@users.noreply.github.com>
```

Chacun trouve son adresse sur <https://github.com/settings/emails>, sous *Keep my email addresses private*, et la donne une fois à son binôme. Le commit s'affiche alors avec ses deux auteurs.

Plus simple : alternez au clavier, et chacun valide ce qu'il a écrit.

## 9. Comment pré-enregistrer notre protocole ?

Écrivez-le dans un fichier du dossier `projet/protocole/`, par exemple `protocole.md`. Validez et synchronisez avant d'ajouter quoi que ce soit dans `projet/analyses/`. Vérifiez ensuite sur github.com qu'il apparaît bien dans le dossier.

Le `README.md` déjà présent vient du modèle : ce n'est pas votre protocole. Toute modification ultérieure reste visible, et datée, dans l'historique.

## 10. Comment l'intervenant suit-il les dépôts ?

Chaque semaine, et à chaque jalon, il lit l'historique de votre dépôt : les dates, les auteurs, les fichiers. Il regarde trois choses :
- la régularité du travail ;
- la présence de chaque membre ;
- le respect des jalons, par exemple, au 15 octobre, un protocole commité avant toute analyse.

Le nombre de commits n'est pas une note : en multiplier de tout petits n'apporte rien. Si un membre n'apparaît plus depuis une semaine, l'intervenant pose la question à l'équipe : c'est une question, pas une sanction. Pour un travail à deux sur un seul écran, voir la question 8.

Ses notes de suivi restent chez lui, hors de tout dépôt, et sont supprimées à la fin de la période d'évaluation.

Une question qui n'est pas ici ? Posez-la en séance : elle rejoindra cette page.
