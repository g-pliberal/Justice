"""La justice civile et économique : les litiges du quotidien et des entreprises."""

from ..chiffres import fiches, valeur
from ..gabarit import (
    affiche, carte, confrontation, encadre, note, plan, section, suite,
)

TITRE = "Justice civile et économique"
DESCRIPTION = (
    "Quatorze mois pour un jugement civil, seize de plus en appel, près de six"
    " décisions prud'homales sur dix frappées d'appel : l'état de la justice des"
    " contrats et du quotidien, et la réforme libérale que nous proposons."
)


def corps() -> str:
    return "\n".join([
        affiche(
            "Le constat, puis la proposition",
            "Le droit ne vaut que ce que vaut son délai",
            "Un contrat dont l'exécution se plaide trois ans n'est pas un contrat"
            " garanti : c'est un pari. La lenteur civile n'est pas un inconfort"
            " administratif, c'est <strong class=\"cle-texte\">une taxe sur"
            " l'échange</strong> — payée d'abord par celui qui a raison.",
        ),

        plan((
            ("delais", "Les délais et leur prix"),
            ("economique", "La justice économique"),
            ("proposition", "Ce que nous proposons"),
        )),

        section(
            "Les délais et leur prix",
            "".join([
                fiches("delai_civil", "delai_appel", "delai_prudhommes",
                       "aide_juridictionnelle"),
                "<p>Le délai n'est pas neutre : il favorise systématiquement le"
                " débiteur, l'assureur qui refuse, le bailleur ou le locataire de"
                " mauvaise foi, l'entreprise qui ne paie pas. Celui qui a raison"
                " finance l'attente ; celui qui a tort l'encaisse. C'est pourquoi une"
                " justice lente est une justice injuste, avant même d'être une"
                " justice inefficace.</p>",
                "<p>Il a aussi un effet que l'on mesure mal : il détourne du juge. Le"
                " petit litige — quelques centaines ou quelques milliers d'euros — ne"
                " vaut plus la peine d'être porté, non parce qu'il est infondé, mais"
                " parce que le coût et le délai excèdent l'enjeu. Le droit existe"
                " alors sur le papier, et pas dans la vie.</p>",
                carte(
                    "<h3>Ce qui a déjà été tenté</h3>"
                    "<p>Le décret du 29 juillet 2023, pris en application de la loi de"
                    " 2023, a créé l'audience de règlement amiable et la césure du"
                    " procès civil : le juge peut convoquer les parties pour une"
                    " tentative de règlement, ou trancher d'abord le principe et"
                    " renvoyer le chiffrage. La médiation et la procédure"
                    " participative existent depuis plus de dix ans. Ces outils sont"
                    " bons ; leur emploi reste marginal, faute de temps de juge pour"
                    " les animer et d'incitation pour les parties.</p>"
                ),
            ]),
            ancre="delais",
        ),

        section(
            "La justice économique",
            "".join([
                fiches("juges_consulaires"),
                "<p>Les litiges entre entreprises sont jugés par des tribunaux de"
                " commerce composés de chefs d'entreprise élus par leurs pairs et non"
                " rémunérés — " + valeur("juges_consulaires") + " juges consulaires."
                " Ce modèle, souvent critiqué de l'extérieur, a deux qualités"
                " réelles : il est rapide, et il est rendu par des gens qui"
                " connaissent l'objet du litige.</p>",
                "<p>La loi du 20 novembre 2023 en a tiré les conséquences en créant,"
                " à titre expérimental depuis le 1<sup>er</sup> janvier 2025 et pour"
                " quatre ans, douze <em>tribunaux des activités économiques</em>, dont"
                " la compétence s'étend au-delà des seuls commerçants — professions"
                " libérales, agriculteurs, associations — pour les procédures"
                " collectives. L'expérimentation s'accompagne d'une contribution"
                " financière pour les demandeurs les plus importants.</p>",
                note(
                    "<p>Nous soutenons cette expérimentation et demandons qu'elle soit"
                    " <strong>évaluée publiquement avant d'être généralisée ou"
                    " abandonnée</strong> : délais, taux d'appel, taux d'infirmation,"
                    " coût par affaire. C'est la règle que nous appliquons à toutes"
                    " les réformes de ce programme, y compris aux nôtres.</p>",
                    genre="vigilance",
                ),
            ]),
            ancre="economique",
        ),

        section(
            "Ce que nous proposons",
            "".join([
                confrontation(
                    titre_aujourdhui="Un délai qui n'engage personne",
                    aujourdhui=(
                        "<ul>"
                        "<li>Les délais sont une statistique interne, publiée avec"
                        " retard et jamais par juridiction.</li>"
                        "<li>L'indemnisation du délai déraisonnable existe, mais il"
                        " faut la demander, la prouver et la plaider à Paris.</li>"
                        "</ul>"
                    ),
                    titre_demain="Un délai garanti et opposable",
                    demain=(
                        "<ul>"
                        "<li>Douze mois en première instance civile, six pour les"
                        " litiges simples, inscrits dans le code de l'organisation"
                        " judiciaire.</li>"
                        "<li>Au-delà, indemnisation forfaitaire de plein droit, sans"
                        " faute à prouver, imputée sur le budget du ministère et"
                        " non sur celui de la juridiction — qui n'y est pour"
                        " rien.</li>"
                        "<li>Publication trimestrielle des délais par juridiction et"
                        " par contentieux, en données ouvertes.</li>"
                        "</ul>"
                    ),
                ),
                confrontation(
                    titre_aujourdhui="Le petit litige n'a pas de juge",
                    aujourdhui=(
                        "<ul>"
                        "<li>Coût et délai excèdent l'enjeu en deçà de quelques"
                        " milliers d'euros.</li>"
                        "<li>La médiation existe mais reste marginale.</li>"
                        "<li>Obtenir une décision ne garantit pas d'être payé :"
                        " l'exécution est à la charge du créancier.</li>"
                        "</ul>"
                    ),
                    titre_demain="Une voie rapide, et une exécution qui suit",
                    demain=(
                        "<ul>"
                        "<li>Procédure simplifiée en ligne pour les litiges de faible"
                        " montant : formulaire, échange écrit, décision motivée en"
                        " quelques semaines, appel ouvert sur les seuls points de"
                        " droit.</li>"
                        "<li>Médiation préalable gratuite pour ces litiges, sans"
                        " obligation de transiger.</li>"
                        "<li>Simplification de l'exécution des titres : accès direct"
                        " du commissaire de justice aux informations de solvabilité"
                        " sous contrôle du juge, et frais à la charge du"
                        " débiteur défaillant.</li>"
                        "</ul>"
                    ),
                ),
                encadre(
                    "<h3>Les décisions doivent être publiques</h3>"
                    "<p>La loi du 23 mars 2019 a ouvert la publication en ligne de"
                    " l'ensemble des décisions de justice, pseudonymisées ; le"
                    " déploiement s'est fait par paliers, degré par degré et matière"
                    " par matière. Il doit être achevé, en accès libre et"
                    " réutilisable.</p>"
                    "<p>La raison est libérale avant d'être technique : un justiciable"
                    " qui peut savoir ce que les tribunaux décident dans des affaires"
                    " comme la sienne négocie, transige et renonce en connaissance de"
                    " cause. L'opacité des décisions profite à ceux qui plaident"
                    " souvent — administrations, assureurs, grandes entreprises —"
                    " contre ceux qui plaident une fois dans leur vie.</p>"
                ),
            ]),
            ancre="proposition",
        ),

        suite("Les libertés et les garanties", "libertes.html"),
    ])
