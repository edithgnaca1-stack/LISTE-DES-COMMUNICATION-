# Ma couronne, mes règles — dossier de production

**Livre :** *Ma couronne, mes règles — Le guide des cheveux texturés en Afrique*
**Autrice :** [à compléter] · **Pays de référence :** Bénin · **Ton :** vouvoiement
**Date :** octobre 2026

## Le fichier à lire

| Fichier | Contenu |
|---|---|
| **`MA-COURONNE-MES-REGLES-Extrait-v1.pdf`** | **L'extrait de 27 pages à corriger** (12 fiches ingrédients + tableau maître + 8 faux amis + Kit anti-paresse + fiche tresses + pages de travail) |
| `PLAN-EBOOK-CHEVEUX-TEXTURES.md` | Le plan éditorial du guide complet (~148 pages) |
| `maquette/index.html` | Maquette de 5 planches (rendu visuel) — imprimable en A4 |

## Comment corriger le PDF

Citez **la page et le numéro de fiche** : « page 12, fiche 3 — la dose de ricin me paraît trop faible ».
Une fiche de correction vous attend à la page 26 du document.

**Les 3 points à vérifier en priorité :**
1. Les **noms locaux** (page 25 : tableau fon / yoruba à remplir).
2. Les **prix en FCFA** par application (estimations à revérifier au marché).
3. Le **chapitre sur les tresses** (page 23 : durées, protocole, consignes à la coiffeuse).

## Ce qui reste à faire pour le guide complet

- Partie 1 (introduction) et le diagnostic des types/porosité (partie 2A) : à rédiger.
- 13 fiches ingrédients supplémentaires (argile, henné, nigelle, moringa, baobab, bissap, neem, banane-avocat, huiles essentielles…).
- Le catalogue illustré des 12 coiffures protectrices et le calendrier de l'année.
- Le chapitre « L'assiette cheveux » — **à écrire avec vous** (votre expertise en nutrition).
- Vos photos, la relecture santé, les 5 lectrices-tests, puis les exports (mobile, EPUB, N&B).

## Reproductibilité

Le PDF est généré depuis les fichiers Python de `extrait/` :
`c_intro.py`, `c_fiches.py`, `c_kit.py` (contenu) et `build_pdf.py` (mise en page).
Commande : `python3 extract/build_pdf.py` (nécessite `reportlab`).
Modifier un texte dans les fichiers de contenu, relancer, le PDF est régénéré à l'identique.
