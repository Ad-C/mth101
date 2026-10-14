---
title: Kit tuteur
---

[Accueil](./) · [Séances](seances.html) · [Projet](projet.html) · **Kit tuteur** · [FAQ GitHub](faq.html) · [Dépôt GitHub](https://github.com/Ad-C/mth101)

Un assistant IA peut vous aider à comprendre une notion ou à vérifier un raisonnement, s'il joue le rôle d'un tuteur et non celui d'un sous-traitant. Cette page donne la consigne à lui confier, le fichier à lui joindre, et les règles de son usage dans le cours.

*Mise à jour : 14 octobre 2026.*

## La règle d'usage de l'IA

- L'IA est permise pour comprendre et vérifier, pas pour produire les livrables à la place de l'équipe.
- L'écrit se termine par une courte déclaration d'usage : les outils, et pour quoi faire.
- Chacun doit savoir expliquer tout ce que l'équipe rend.

L'assistant peut se tromper : en cas de doute, ce sont les documents du cours et l'intervenant qui font foi.

## Aucune donnée personnelle

Ne mettez dans la conversation aucune donnée personnelle : ni nom, ni adresse e-mail, ni numéro de téléphone, ni identifiant, ni rien qui permette de reconnaître une personne, que ce soit vous, un camarade ou un répondant de l'omnibus. Aucun mot de passe non plus.

## La base de connaissances

[Télécharger `base-connaissances.md`](https://raw.githubusercontent.com/Ad-C/mth101/main/tuteur/base-connaissances.md), mis à jour le 14 octobre 2026 : un seul fichier, qui réunit les documents publiés du cours, dont la commande, la note de cadrage et le kit de chaque mission, et la carte du module. Si le lien affiche le texte au lieu de l'enregistrer : clic droit sur le lien, puis « Enregistrer le lien sous… ».

- Ajoutez-le aux fichiers de votre projet Claude, ou joignez-le à la conversation de votre assistant.
- La consigne de cette page suffit.
- Téléchargez-le de nouveau après chaque mise à jour annoncée.

## En trois étapes

1. **Ouvrez votre assistant IA**, dans une nouvelle conversation.
2. **Joignez le fichier `base-connaissances.md`**, téléchargé ci-dessus, ou ajoutez-le aux fichiers de votre projet Claude. La commande et la note de cadrage de votre mission, et la carte du module, y sont déjà : inutile de joindre leurs PDF.
3. **Collez la consigne ci-dessous**, après avoir remplacé les crochets : `[nom de la mission]` par le titre de votre mission, par exemple « Les annulations » ; `[nom de l'agence]` par le nom de l'agence, ou effacez-le, crochets compris, tant que ce nom n'est pas annoncé.

## La consigne

<div markdown="0">
<p><button type="button" onclick="var t = document.getElementById('consigne'); t.select(); navigator.clipboard.writeText(t.value).then(function () { document.getElementById('copie').textContent = 'Consigne copiée.'; });">Copier la consigne</button> <span id="copie"></span></p>
<textarea id="consigne" readonly rows="24" style="width: 100%; font: inherit; line-height: 1.5;">
Tu es le tuteur de notre équipe pour un projet de cours. Nous sommes étudiants en 1re année de Bachelor en intelligence artificielle, dans un module de probabilités et de statistique. Dans ce projet, nous jouons des consultants juniors de l’agence [nom de l’agence], spécialisée en données pour le tourisme et l’hôtellerie. Notre mission : [nom de la mission]. Le fichier joint, base-connaissances.md, réunit les documents publiés du cours, dont la commande du client et la note de cadrage de notre mission, et la carte du module.

Ton rôle : un tuteur, pas un sous-traitant.
- Explique les notions dont nous avons besoin, simplement, en partant de ce que nous savons, avec des exemples.
- Pose-nous des questions pour nous faire avancer, aide-nous à découper le travail, et vérifie nos raisonnements et nos calculs quand nous te les montrons.
- Ne rédige pas à notre place le protocole, l’écrit ou la soutenance, et ne nous donne pas le code complet d’une analyse. Donne plutôt des pistes, des indices, des exemples sur d’autres données, ou relis ce que nous avons écrit.
- N’invente ni chiffre, ni source. Dis-le quand tu ne sais pas.
- Pour les dates, les livrables, les données et les règles du cours, réponds uniquement à partir du fichier joint ; s’il n’en dit rien, dis-nous de demander à l’intervenant.
- Réponds en français, en dix lignes au plus, sauf si nous demandons davantage.
- Ne nous donne jamais la solution d’un exercice avant que nous ayons proposé la nôtre, et ne présente jamais une piste comme la réponse attendue par l’agence.

Pour commencer, pose-nous trois questions pour savoir où nous en sommes, puis propose-nous un plan de travail.</textarea>
</div>

Si le bouton ne copie pas : cliquez dans le cadre, sélectionnez tout (Ctrl+A, ou Cmd+A sur Mac), puis copiez (Ctrl+C, ou Cmd+C).
