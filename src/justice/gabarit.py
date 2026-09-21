"""La mise en page commune : bandeau, affiche, pied, et les fragments.

Tout le HTML du site sort d'ici. Une page n'écrit jamais de balise `<header>`
ni de `<footer>` : elle rend un corps, et ``document`` l'enveloppe. C'est ce
qui garantit que les huit pages se reconnaissent comme un seul site, et que
changer le pied de page se fait à un seul endroit.

La charte est celle du dépôt `retraitecomptenotionelle`, copiée dans
`moteur/style.css` : les noms de classe employés ici sont les siens.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

#: La racine du dépôt, d'où sont lus les pictogrammes.
RACINE = Path(__file__).resolve().parents[2]

DEPOT = "https://github.com/g-pliberal/justice"
SITE_PARENT = "https://partiliberalfrancais.fr"
SITE_RETRAITE = "https://g-pliberal.github.io/retraitecomptenotionelle/"
NOM_DU_SITE = "Justice"

#: Les pages, par groupe, dans l'ordre du bandeau. Le fichier est aussi
#: l'adresse : le site est servi comme un dossier de fichiers, sans routeur,
#: ce qui lui permet de vivre sur n'importe quel hébergement statique.
GROUPES_NAVIGATION: tuple[tuple[str, tuple[tuple[str, str], ...]], ...] = (
    (
        "Le constat",
        (
            ("etat-des-lieux.html", "État des lieux"),
            ("penale.html", "Pénal"),
            ("prison.html", "Prison"),
            ("civile.html", "Civil"),
        ),
    ),
    (
        "La proposition",
        (
            ("libertes.html", "Libertés"),
            ("programme.html", "Programme"),
        ),
    ),
    ("La méthode", (("sources.html", "Sources"),)),
)

LIENS = tuple(lien for _, liens in GROUPES_NAVIGATION for lien in liens)


def icone(nom: str) -> str:
    """Un pictogramme Lucide, inséré dans la page plutôt que chargé.

    Les huit pages en portent une poignée : autant de requêtes, et autant
    d'occasions pour un pictogramme d'arriver après le texte qu'il accompagne.
    Ils sont donc lus au moment de la construction et écrits dans le HTML, avec
    la classe `.icone` qui leur donne la taille et la couleur du texte porteur.
    """
    source = (RACINE / "moteur" / "icones" / f"{nom}.svg").read_text(encoding="utf-8")
    # Le SVG du fichier porte déjà `aria-hidden` et `currentColor` ; il ne lui
    # manque que la classe, que le fichier ne peut pas connaître.
    return source.replace("<svg ", '<svg class="icone" ', 1).strip()


def navigation(actif: str) -> str:
    """Les onglets du bandeau, par groupe.

    L'étiquette de groupe est du texte, lu par les synthèses vocales et masqué
    à l'œil : à neuf onglets, l'afficher doublait la hauteur d'un bandeau qui
    reste collé en haut.
    """
    def liens(groupe: tuple[tuple[str, str], ...]) -> str:
        return "".join(
            f'<a href="{fichier}"'
            + (' aria-current="page"' if fichier == actif else "")
            + f">{escape(libelle)}</a>"
            for fichier, libelle in groupe
        )

    return "".join(
        f'<span class="groupe"><span class="etiquette">{escape(etiquette)}</span>'
        f'<span class="liens">{liens(groupe)}</span></span>'
        for etiquette, groupe in GROUPES_NAVIGATION
    )


def entete(actif: str) -> str:
    """Bandeau de tête, précédé du lien d'évitement.

    Le lien d'évitement est le premier élément parcouru au clavier : sans lui,
    atteindre le contenu impose de traverser les sept onglets à chaque page.

    Le nom du site n'est pas un ``<h1>`` — chaque page porte le sien, massif et
    en capitales, et c'est lui le titre du document.
    """
    return f"""<a class="evitement" href="#contenu">Aller au contenu</a>
<header class="bandeau"><div class="interieur">
  <p class="nom"><a href="index.html">{icone('scale')}<span>{escape(NOM_DU_SITE)}</span></a></p>
  <nav aria-label="Navigation principale">{navigation(actif)}</nav>
</div></header>"""


def affiche(surtitre: str, titre: str, chapeau: str) -> str:
    """Le bloc de tête d'une page : sur-titre, titre massif, chapeau.

    ``titre`` et ``chapeau`` sont du HTML — ils portent les passages en or et
    les liens ; ``surtitre`` est du texte. Le titre est mis en capitales par le
    style et jamais dans le texte : certaines synthèses vocales épellent lettre
    à lettre un mot écrit en majuscules.
    """
    return (
        f'<div class="affiche"><p class="surtitre">{escape(surtitre)}</p>'
        f"<h1>{titre}</h1><p class=\"chapeau\">{chapeau}</p></div>"
    )


def pied() -> str:
    """Pied de page.

    Il porte ce qu'il faut savoir avant de citer une ligne du site : que les
    chiffres sont ceux de sources publiques, datées et liées, et que le
    programme est une proposition politique — pas un exposé du droit en
    vigueur.
    """
    return f"""<footer>
  <p><strong>Ce site est un document politique.</strong> Il expose l'état du
  droit et des moyens de la justice française, puis la réforme que le Parti
  libéral français propose. Le premier se vérifie, la seconde se discute :
  les deux sont séparés sur chaque page, et rien de ce qui est proposé ici
  n'est en vigueur.</p>
  <p>Les chiffres sont ceux publiés par le ministère de la Justice, la CEPEJ,
  la Cour des comptes et l'Insee, chacun daté et lié sur la page
  <a href="sources.html">Sources</a>. Ils décrivent des ordres de grandeur :
  <a href="sources.html#limites">lisez les limites</a> avant d'en citer un.
  Textes et code sur <a href="{DEPOT}">GitHub</a> — code sous licence Apache 2.0,
  textes sous <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">CC BY-SA 4.0</a>.</p>
  <p class="retour-site">Un site du <a href="{SITE_PARENT}">Parti libéral français</a>.
  Voir aussi notre programme pour les retraites :
  <a href="{SITE_RETRAITE}">retraite à comptes notionnels</a>.</p>
</footer>"""


def document(*, fichier: str, titre: str, description: str, corps: str) -> str:
    """La page complète, de ``<!doctype>`` au ``</html>``.

    ``titre`` est celui de l'onglet du navigateur et des moteurs de recherche ;
    il se termine par le nom du site, sauf sur l'accueil où il l'est déjà.
    """
    titre_complet = titre if fichier == "index.html" else f"{titre} — Justice"
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- La couleur du bandeau de tête : sur un téléphone, la barre du navigateur la
     reprend, et la page commence où elle commence. -->
<meta name="theme-color" content="#0b3d3a">
<title>{escape(titre_complet)}</title>
<meta name="description" content="{escape(description)}">
<meta property="og:title" content="{escape(titre_complet)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<link rel="icon" href="moteur/icone.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="moteur/icone.svg">
<!-- La charte du parti, puis ce que ce site-ci y ajoute. L'ordre compte : la
     seconde feuille ne redéfinit que ce qu'elle apporte. -->
<link rel="stylesheet" href="moteur/style.css">
<link rel="stylesheet" href="moteur/complement.css">
<!-- Les deux polices de l'affiche sont servies par le dépôt, et non par un
     tiers : une requête de police chez un hébergeur extérieur emporte
     l'adresse IP du lecteur, et lire un programme politique ne devrait rien
     dire de soi à personne. Elles sont préchargées parce que le titre de
     l'affiche les attend dès la première ligne rendue. -->
<link rel="preload" href="moteur/polices/public-sans-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="moteur/polices/instrument-serif-latin.woff2" as="font" type="font/woff2" crossorigin>
</head>
<body>
{entete(fichier)}
<main id="contenu" tabindex="-1">
{corps}
</main>
{pied()}
</body>
</html>
"""


# -- fragments ---------------------------------------------------------------


def section(titre: str, corps: str, *, ancre: str = "") -> str:
    """Un intertitre de page et ce qui le suit.

    L'ancre sert au plan de page : un titre sans ancre ne se cite pas, et une
    page longue dont on ne peut citer aucun passage se cite en entier ou pas
    du tout.
    """
    attribut = f' id="{ancre}"' if ancre else ""
    return f"<h2{attribut}>{titre}</h2>\n{corps}"


def plan(entrees: tuple[tuple[str, str], ...]) -> str:
    """Le sommaire d'une page longue : les ancres de ses sections.

    C'est un ``<nav>`` nommé, et non une simple liste : une page peut en
    compter plusieurs, et « navigation » tout court ne dit pas laquelle.
    """
    liens = "".join(f'<li><a href="#{ancre}">{escape(libelle)}</a></li>'
                    for ancre, libelle in entrees)
    return ('<nav class="plan" aria-label="Plan de la page">'
            '<p class="etiquette">Sur cette page</p>'
            f"<ol>{liens}</ol></nav>")


def confrontation(
    *,
    titre_aujourdhui: str,
    aujourdhui: str,
    titre_demain: str,
    demain: str,
) -> str:
    """Les deux volets : ce qui se fait, ce que nous proposons.

    L'ordre du HTML est l'ordre de lecture une fois les colonnes empilées, et
    c'est pour cela que le constat est écrit en premier : on ne propose pas
    avant d'avoir dit à quoi l'on répond.
    """
    return f"""<div class="confrontation">
  <div class="volet aujourdhui">
    <p class="etiquette">Aujourd'hui</p>
    <h3>{titre_aujourdhui}</h3>
    {aujourdhui}
  </div>
  <div class="volet demain">
    <p class="etiquette">Ce que nous proposons</p>
    <h3>{titre_demain}</h3>
    {demain}
  </div>
</div>"""


def mesure(rang: int, titre: str, corps: str, *, porte: str = "", cout: str = "") -> str:
    """Une mesure du programme : un rang, un intitulé, ce qu'elle change.

    ``porte`` dit par quel véhicule elle se prend — loi organique, loi
    ordinaire, décret, circulaire — et ``cout`` ce qu'elle pèse. Les deux sont
    facultatifs dans la signature et obligatoires dans les faits : une mesure
    dont on ne sait dire ni le véhicule ni le coût n'est pas une mesure, c'est
    un souhait. Un test le vérifie.
    """
    rappel = ""
    if porte or cout:
        morceaux = []
        if porte:
            morceaux.append(f"<span><b>Véhicule</b> {porte}</span>")
        if cout:
            morceaux.append(f"<span><b>Coût</b> {cout}</span>")
        rappel = '<p class="porte">' + "".join(morceaux) + "</p>"
    return f"""<div class="mesure">
  <p class="rang">{rang:02d}</p>
  <div class="corps"><h3>{titre}</h3>{corps}{rappel}</div>
</div>"""


def mesures(*blocs: str) -> str:
    return '<div class="mesures">' + "".join(blocs) + "</div>"


def barres(entrees: tuple[tuple[str, float, str, bool], ...], *, legende: str = "") -> str:
    """Une comparaison à quelques termes, en barres dessinées par le style.

    Chaque entrée est ``(nom, valeur, texte affiché, est-ce le terme visé)``.
    La valeur sert à la longueur de la barre, le texte à la lecture : la barre
    est un confort, la valeur écrite est l'information. La plus grande donne
    l'échelle — une comparaison à trois termes n'a pas besoin d'axe.
    """
    maximum = max(valeur for _, valeur, _, _ in entrees) or 1
    lignes = ""
    for nom, valeur, texte, visee in entrees:
        part = max(2, round(100 * valeur / maximum))
        classe = ' class="visee"' if visee else ""
        lignes += (
            f"<li{classe}><span class=\"nom\">{escape(nom)}</span>"
            '<span class="piste">'
            f'<span class="valeur">{texte}</span>'
            f'<span class="trait" style="width: {part}%"></span>'
            "</span></li>"
        )
    bloc = f'<ul class="barres">{lignes}</ul>'
    if legende:
        bloc += f'<p class="source">{legende}</p>'
    return bloc


def note(corps: str, *, genre: str = "") -> str:
    """Un encart : un rappel, une réserve, un avertissement.

    ``genre`` vaut « vigilance » pour une réserve que le site fait sur
    lui-même, « avertissement » pour ce qu'il faut avoir lu avant de continuer.
    """
    classes = "note" + (f" {genre}" if genre else "")
    if genre == "avertissement":
        corps = icone("triangle-alert") + f"<div>{corps}</div>"
    return f'<div class="{classes}">{corps}</div>'


def encadre(corps: str) -> str:
    return f'<div class="encadre">{corps}</div>'


def carte(corps: str) -> str:
    return f'<div class="carte">{corps}</div>'


def points(entrees: tuple[tuple[str, str], ...]) -> str:
    """Trois ou quatre idées de même rang, chacune sous un filet d'or."""
    blocs = "".join(
        f'<div class="point"><h3>{titre}</h3><p>{texte}</p></div>'
        for titre, texte in entrees
    )
    return f'<div class="points">{blocs}</div>'


def suite(libelle: str, fichier: str) -> str:
    """Le lien de bas de page vers la page suivante du parcours."""
    return (
        '<div class="suite"><span class="etiquette">La suite</span>'
        f'<a class="bouton" href="{fichier}">{escape(libelle)}</a></div>'
    )


def engagements(entrees: tuple[tuple[str, str, str], ...]) -> str:
    """Les engagements chiffrés du programme, en tête de l'accueil.

    Chaque entrée est ``(chiffre, promesse, détail)``. La numérotation les fait
    lire comme une liste d'engagements et non comme des statistiques
    orphelines : c'est le même bloc que sur le site des retraites, et il tient
    le même rôle — dire en quatre nombres ce que la réforme change.

    Deux par ligne, jamais trois : la charte l'impose, et la quatrième carte ne
    doit pas tomber seule sur sa ligne.
    """
    blocs = "".join(
        f'<div class="engagement"><p class="rang">{rang:02d}</p>'
        f'<p class="chiffre">{chiffre}</p>'
        f'<p class="promesse">{promesse}</p>'
        f'<p class="detail">{detail}</p></div>'
        for rang, (chiffre, promesse, detail) in enumerate(entrees, start=1)
    )
    return f'<section class="engagements"><div class="grille">{blocs}</div></section>'


def gestes(*entrees: str) -> str:
    """Le mécanisme en trois lignes numérotées : un rang énorme, une phrase."""
    lignes = "".join(
        f'<li><span class="rang">{rang}</span><span>{texte}</span></li>'
        for rang, texte in enumerate(entrees, start=1)
    )
    return f'<ol class="gestes">{lignes}</ol>'


def tableau(legende: str, entetes: tuple[str, ...], lignes: tuple[tuple[str, ...], ...],
            *, source: str = "") -> str:
    """Un tableau, dans un cadre qui défile quand il est plus large que l'écran.

    Le cadre porte ``tabindex="0"`` : chez plusieurs moteurs, une boîte qui
    défile n'est pas atteignable au clavier sans cela, et le tableau devient
    illisible pour qui n'a pas de souris.

    La première colonne est un en-tête de ligne — c'est ce que lit une synthèse
    vocale avant chaque cellule —, les suivantes sont des nombres, alignés à
    droite par la charte.
    """
    tete = "".join(f"<th scope=\"col\">{cellule}</th>" for cellule in entetes)
    corps = ""
    for ligne in lignes:
        premiere, *reste = ligne
        cellules = "".join(f"<td>{cellule}</td>" for cellule in reste)
        corps += f'<tr><th scope="row">{premiere}</th>{cellules}</tr>'
    bloc = (
        f'<div class="defilant" tabindex="0" role="group" aria-label="{escape(legende)}">'
        f"<table><caption>{legende}</caption>"
        f"<thead><tr>{tete}</tr></thead><tbody>{corps}</tbody></table></div>"
    )
    if source:
        bloc += f'<p class="source">{source}</p>'
    return bloc
