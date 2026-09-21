# Justice — le programme du Parti libéral français

Un site de programme : ce que la France fait aujourd'hui de sa justice, chiffres
et textes à l'appui, puis la réforme libérale que nous proposons. Le constat et
la proposition ne sont jamais mêlés dans un même paragraphe — le premier se
vérifie, la seconde se discute.

Le site est en ligne à la racine de ce dépôt, servi par GitHub Pages :
**<https://g-pliberal.github.io/Justice/>**

## Ce que contient le site

| Page | Ce qu'elle dit |
| --- | --- |
| `index.html` | L'affiche : le constat en quatre chiffres, la réforme en quatre engagements |
| `etat-des-lieux.html` | Moyens, comparaison européenne, délais, les cinq lois qui font le droit en vigueur, la confiance |
| `penale.html` | L'inflation pénale, l'exécution des peines, et ce que nous proposons |
| `prison.html` | Surpopulation, coût, récidive, et ce que nous proposons |
| `civile.html` | Délais civils et prud'homaux, justice économique, petits litiges |
| `libertes.html` | Statut du parquet, garanties avant jugement, surveillance |
| `programme.html` | Les vingt mesures, leur véhicule juridique, leur coût, et le chiffrage d'ensemble |
| `sources.html` | Tous les chiffres du site, leur source, leur année, et les limites de l'exercice |

## Deux principes de fabrication

**Aucun chiffre sans source.** Les nombres ne sont pas écrits dans le texte :
ils sont déclarés dans `src/justice/chiffres.py` avec l'organisme qui les
publie, l'année à laquelle ils se rapportent et ce qu'ils ne disent pas. La
page « Sources » se construit à partir de cette déclaration, et un test refuse
un chiffre orphelin de source — comme un chiffre déclaré et cité nulle part.

**Aucune mesure sans véhicule ni coût.** Chacune des vingt mesures du programme
porte le texte par lequel elle se prend — loi constitutionnelle, loi organique,
loi ordinaire, décret — et son ordre de grandeur budgétaire. Un test vérifie
que les vingt les portent.

## Fabriquer le site

```sh
python3 scripts/construire.py   # écrit les huit pages HTML à la racine
python3 tests/verifier.py       # les vérifications, sans aucune dépendance
```

Le HTML produit est versionné : le dépôt est servi tel quel, sans étape de
construction chez l'hébergeur. Après toute modification du texte, relancez la
construction — un test échoue si le HTML publié n'est plus celui que produit le
code publié.

Pour le relire dans un navigateur, servez le dossier par HTTP plutôt que
d'ouvrir les fichiers directement : en `file://`, le navigateur refuse de
charger les polices (règle d'origine), et la page s'affiche dans la police du
système.

```sh
python3 -m http.server 8000   # puis http://localhost:8000
```

## Organisation

```
index.html, *.html        les pages publiées, produites par le script
moteur/style.css          la charte du parti, copiée du dépôt retraitecomptenotionelle
moteur/complement.css     ce que ce site-ci ajoute à la charte
moteur/polices/           Public Sans et Instrument Serif, servies par le dépôt (OFL)
moteur/icones/            les pictogrammes Lucide employés (ISC)
src/justice/gabarit.py    bandeau, affiche, pied, et tous les fragments
src/justice/chiffres.py   les chiffres et leurs sources
src/justice/pages/        le texte, une page par module
scripts/construire.py     la construction
tests/verifier.py         les vérifications
```

Rien n'est chargé depuis un tiers : ni police, ni script, ni mesure d'audience,
ni cookie. Lire un programme politique ne devrait rien apprendre de vous à
personne, et surtout pas à nous.

## L'apparence

La charte est celle du site frère,
[retraite à comptes notionnels](https://github.com/g-pliberal/retraitecomptenotionelle) :
fond vert profond, titres massifs en capitales, or pour ce qui compte, crème
pour ce qu'on doit lire de près. `moteur/style.css` en est une copie conforme,
et se remplace d'un `cp` le jour où la charte bouge ; tout ce qui est propre à
ce site vit dans `moteur/complement.css`.

## Corriger, contredire

Une erreur de fait se signale par une *issue*, une correction se propose par
une *pull request*. Les deux sont bienvenues, y compris de la part de ceux qui
ne votent pas pour nous : le constat de ce site doit tenir devant quelqu'un qui
n'en partage pas les conclusions.

## Licences

Le code est sous licence Apache 2.0 (voir `LICENSE`), les textes sous
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr). Les
polices sont sous SIL Open Font License (voir `moteur/polices/`), les
pictogrammes Lucide sous licence ISC (voir `moteur/icones/`).
