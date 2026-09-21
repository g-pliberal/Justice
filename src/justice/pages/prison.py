"""La prison : la surpopulation, son coût, et ce qu'on y fait des gens."""

from ..chiffres import CHIFFRES, fiches, valeur
from ..gabarit import (
    affiche, carte, confrontation, encadre, note, plan, section, suite,
)

TITRE = "Prison et peines"
DESCRIPTION = (
    "Plus de 86 000 détenus pour 63 000 places, une condamnation européenne"
    " restée sans effet depuis 2020, 120 € par jour et par personne : l'état"
    " des prisons françaises et la réforme que nous proposons."
)


def corps() -> str:
    return "\n".join([
        affiche(
            "Le constat, puis la proposition",
            "Des prisons pleines, un État qui ne tient pas sa parole",
            "La France détient plus de personnes qu'elle n'a de places, a été"
            " condamnée pour cela par la Cour européenne des droits de l'homme, et"
            " n'a pas résorbé l'écart depuis. <strong class=\"cle-texte\">Une peine"
            " exécutée dans des conditions indignes n'est pas la peine qui a été"
            " prononcée.</strong>",
        ),

        plan((
            ("surpopulation", "La surpopulation"),
            ("cout", "Ce que cela coûte"),
            ("proposition", "Ce que nous proposons"),
        )),

        section(
            "La surpopulation",
            "".join([
                fiches("detenus", "places", "densite", "matelas"),
                "<p>La densité carcérale globale approche 137 %, mais la moyenne"
                " trompe : les centres de détention et les maisons centrales, qui"
                " accueillent les longues peines, fonctionnent en cellule"
                " individuelle. La surpopulation est concentrée dans les maisons"
                " d'arrêt, où sont détenus les prévenus — présumés innocents — et les"
                " condamnés à de courtes peines. C'est là que la densité atteint"
                " " + valeur("densite_maison_arret") + ", et là que des personnes"
                " dorment au sol. Vingt-cinq établissements dépassent 200 %.</p>",
                note(
                    "<p>Le " + valeur("cedh") + ", dans l'arrêt <em>J.M.B. et autres"
                    " c. France</em>, la Cour européenne des droits de l'homme a jugé"
                    " que les conditions de détention dans plusieurs établissements"
                    " français violaient l'article 3 de la Convention — l'interdiction"
                    " des traitements inhumains ou dégradants — et a demandé à la"
                    " France d'adopter des mesures générales pour résorber la"
                    " surpopulation. Six ans plus tard, le nombre de personnes"
                    " détenues a augmenté de plus de 15 %, et chaque mois bat le"
                    " record du précédent.</p>",
                    genre="avertissement",
                ),
                carte(
                    "<h3>Le principe de l'encellulement individuel</h3>"
                    "<p>Il est inscrit dans la loi française depuis 1875. Il n'a"
                    " jamais été appliqué. Le Parlement en a repoussé l'échéance à"
                    " intervalles réguliers, par moratoires successifs, plutôt que"
                    " d'en tirer les conséquences dans un sens ou dans l'autre. Une"
                    " règle que l'État se donne à lui-même et qu'il reporte depuis"
                    " cent cinquante ans n'est pas une règle : c'est une"
                    " déclaration.</p>"
                ),
            ]),
            ancre="surpopulation",
        ),

        section(
            "Ce que cela coûte",
            "".join([
                fiches("cout_detention", "cout_place", "recidive_1an",
                       "places_livrees"),
                "<p>Une journée de détention coûte à la collectivité "
                + valeur("cout_detention") + " par personne, soit plus de 40 000 €"
                " par an — davantage qu'une année d'études supérieures, davantage que"
                " le salaire médian. Et " + valeur("recidive_1an") + " des"
                " sortants sont recondamnés dans l'année qui suit leur"
                " libération.</p>"
                "<p>Ces deux nombres, côte à côte, définissent le problème. La prison"
                " est le plus coûteux des services publics par usager, et celui dont"
                " le taux d'échec est le mieux connu et le moins discuté. Le"
                " contribuable libéral a le droit de demander ce qu'il achète.</p>",
                "<p>Le travail en détention a été refondu par la loi du 22 décembre"
                " 2021, qui a substitué à l'ancien « acte d'engagement » un contrat"
                " d'emploi pénitentiaire ouvrant des droits sociaux. C'est la bonne"
                " direction ; elle reste très en deçà de ce qu'elle pourrait être :"
                " une minorité des personnes détenues exerce une activité"
                " rémunérée.</p>",
            ]),
            ancre="cout",
        ),

        section(
            "Ce que nous proposons",
            "".join([
                confrontation(
                    titre_aujourdhui="Une capacité qui court après les entrées",
                    aujourdhui=(
                        "<ul>"
                        "<li>Un « plan 15 000 » lancé en 2017 pour 2027 :"
                        " " + CHIFFRES["places_livrees"].valeur + " places livrées,"
                        " coût réévalué de 46 %, achèvement repoussé à 2031.</li>"
                        "<li>Aucune conséquence juridique lorsqu'un établissement"
                        " dépasse sa capacité.</li>"
                        "<li>Des courtes peines exécutées en maison d'arrêt surpeuplée,"
                        " sans travail ni formation.</li>"
                        "</ul>"
                    ),
                    titre_demain="Une obligation de capacité, opposable",
                    demain=(
                        "<ul>"
                        "<li>Publication mensuelle de la densité par établissement, et"
                        " information du juge qui prononce.</li>"
                        "<li>Au-delà d'un seuil, obligation pour l'administration de"
                        " saisir le juge de l'application des peines des situations"
                        " aménageables : l'État choisit qui il libère selon des"
                        " critères de dangerosité, plutôt que de laisser la"
                        " surpopulation choisir à sa place.</li>"
                        "<li>Programme porté à environ 3 000 places nettes par"
                        " an — ce que coûtent 800 M€ à " + CHIFFRES["cout_place"].valeur
                        + " la place —, avec recours à la conception-réalisation et à"
                        " la gestion déléguée là où elle livre plus vite et moins"
                        " cher. La mesure se juge sur le coût complet publié"
                        " opération par opération, pas sur le principe.</li>"
                        "</ul>"
                    ),
                ),
                confrontation(
                    titre_aujourdhui="Une détention sans contrepartie",
                    aujourdhui=(
                        "<ul>"
                        "<li>Une minorité de détenus travaille ou se forme.</li>"
                        "<li>Le suivi à la sortie dépend de services d'insertion"
                        " saturés.</li>"
                        "<li>La récidive n'est plus mesurée sur cohorte récente.</li>"
                        "</ul>"
                    ),
                    titre_demain="Le travail, la formation, et la mesure",
                    demain=(
                        "<ul>"
                        "<li>Objectif d'une activité — travail rémunéré, formation ou"
                        " enseignement — pour toute personne détenue, avec ouverture"
                        " des ateliers aux entreprises selon une procédure simple et"
                        " un contrat de droit commun adapté.</li>"
                        "<li>Rémunération réelle, dont une part indemnise les parties"
                        " civiles et une part est bloquée jusqu'à la sortie.</li>"
                        "<li>Publication annuelle du taux de recondamnation par"
                        " établissement et par type de peine : la statistique de 2011"
                        " doit redevenir une série.</li>"
                        "</ul>"
                    ),
                ),
                encadre(
                    "<h3>La ligne, en une phrase</h3>"
                    "<p>Nous voulons que les peines privatives de liberté soient"
                    " réservées à ceux dont la liberté menace celle des autres, que"
                    " ces peines soient exécutées immédiatement et dans des conditions"
                    " conformes au droit, et que tout le reste — les courtes peines"
                    " sans violence, les défauts de paiement, les manquements"
                    " administratifs — soit sanctionné autrement. Ce n'est ni"
                    " l'indulgence ni la fermeté : c'est l'usage économe d'un"
                    " instrument rare et coûteux.</p>"
                ),
            ]),
            ancre="proposition",
        ),

        suite("La justice civile et économique", "civile.html"),
    ])
