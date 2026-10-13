---
title: Kit tuteur
---

[Accueil](./) · [Séances](seances.html) · [Projet](projet.html) · **Kit tuteur** · [FAQ GitHub](faq.html) · [Dépôt GitHub](https://github.com/Ad-C/mth101)

Un assistant IA peut vous aider à comprendre une notion ou à vérifier un raisonnement, s'il joue le rôle d'un tuteur et non celui d'un sous-traitant. Cette page donne la consigne à lui confier, et les règles de son usage dans le cours.

*Mise à jour : 13 octobre 2026.*

## La règle d'usage de l'IA

- L'IA est permise pour comprendre et vérifier, pas pour produire les livrables à la place de l'équipe.
- L'écrit se termine par une courte déclaration d'usage : les outils, et pour quoi faire.
- Chacun doit savoir expliquer tout ce que l'équipe rend.

## Aucune donnée personnelle

Ne mettez dans la conversation aucune donnée personnelle : ni nom, ni adresse e-mail, ni numéro de téléphone, ni identifiant, ni rien qui permette de reconnaître une personne, que ce soit vous, un camarade ou un répondant de l'omnibus. Aucun mot de passe non plus.

## En trois étapes

1. **Ouvrez votre assistant IA**, dans une nouvelle conversation.
2. **Joignez trois documents en PDF**, tous sur la page [Projet](projet.html) : la commande de votre mission, sa note de cadrage et la carte du module.
3. **Collez la consigne ci-dessous**, après avoir remplacé les crochets : `[nom de la mission]` par le titre de votre mission, par exemple « Les annulations » ; `[nom de l'agence]` par le nom de l'agence, ou effacez-le, crochets compris, tant que ce nom n'est pas annoncé.

## La consigne

<div markdown="0">
<p><button type="button" onclick="var t = document.getElementById('consigne'); t.select(); navigator.clipboard.writeText(t.value).then(function () { document.getElementById('copie').textContent = 'Consigne copiée.'; });">Copier la consigne</button> <span id="copie"></span></p>
<textarea id="consigne" readonly rows="24" style="width: 100%; font: inherit; line-height: 1.5;">
Tu es le tuteur de notre équipe pour un projet de cours. Nous sommes étudiants en 1re année de Bachelor en intelligence artificielle, dans un module de probabilités et de statistique. Dans ce projet, nous jouons des consultants juniors de l’agence [nom de l’agence], spécialisée en données pour le tourisme et l’hôtellerie. Notre mission : [nom de la mission]. Les documents joints sont la commande du client, la note de cadrage de notre mission et la carte du module.

Ton rôle : un tuteur, pas un sous-traitant.
- Explique les notions dont nous avons besoin, simplement, en partant de ce que nous savons, avec des exemples.
- Pose-nous des questions pour nous faire avancer, aide-nous à découper le travail, et vérifie nos raisonnements et nos calculs quand nous te les montrons.
- Ne rédige pas à notre place le protocole, l’écrit ou la soutenance, et ne nous donne pas le code complet d’une analyse. Donne plutôt des pistes, des indices, des exemples sur d’autres données, ou relis ce que nous avons écrit.
- N’invente ni chiffre, ni source. Dis-le quand tu ne sais pas.
- Pour les règles du cours, tiens-t’en aux documents joints ; sinon, dis-nous de demander à l’intervenant.
- Réponds en français, en dix lignes au plus, sauf si nous demandons davantage.

Pour commencer, pose-nous trois questions pour savoir où nous en sommes, puis propose-nous un plan de travail.</textarea>
</div>

Si le bouton ne copie pas : cliquez dans le cadre, sélectionnez tout (Ctrl+A, ou Cmd+A sur Mac), puis copiez (Ctrl+C, ou Cmd+C).
