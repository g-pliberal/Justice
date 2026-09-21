"""Les sources : d'où vient chaque chiffre, et ce qu'il ne dit pas.

La page se construit à partir de ``chiffres.py`` : ajouter un chiffre au site
l'ajoute ici, et un chiffre sans source ne franchit pas les tests. C'est la
seule manière connue d'éviter qu'une page de programme finisse par citer des
nombres dont plus personne ne sait l'origine.
"""

from html import escape

from ..chiffres import CHIFFRES, SOURCES
from ..gabarit import (
    DEPOT, affiche, encadre, icone, note, plan, section, suite,
)

TITRE = "Sources et méthode"
DESCRIPTION = (
    "Chaque chiffre cité sur ce site, l'organisme qui le publie, l'année à"
    " laquelle il se rapporte et ce qu'il ne dit pas. Ainsi que les limites de"
    " l'exercice, écrites par nous."
)


def _inventaire() -> str:
    """Tous les chiffres du site, groupés par source."""
    par_source: dict[str, list] = {cle: [] for cle in SOURCES}
    for chiffre in CHIFFRES.values():
        par_source[chiffre.source].append(chiffre)

    blocs = []
    for cle, source in SOURCES.items():
        entrees = par_source[cle]
        if not entrees:
            continue
        lignes = "".join(
            f"<dt>{escape(c.valeur)} — {escape(c.libelle)}"
            f' <span class="badge">{escape(c.annee)}</span></dt>'
            f"<dd>{escape(c.precision)}</dd>"
            for c in entrees
        )
        blocs.append(
            '<details class="section"><summary>' + icone("chevron-down")
            + f"<span>{escape(source.nom)} — {len(entrees)} chiffre"
            f"{'s' if len(entrees) > 1 else ''}</span></summary>"
            '<div class="dedans">'
            f"<p>{escape(source.detail)} "
            f'<a href="{source.url}">Consulter la source</a>.</p>'
            f'<dl class="gloses">{lignes}</dl>'
            "</div></details>"
        )
    return "".join(blocs)


def corps() -> str:
    return "\n".join([
        affiche(
            "La méthode",
            "Tous les chiffres, et ce qu'ils ne disent pas",
            "Un programme politique qui cite des nombres doit pouvoir être"
            " contredit sur chacun. Voici les "
            f"<strong class=\"cle-texte\">{len(CHIFFRES)} chiffres</strong> du site,"
            " leur source, leur année et leurs limites — y compris celles qui"
            " gênent notre propre démonstration.",
        ),

        plan((
            ("inventaire", "L'inventaire des chiffres"),
            ("limites", "Les limites"),
            ("methode", "Comment ce site est fait"),
        )),

        section(
            "L'inventaire des chiffres",
            "<p>Chaque section se déplie. Les valeurs sont celles publiées par"
            " l'organisme cité, arrondies : le site compare des ordres de grandeur,"
            " et la décimale se trouve dans la source.</p>" + _inventaire(),
            ancre="inventaire",
        ),

        section(
            "Les limites",
            "".join([
                note(
                    "<p><strong>Aucun chiffre de ce site n'est de première main.</strong>"
                    " Nous ne produisons pas de statistique : nous citons celles du"
                    " ministère de la Justice, du Conseil de l'Europe, de la Cour des"
                    " comptes et de Sciences Po, et nous les arrondissons. Une seule"
                    " grandeur est calculée par nous — le chiffrage du programme — et"
                    " elle est signalée comme telle partout où elle apparaît.</p>",
                    genre="avertissement",
                ),
                encadre(
                    "<h3>Les quatre réserves que nous ferions si nous lisions ce site</h3>"
                    "<ol class=\"serree\">"
                    "<li><strong>Les comparaisons européennes comparent des choses"
                    " différentes.</strong> Les systèmes judiciaires ne répartissent"
                    " pas les mêmes tâches entre le juge, le greffe, le notaire et"
                    " l'huissier ; les juges non professionnels — consulaires,"
                    " prud'homaux — ne sont pas comptés partout de la même manière."
                    " L'écart France-Europe est réel, son ampleur exacte se"
                    " discute.</li>"
                    "<li><strong>Les durées moyennes additionnent l'incomparable.</strong>"
                    " Un divorce par consentement mutuel et une succession disputée"
                    " comptent pour un dans la même moyenne. Les médianes par"
                    " contentieux diraient mieux les choses ; elles ne sont pas"
                    " publiées avec la même régularité.</li>"
                    "<li><strong>Nos chiffres les plus utiles sont les plus"
                    " vieux.</strong> L'étude de référence sur la récidive après une"
                    " sortie de prison date de 2011. Nous la citons faute de mieux, et"
                    " le fait qu'il n'y ait pas mieux est l'un de nos"
                    " arguments — ce qui doit inciter le lecteur à la prudence sur"
                    " l'usage que nous en faisons.</li>"
                    "<li><strong>Le stock de peines non exécutées n'a pas de série"
                    " officielle.</strong> Nous écrivons « des dizaines de milliers »"
                    " parce que c'est ce que les rapports permettent d'affirmer, et"
                    " nous nous refusons à donner un nombre précis qui aurait"
                    " l'apparence d'une donnée publiée.</li>"
                    "</ol>"
                ),
                "<p id=\"limites\">Enfin, une réserve de nature : ce site est"
                " publié par un parti. Le constat est sourcé et vérifiable ; la"
                " sélection des chiffres, elle, sert une démonstration — nous avons"
                " retenu ceux qui éclairent la lenteur, l'inexécution et le"
                " sous-dimensionnement, parce que c'est ce que nous voulons changer."
                " Un adversaire honnête en citerait d'autres, et il aurait le droit"
                " de le faire.</p>",
            ]),
            ancre="limites",
        ),

        section(
            "Comment ce site est fait",
            "".join([
                "<p>Huit pages HTML statiques, sans serveur, sans base de données et"
                " sans une ligne de JavaScript. Aucune requête n'est envoyée à un"
                " tiers : les polices de caractères sont servies par le site"
                " lui-même, il n'y a ni mesure d'audience, ni cookie, ni traceur."
                " Lire un programme politique ne devrait rien apprendre de vous à"
                " personne, et surtout pas à nous.</p>",
                "<p>Le texte est écrit dans des modules Python, les chiffres sont"
                " déclarés avec leur source, et les pages sont produites par un"
                " script de construction. Des tests vérifient qu'aucun chiffre n'est"
                " orphelin de source, qu'aucune mesure du programme n'est privée de"
                " véhicule juridique ou de coût, et que le HTML publié correspond au"
                " code publié.</p>",
                f"<p>Tout est ouvert : <a href=\"{DEPOT}\">le dépôt</a> contient le"
                " texte, les chiffres, le code et l'historique des modifications."
                " Une erreur se signale par une <em>issue</em>, une correction se"
                " propose par une <em>pull request</em>, et les deux sont"
                " bienvenues — y compris de la part de ceux qui ne votent pas pour"
                " nous.</p>",
                "<p>L'apparence est celle de la charte du Parti libéral français,"
                " partagée avec notre site sur les retraites à comptes notionnels :"
                " deux outils, une seule voix.</p>",
            ]),
            ancre="methode",
        ),

        suite("Revenir à l'accueil", "index.html"),
    ])
