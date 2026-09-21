"""La justice pénale : ce qu'on punit, et ce qu'on exécute."""

from ..chiffres import fiches, valeur
from ..gabarit import (
    affiche, carte, confrontation, encadre, note, plan, section, suite,
)

TITRE = "Justice pénale"
DESCRIPTION = (
    "Plus de 10 000 infractions en vigueur, des dizaines de milliers de peines"
    " prononcées et non exécutées : l'état du droit pénal français, et la"
    " réforme libérale — punir moins de choses, et les punir sûrement."
)


def corps() -> str:
    return "\n".join([
        affiche(
            "Le constat, puis la proposition",
            "Prononcer moins, exécuter tout",
            "Le droit pénal français promet énormément et tient peu. Il crée des"
            " infractions plus vite qu'il ne juge, et laisse dormir les peines qu'il"
            " prononce. Nous proposons l'inverse : <strong class=\"cle-texte\">un"
            " champ pénal réduit, et une exécution certaine</strong>.",
        ),

        plan((
            ("inflation", "L'inflation pénale"),
            ("execution", "L'exécution des peines"),
            ("proposition", "Ce que nous proposons"),
        )),

        section(
            "L'inflation pénale",
            "".join([
                fiches("incriminations", "reponse_penale", "classement_auteur",
                       "delai_instruction"),
                "<p>Personne ne sait combien d'infractions sont en vigueur en France."
                " Les estimations courantes dépassent dix mille, réparties entre le"
                " code pénal et des dizaines d'autres codes — la santé publique,"
                " l'environnement, la consommation, les transports, l'urbanisme. Le"
                " ministère lui-même ne publie pas d'inventaire. C'est un fait qui"
                " devrait suffire : une société dont nul ne peut connaître la loi"
                " pénale a cessé de remplir la première condition de l'État de"
                " droit.</p>",
                "<p>Cette inflation a une mécanique connue. Un fait divers survient,"
                " une proposition de loi suit, une incrimination nouvelle est votée —"
                " souvent redondante avec une incrimination existante — et les moyens"
                " de la mettre en œuvre ne suivent jamais. Le législateur légifère"
                " parce que c'est ce qu'il peut faire, et non parce que c'est ce qui"
                " manque.</p>",
                note(
                    "<p><strong>Ce n'est pas un plaidoyer pour l'impunité.</strong>"
                    " Les atteintes aux personnes, aux biens et aux libertés doivent"
                    " être poursuivies avec plus de constance qu'aujourd'hui. Réduire"
                    " le champ pénal, c'est rendre du temps de juge, de procureur et"
                    " d'enquêteur à ce qui le mérite : un policier qui dresse un"
                    " procès-verbal pour une obligation déclarative n'est pas sur une"
                    " enquête de cambriolage.</p>",
                    genre="vigilance",
                ),
            ]),
            ancre="inflation",
        ),

        section(
            "L'exécution des peines",
            "".join([
                fiches("peines_attente", "recidive", "cout_detention"),
                "<p>Une peine prononcée n'est pas une peine exécutée. Entre le"
                " prononcé et la mise à exécution s'intercalent l'appel, la"
                " signification, la convocation devant le juge de l'application des"
                " peines, l'aménagement éventuel, puis l'exécution elle-même — une"
                " chaîne où chaque maillon a ses délais propres et où le stock"
                " s'accumule. La Cour des comptes et les rapporteurs budgétaires du"
                " Parlement relèvent régulièrement " + valeur("peines_attente") + " de"
                " peines d'emprisonnement ferme en attente.</p>",
                "<p>Le ministère ne publie pas de série continue de ce stock. C'est"
                " l'indicateur le plus important de la chaîne pénale, et c'est celui"
                " qu'on ne trouve pas.</p>",
                carte(
                    "<h3>Pourquoi la certitude bat la sévérité</h3>"
                    "<p>La littérature criminologique est constante sur ce point : ce"
                    " qui dissuade, c'est la probabilité d'être pris et sanctionné,"
                    " beaucoup plus que le quantum encouru. Une peine de six mois"
                    " exécutée dans le mois produit plus d'effet qu'une peine de deux"
                    " ans mise à exécution deux ans plus tard — et coûte moins cher.</p>"
                    "<p>C'est aussi une exigence libérale, et pas seulement une"
                    " considération d'efficacité : une peine incertaine est une peine"
                    " arbitraire. Celui qui la subit ne sait pas ce qu'il encourt ;"
                    " celui qui y échappe le doit au hasard d'un greffe.</p>"
                ),
            ]),
            ancre="execution",
        ),

        section(
            "Ce que nous proposons",
            "".join([
                confrontation(
                    titre_aujourdhui="Un champ pénal qui s'étend sans inventaire",
                    aujourdhui=(
                        "<ul>"
                        "<li>Aucune administration ne tient le compte des"
                        " incriminations en vigueur.</li>"
                        "<li>Des manquements purement administratifs — déclarations,"
                        " formalités, seuils — sont assortis de peines"
                        " correctionnelles.</li>"
                        "<li>Chaque loi nouvelle ajoute, aucune ne retranche.</li>"
                        "</ul>"
                    ),
                    titre_demain="Un inventaire, puis une règle de compensation",
                    demain=(
                        "<ul>"
                        "<li>Inventaire public et exhaustif des incriminations, publié"
                        " et tenu à jour par le ministère de la Justice.</li>"
                        "<li>Déclassement en sanction administrative ou en"
                        " responsabilité civile de ce qui ne porte atteinte ni aux"
                        " personnes, ni aux biens, ni aux libertés.</li>"
                        "<li>Règle organique : aucune incrimination nouvelle sans"
                        " abrogation d'une incrimination existante.</li>"
                        "</ul>"
                    ),
                ),
                confrontation(
                    titre_aujourdhui="Des peines prononcées puis oubliées",
                    aujourdhui=(
                        "<ul>"
                        "<li>Un stock de peines fermes non exécutées que l'État ne"
                        " publie pas.</li>"
                        "<li>Des mois, parfois des années, entre le prononcé et"
                        " l'exécution.</li>"
                        "<li>Un effet dévastateur sur la confiance : la victime"
                        " apprend que rien n'a suivi.</li>"
                        "</ul>"
                    ),
                    titre_demain="Quatre-vingt-dix jours, et une publication",
                    demain=(
                        "<ul>"
                        "<li>Délai maximal de 90 jours entre la décision définitive et"
                        " la mise à exécution, inscrit dans le code de procédure"
                        " pénale.</li>"
                        "<li>Publication trimestrielle du stock et des délais, par"
                        " juridiction — ce qui se publie se corrige.</li>"
                        "<li>Généralisation du bureau de l'exécution des peines : la"
                        " convocation est remise à l'issue de l'audience, pas des mois"
                        " plus tard par courrier.</li>"
                        "<li>Plan d'extinction du stock existant en cinq ans, avec"
                        " revue annuelle devant le Parlement.</li>"
                        "</ul>"
                    ),
                ),
                encadre(
                    "<h3>Ce que nous ne proposons pas</h3>"
                    "<p>Ni peines planchers automatiques, ni suppression des"
                    " aménagements de peine. Les premières retirent au juge"
                    " l'appréciation de l'espèce, qui est sa fonction même ; les"
                    " seconds sont, pour les courtes peines, la seule manière connue"
                    " de réduire la récidive. Ce que nous voulons supprimer, ce n'est"
                    " pas l'aménagement : c'est le délai, l'incertitude, et la"
                    " part de hasard.</p>"
                ),
            ]),
            ancre="proposition",
        ),

        suite("La prison et les peines", "prison.html"),
    ])
