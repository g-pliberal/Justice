"""Les libertés : l'indépendance du juge, et ce qui protège le justiciable."""

from ..gabarit import (
    affiche, carte, confrontation, encadre, note, plan, points, section, suite,
)

TITRE = "Libertés et garanties"
DESCRIPTION = (
    "Indépendance du parquet, détention provisoire, présomption d'innocence,"
    " surveillance : ce que le droit français garantit aujourd'hui, et les"
    " garanties que nous proposons d'ajouter."
)


def corps() -> str:
    return "\n".join([
        affiche(
            "Le constat, puis la proposition",
            "Une justice indépendante, ou rien de ce qui précède",
            "Tout ce que ce site propose — des délais tenus, des peines exécutées,"
            " des moyens accrus — suppose une institution que le pouvoir ne peut ni"
            " freiner ni orienter. <strong class=\"cle-texte\">Une justice efficace"
            " et dépendante serait pire qu'une justice lente</strong>, et c'est"
            " pourquoi cette page-ci vient avant le programme.",
        ),

        plan((
            ("parquet", "Le statut du parquet"),
            ("procedure", "Avant le jugement"),
            ("surveillance", "La surveillance et les données"),
            ("proposition", "Ce que nous proposons"),
        )),

        section(
            "Le statut du parquet",
            "".join([
                "<p>Les magistrats du parquet — les procureurs — sont des magistrats,"
                " mais leur carrière ne relève pas du même régime que celle des juges"
                " du siège. Le Conseil supérieur de la magistrature rend sur leur"
                " nomination un avis <em>simple</em>, que le garde des Sceaux suit en"
                " pratique mais n'est pas tenu de suivre en droit ; le pouvoir"
                " disciplinaire à leur égard appartient au ministre, sur avis du"
                " CSM.</p>",
                "<p>La loi du 25 juillet 2013 a interdit les instructions"
                " individuelles du ministre dans les affaires en cours, et inscrit"
                " dans l'article 30 du code de procédure pénale que sa compétence se"
                " limite aux instructions générales de politique pénale. C'est un"
                " progrès réel. Il reste que la Cour européenne des droits de l'homme"
                " juge de longue date que le parquet français ne présente pas les"
                " garanties d'indépendance nécessaires pour être regardé comme une"
                " « autorité judiciaire » au sens de la Convention — ce qui a des"
                " conséquences concrètes, notamment sur le contrôle de la garde à"
                " vue.</p>",
                "<p>Plusieurs projets de révision constitutionnelle ont prévu de"
                " soumettre les nominations du parquet à l'avis conforme du CSM et de"
                " lui transférer la discipline. Aucun n'a été mené à son terme, faute"
                " de réunion du Congrès. Le sujet n'est pas technique : il est"
                " simplement inachevé depuis trente ans.</p>",
                note(
                    "<p><strong>Ce qui se joue, très concrètement :</strong> c'est le"
                    " procureur qui décide de poursuivre ou de classer, d'ouvrir une"
                    " enquête préliminaire, de la laisser dormir, de requérir ou non"
                    " la détention. Qu'il soit nommé par un ministre suffit à rendre"
                    " chacune de ces décisions discutable, y compris lorsqu'elle est"
                    " parfaitement fondée. L'indépendance protège autant le magistrat"
                    " que le justiciable.</p>",
                    genre="vigilance",
                ),
            ]),
            ancre="parquet",
        ),

        section(
            "Avant le jugement",
            "".join([
                points((
                    (
                        "La détention provisoire",
                        "Une part importante des personnes détenues en France n'a pas"
                        " été jugée. La détention provisoire est décidée par le juge"
                        " des libertés et de la détention, sur réquisitions du"
                        " parquet, et sa durée se prolonge au rythme des"
                        " renouvellements. Elle doit rester l'exception motivée"
                        " qu'elle est en droit.",
                    ),
                    (
                        "La garde à vue",
                        "L'avocat y est présent depuis 2011 et le droit au silence"
                        " notifié, mais le contrôle de la mesure relève du procureur,"
                        " partie poursuivante. C'est ce point précis que la Cour"
                        " européenne des droits de l'homme critique.",
                    ),
                    (
                        "La présomption d'innocence",
                        "La loi du 22 décembre 2021 a encadré le secret de l'enquête"
                        " et permis au procureur de communiquer pour rétablir des"
                        " faits. Les fuites, elles, restent rarement sanctionnées, et"
                        " une mise en examen médiatisée équivaut souvent à une"
                        " condamnation sociale.",
                    ),
                )),
                carte(
                    "<h3>La procédure n'est pas un formalisme</h3>"
                    "<p>Chaque garantie procédurale a été arrachée à la suite d'une"
                    " erreur judiciaire ou d'un abus. Les présenter comme des"
                    " lourdeurs dont il faudrait alléger les enquêteurs est le"
                    " raisonnement le plus constant des quarante dernières années de"
                    " législation pénale, et c'est celui auquel nous nous opposons"
                    " le plus fermement.</p>"
                    "<p>Une procédure protège d'abord l'innocent. Celui qui est"
                    " coupable et bien défendu sera condamné quand même ; celui qui"
                    " est innocent et mal défendu ne sera sauvé que par la"
                    " procédure.</p>"
                ),
            ]),
            ancre="procedure",
        ),

        section(
            "La surveillance et les données",
            "".join([
                "<p>Le droit français a autorisé ces dernières années des techniques"
                " que l'on aurait jugées inconcevables il y a vingt ans : captation de"
                " données à distance, conservation généralisée de données de connexion"
                " sous conditions, expérimentation du traitement algorithmique"
                " d'images de vidéoprotection, autorisée par la loi du 19 mai 2023"
                " relative aux Jeux olympiques et paralympiques de 2024 puis"
                " prolongée. Chacune de ces mesures a été présentée comme temporaire,"
                " exceptionnelle et strictement encadrée.</p>",
                "<p>C'est le point où le libéralisme se distingue le plus nettement"
                " des autres familles politiques : nous ne jugeons pas ces"
                " dispositifs sur l'intention de ceux qui les demandent, mais sur ce"
                " qu'ils permettront à un gouvernement futur qui ne partagerait pas"
                " cette intention. Une capacité de surveillance installée ne se"
                " désinstalle pas.</p>",
                encadre(
                    "<h3>Trois règles que nous voulons voir appliquées à toute"
                    " technique nouvelle</h3>"
                    "<ol class=\"serree\">"
                    "<li><strong>Autorisation préalable par un juge du siège</strong>,"
                    " et non par une autorité administrative ou par le parquet, pour"
                    " toute mesure attentatoire à la vie privée.</li>"
                    "<li><strong>Extinction automatique</strong> : toute"
                    " expérimentation prend fin de plein droit à son terme, et sa"
                    " reconduction suppose une évaluation publique et indépendante"
                    " remise avant le vote.</li>"
                    "<li><strong>Information de la personne surveillée</strong> une"
                    " fois la mesure achevée et l'enquête close, sauf décision"
                    " motivée du juge. Une surveillance dont on n'apprend jamais"
                    " l'existence ne peut pas être contestée.</li>"
                    "</ol>"
                ),
            ]),
            ancre="surveillance",
        ),

        section(
            "Ce que nous proposons",
            confrontation(
                titre_aujourdhui="Une indépendance partielle et un contrôle interne",
                aujourdhui=(
                    "<ul>"
                    "<li>Nomination des procureurs sur avis simple du CSM ; discipline"
                    " exercée par le ministre.</li>"
                    "<li>Contrôle de la garde à vue confié au parquet.</li>"
                    "<li>Budget des juridictions arbitré dans une enveloppe"
                    " ministérielle, sans visibilité publique par juridiction.</li>"
                    "</ul>"
                ),
                titre_demain="Une indépendance achevée, et un budget lisible",
                demain=(
                    "<ul>"
                    "<li>Révision constitutionnelle : nomination des magistrats du"
                    " parquet sur avis conforme du CSM, discipline transférée au"
                    " CSM.</li>"
                    "<li>Contrôle des mesures privatives de liberté confié au juge du"
                    " siège, conformément à la jurisprudence européenne.</li>"
                    "<li>Publication du budget et des effectifs réels par juridiction,"
                    " et rapport annuel d'exécution de la loi de programmation débattu"
                    " au Parlement.</li>"
                    "</ul>"
                ),
            ),
            ancre="proposition",
        ),

        suite("Le programme en vingt mesures", "programme.html"),
    ])
