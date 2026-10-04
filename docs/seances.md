---
title: Séances
---

[Accueil](./) · **Séances** · [Dépôt GitHub](https://github.com/Ad-C/mth101)

Le résumé de chaque séance passée, avec ses supports en PDF.

{% assign resumes = site.pages | where_exp: "p", "p.path contains 'seances/seance-'" | sort: "path" %}
{% for p in resumes %}
- [{{ p.title }}]({{ p.url | relative_url }})
{% endfor %}

{% if resumes.size == 0 %}
Le premier résumé paraîtra après la séance du mercredi 7 octobre.
{% endif %}
