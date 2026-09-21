"""Les sources : d'où vient chaque chiffre, et ce qu'il ne dit pas.

La page se construit à partir de ``chiffres.py`` : ajouter un chiffre au site
l'ajoute ici, et un chiffre sans source ne franchit pas les tests. C'est la
seule manière connue d'éviter qu'une page de programme finisse par citer des
nombres dont plus personne ne sait l'origine.
"""

from html import escape

from ..chiffres import CHIFFRES, PEREMPTION_MOIS, SOURCES, verifies
from ..gabarit import (
    DEPOT, affiche, encadre, icone, note, plan, section, suite,
)

TITRE = "Sources et méthode"
DESCRIPTION = (
    "Chaque chiffre cité sur ce site, l'organisme qui le publie, l'année à"
    " laquelle il se rapporte et ce qu'il ne dit pas. Ainsi que les limites de"
    " l'exercice, écrites par nous."
)


MOIS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre")


def _en_clair(iso: str) -> str:
    """Une date ISO en français : « 21 septembre 2026 »."""
    annee, mois, jour = iso.split("-")
    return f"{int(jour)} {MOIS[int(mois) - 1]} {annee}"


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
        lignes = ""
        for c in entrees:
            if c.verifie:
                marque = (f'<span class="badge">vérifié le'
                          f' {escape(_en_clair(c.verifie_le))}</span>')
            else:
                marque = '<span class="badge a-verifier">à revérifier</span>'
            document = (f'<a href="{c.url}">{escape(c.document)}</a>'
                        if c.url else escape(c.document))
            lignes += (
                f"<dt>{escape(c.valeur)} — {escape(c.libelle)}"
                f' <span class="badge">{escape(c.annee)}</span> {marque}</dt>'
                f"<dd>{escape(c.precision)}"
                f'<span class="document">{document}</span></dd>'
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
            " la publication précise d'où chacun sort, la date à laquelle nous l'y"
            " avons vérifié pour la dernière fois, et leurs limites — y compris"
            " celles qui gênent notre propre démonstration.",
        ),

        plan((
            ("inventaire", "L'inventaire des chiffres"),
            ("limites", "Les limites"),
            ("methode", "Comment ce site est fait"),
        )),

        section(
            "L'inventaire des chiffres",
            f"<p>Chaque section se déplie. Les valeurs sont celles publiées par"
            " l'organisme cité, arrondies : le site compare des ordres de grandeur,"
            " et la décimale se trouve dans la source. Chaque chiffre porte le"
            " titre de la publication où il se trouve — pas l'adresse d'un portail"
            " sur lequel il faudrait le chercher.</p>"
            f"<p><strong class=\"cle-texte\">{verifies()[0]} des"
            f" {verifies()[1]} chiffres</strong> ont été rouverts à la source et"
            " revérifiés à la dernière mise à jour. Les autres portent la mention"
            " « à revérifier » : ils viennent de publications que nous n'avons pas"
            " rouvertes depuis, et nous préférons l'écrire que laisser croire à une"
            " fraîcheur que nous n'avons pas contrôlée. Un test du dépôt refuse par"
            f" ailleurs toute vérification datant de plus de {PEREMPTION_MOIS}"
            " mois.</p>" + _inventaire(),
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
                    "<li><strong>Notre chiffre le plus frappant est le plus"
                    " vieux.</strong> Le seul suivi français de la récidive à cinq"
                    " ans porte sur les personnes libérées en 2002 et a été publié"
                    " en 2011. Nous le citons faute de mieux, et le fait qu'il n'y"
                    " ait pas mieux est l'un de nos arguments — mais il décrit une"
                    " cohorte d'il y a plus de vingt ans, et le lecteur doit en"
                    " tenir compte. La récidive à un an, elle, est publiée chaque"
                    " année, et nous la citons aussi.</li>"
                    "<li><strong>Le stock de peines en attente n'a pas de série"
                    " officielle — mais les taux d'exécution, si.</strong> Nous"
                    " avons longtemps écrit ici que le ministère ne publiait pas ces"
                    " chiffres. C'était inexact, et nous l'avons corrigé : les taux"
                    " de mise à exécution figurent dans les « Références"
                    " statistiques Justice ». Ce qui manque est le niveau du stock à"
                    " une date donnée, et le fait que les taux publiés reposent sur"
                    " des définitions qui ne se recoupent pas d'une publication à"
                    " l'autre.</li>"
                    "<li><strong>Nos chiffres de prison périment en un mois.</strong>"
                    " La population détenue est publiée mensuellement et bat son"
                    " record presque à chaque parution. Les chiffres de cette"
                    " section sont tous pris au 1<sup>er</sup> février 2026, pour"
                    " qu'ils se rapportent les uns aux autres — l'effectif réel, à"
                    " la date où vous lisez, est plus élevé.</li>"
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
                " orphelin de source ou de document, qu'aucune vérification n'a"
                f" dépassé {PEREMPTION_MOIS} mois, qu'aucune mesure du programme"
                " n'est privée de véhicule juridique, de coût ou d'objection, que le"
                " chiffrage annoncé est bien la somme des mesures annoncées, et que"
                " le HTML publié correspond au code publié. Un programme dont les"
                " comptes ne tombent pas juste ne peut pas être publié : c'est une"
                " machine qui le refuse, pas notre vigilance.</p>",
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
