# REX Pro Bono — Centres Relier 2026

Support de présentation (retour d'expérience) sur la mission pro bono
**BearingPoint × Centres Relier** de l'été 2026 : améliorer un chatbot déjà
développé (Monster Messenger) avant son déploiement auprès de vrais
utilisateurs.

Le deck couvre :

- **Observabilité** — Langfuse : lire les traces, les sessions et exploiter les données conversationnelles.
- **Évaluation** — LLM as a judge : conversations, stratégies recommandées, performance du RAG.
- **Industrialisation** — GitHub Actions : automatisation des analyses, intégrations, points de vigilance.
- **REX & risques** — vibe coding, coûts, soutenabilité GCP.

## Consulter les slides

Le deck est un fichier HTML sans build (CSS/JS inline). Seules les captures
d'écran de la démo Langfuse sont chargées depuis [`assets/`](assets/).

- **En ligne :** https://arno-vel-bept.github.io/rex-centres-relier-2026/
- **En local :** ouvrir [`slides.html`](slides.html) dans un navigateur (garder le dossier `assets/` à côté).

### Raccourcis clavier

| Touche | Action |
| --- | --- |
| `←` / `→` | Naviguer entre les slides |
| `O` | Vue mosaïque (overview) |
| `F` | Plein écran |
| `Home` / `End` | Première / dernière slide |
| `Sources` (bouton) | Afficher les références internes |

## Déploiement

Chaque push sur `main` déclenche le workflow
[`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml),
qui publie `slides.html` (servi comme `index.html`) et le dossier `assets/`
sur GitHub Pages.

> GitHub Pages sur un dépôt privé nécessite un plan GitHub payant
> (Pro, Team ou Enterprise). Sinon, publier le dépôt ou consulter le fichier
> en local.

## Contenu

- `slides.html` — la présentation complète (HTML/CSS/JS inline).
- `assets/` — captures d'écran Langfuse utilisées dans la slide de démo.
- Les blocs `À COMPLÉTER` restants signalent les exemples à ajouter avant la présentation.

## Sources

Sources internes : échanges Outlook & Teams, août 2026 (voir le panneau
« Sources » dans le deck).
