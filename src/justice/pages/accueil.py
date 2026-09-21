"""L'accueil : ce que la justice française coûte, ce qu'elle rend, et ce que
nous proposons d'en faire.

C'est la seule page lue par quelqu'un qui n'a pas demandé à lire. Elle dit
donc tout en un écran — le constat en quatre nombres, la réforme en quatre
engagements — et laisse le détail aux sept autres.
"""

from ..chiffres import fiches, valeur
from ..gabarit import (
    affiche, confrontation, engagements, gestes, note, points, section, suite,
)

TITRE = "Justice — le programme du Parti libéral français"
DESCRIPTION = (
    "La justice française juge lentement, exécute mal ses propres décisions et"
    " compte deux fois moins de magistrats que ses voisins. Le constat chiffré,"
    " source par source, et la réforme libérale que nous proposons : juger vite,"
    " exécuter sûrement, punir moins de choses et mieux."
)


def corps() -> str:
    return "\n".join([
        affiche(
            "Le programme justice",
            "Une justice qui juge vite, exécute ce qu'elle prononce, "
            "et se mêle de moins de choses",
            "La France ne souffre pas d'une justice trop clémente ni trop sévère : "
            "elle souffre d'une justice <strong class=\"cle-texte\">lente, "
            "imprévisible et sous-dotée</strong>, qui promet tout et tient peu. "
            "Ce site expose d'abord ce que la France fait aujourd'hui, chiffres et "
            "textes à l'appui ; puis la réforme libérale que nous proposons, "
            "mesure par mesure.",
        ),

        note(
            "<p>Deux lectures possibles. <a href=\"etat-des-lieux.html\">L'état des"
            " lieux</a> n'engage que les sources : il décrit le droit en vigueur et"
            " les moyens réels de l'institution. <a href=\"programme.html\">Le"
            " programme</a> engage notre parti, et rien d'autre. Les deux ne sont"
            " jamais mêlés dans un même paragraphe.</p>",
            genre="entree",
        ),

        fiches("juges", "delai_civil", "densite", "confiance"),

        engagements((
            (
                "17,6",
                "Autant de juges par habitant que la médiane européenne, en dix ans.",
                "La France compte 11,1 juges professionnels pour 100 000 habitants"
                " et 3,2 procureurs, contre 17,6 et 11,1 pour la médiane des États"
                " du Conseil de l'Europe. Aucune réforme de procédure ne rattrape"
                " un tel écart : il faut recruter, former, et le dire dans une loi"
                " de programmation qui engage.",
            ),
            (
                "12 mois",
                "Un délai de jugement garanti, et opposable à l'État.",
                "Douze mois en première instance civile, six pour les litiges"
                " simples. Au-delà, le justiciable obtient réparation sans avoir à"
                " prouver une faute : le délai cesse d'être une statistique interne"
                " pour devenir une obligation de résultat.",
            ),
            (
                "90 jours",
                "Le délai maximal entre une condamnation et son exécution.",
                "Une peine prononcée et jamais exécutée détruit plus de confiance"
                " qu'une peine clémente exécutée sur-le-champ. Publication"
                " trimestrielle du stock de peines en attente, juridiction par"
                " juridiction, et extinction du stock existant en cinq ans.",
            ),
            (
                "− 1 pour + 1",
                "Aucune incrimination nouvelle sans en abroger une autre.",
                "Plus de 10 000 infractions sont en vigueur, réparties dans des"
                " dizaines de codes, et personne n'en tient le compte exact. Le"
                " droit pénal doit redevenir l'exception qu'il n'aurait jamais dû"
                " cesser d'être : un inventaire complet, puis une règle de"
                " compensation inscrite dans la loi organique.",
            ),
        )),

        section(
            "Le désaccord, en une page",
            confrontation(
                titre_aujourdhui="Punir davantage sur le papier",
                aujourdhui=(
                    "<p>Depuis trente ans, chaque fait divers produit une loi, chaque"
                    " loi de nouvelles incriminations, et presque jamais les moyens"
                    " de les appliquer. Le résultat est une justice qui prononce"
                    " beaucoup et exécute mal.</p>"
                    "<ul>"
                    "<li>Des peines prononcées puis mises à exécution des mois, parfois"
                    " des années plus tard.</li>"
                    "<li>Des prisons à " + valeur("densite") + " de leur capacité,"
                    " que la France est condamnée à désengorger depuis le "
                    + valeur("cedh") + ".</li>"
                    "<li>Un juge civil qui met " + valeur("delai_civil") + " à trancher"
                    " un litige, et autant en appel.</li>"
                    "</ul>"
                ),
                titre_demain="Punir moins de choses, et vraiment",
                demain=(
                    "<p>La force d'une sanction tient à sa <strong"
                    " class=\"cle-texte\">certitude</strong>, non à son quantum."
                    " C'est le point où le libéralisme et l'efficacité disent la"
                    " même chose.</p>"
                    "<ul>"
                    "<li>Un inventaire des incriminations, puis l'abrogation de ce"
                    " qui relève du contrat, de la sanction administrative ou de"
                    " rien.</li>"
                    "<li>Des moyens portés au niveau européen, dans une loi de"
                    " programmation dont l'exécution est publiée.</li>"
                    "<li>Un délai de jugement opposable, et une exécution des peines"
                    " suivie comme un service public l'est ailleurs.</li>"
                    "</ul>"
                ),
            ),
            ancre="desaccord",
        ),

        section(
            "Comment on y arrive",
            gestes(
                "<strong>On compte.</strong> Un inventaire public des incriminations,"
                " des stocks d'affaires et des peines en attente, publié tous les"
                " trimestres, juridiction par juridiction. Ce qui n'est pas mesuré"
                " n'est jamais corrigé.",
                "<strong>On retire.</strong> Ce qui n'a rien à faire devant un juge"
                " pénal en sort : contraventions de pure forme, délits d'opinion,"
                " obligations sans victime. Le juge retrouve du temps pour ce qui"
                " compte, et l'État cesse de promettre ce qu'il ne peut pas tenir.",
                "<strong>On dote, et on rend des comptes.</strong> Les moyens"
                " rejoignent la médiane européenne selon une trajectoire votée, et"
                " chaque juridiction publie ses délais. Le justiciable qui subit un"
                " dépassement est indemnisé.",
            ),
            ancre="methode",
        ),

        section(
            "Ce qui ne se négocie pas",
            points((
                (
                    "L'indépendance",
                    "Le parquet est nommé et discipliné comme le siège, sur avis"
                    " conforme du Conseil supérieur de la magistrature. Une justice"
                    " que l'exécutif peut freiner n'est pas une justice.",
                ),
                (
                    "La présomption d'innocence",
                    "La détention provisoire est l'exception, la publicité de"
                    " l'enquête une atteinte, et la garde à vue un régime encadré."
                    " Une société libérale juge avant de punir, jamais l'inverse.",
                ),
                (
                    "L'égalité devant le juge",
                    "Un droit accessible suppose un juge accessible : aide"
                    " juridictionnelle revalorisée, procédures lisibles, décisions"
                    " publiées et anonymisées pour que chacun sache ce que vaut sa"
                    " cause avant d'engager des frais.",
                ),
            )),
            ancre="principes",
        ),

        suite("Lire l'état des lieux", "etat-des-lieux.html"),
    ])
