"""L'état des lieux : ce que la France fait aujourd'hui.

Cette page n'engage que ses sources. Elle décrit les moyens, les délais et les
textes en vigueur, sans en tirer de conclusion : la conclusion est dans les
pages suivantes, et le lecteur doit pouvoir lire celle-ci même s'il ne partage
aucune de nos idées.
"""

from ..chiffres import fiches, valeur
from ..gabarit import (
    affiche, barres, carte, encadre, note, plan, section, suite,
)

TITRE = "État des lieux"
DESCRIPTION = (
    "Combien la France dépense pour sa justice, combien elle emploie de"
    " magistrats, combien de temps elle met à juger, et quels textes régissent"
    " tout cela depuis 2019. Chiffres sourcés et datés, sans commentaire."
)


def corps() -> str:
    return "\n".join([
        affiche(
            "Le constat",
            "Une institution pauvre, lente, et dont la loi change tous les deux ans",
            "La justice française coûte <strong class=\"cle-texte\">environ 0,35 %"
            " du PIB</strong>, emploie deux fois moins de juges par habitant que la"
            " médiane européenne et six fois moins de procureurs. Voici ce que les"
            " sources publiques permettent d'établir, avant toute opinion.",
        ),

        note(
            "<p>Tout ce qui suit est une description de l'existant. Les chiffres"
            " sont arrondis et liés à leur source ; les textes sont cités par leur"
            " numéro et leur date. Notre proposition commence"
            " <a href=\"programme.html\">ailleurs</a>, et n'est jamais mêlée à un"
            " paragraphe de constat.</p>",
            genre="resume",
        ),

        plan((
            ("moyens", "Les moyens"),
            ("europe", "La comparaison européenne"),
            ("delais", "Les délais"),
            ("droit", "Ce que la loi a fait depuis 2019"),
            ("confiance", "La confiance"),
        )),

        section(
            "Les moyens",
            "".join([
                fiches("budget", "part_pib", "magistrats", "aide_juridictionnelle"),
                "<p>Le budget de la mission « Justice » couvre trois mondes très"
                " différents : les juridictions, l'administration pénitentiaire —"
                " qui en absorbe à elle seule une part considérable — et la"
                " protection judiciaire de la jeunesse. La loi de programmation du"
                " 20 novembre 2023 prévoit de le porter à " + valeur("budget_cible")
                + " en 2027, avec " + valeur("recrutements") + " et 1 800 greffiers"
                " recrutés sur la période.</p>",
                "<p>Deux réserves s'imposent sur cette trajectoire. D'abord, une"
                " promesse de recrutement n'est pas une promesse d'effectifs : les"
                " départs en retraite et les démissions s'en déduisent. Ensuite, un"
                " magistrat recruté aujourd'hui juge dans trois ans — le délai de"
                " formation à l'École nationale de la magistrature est incompressible,"
                " et aucune loi de finances ne le raccourcit.</p>",
            ]),
            ancre="moyens",
        ),

        section(
            "La comparaison européenne",
            "".join([
                "<p>La CEPEJ, organe du Conseil de l'Europe, compte les magistrats"
                " des États membres sur des définitions communes. C'est la seule"
                " comparaison qui vaille : elle ne compare pas des budgets"
                " nationaux, mais des effectifs rapportés à la population.</p>",
                barres(
                    (
                        ("France", 11.1, "11,1", True),
                        ("Médiane du Conseil de l'Europe", 17.6, "17,6", False),
                        ("Allemagne", 24.5, "environ 25", False),
                    ),
                    legende="Juges professionnels pour 100 000 habitants, données"
                            " 2022. Source : CEPEJ, rapport d'évaluation des"
                            " systèmes judiciaires européens.",
                ),
                barres(
                    (
                        ("France", 3.2, "3,2", True),
                        ("Médiane du Conseil de l'Europe", 11.1, "11,1", False),
                    ),
                    legende="Procureurs pour 100 000 habitants, données 2022."
                            " Source : CEPEJ. L'écart est ici le plus large de tout"
                            " le tableau européen, et il porte sur la fonction qui"
                            " décide des suites données à une plainte.",
                ),
                note(
                    "<p><strong>Une comparaison n'est pas un verdict.</strong> Les"
                    " systèmes judiciaires ne se superposent pas : l'Allemagne confie"
                    " au juge des tâches que la France confie au notaire, à l'huissier"
                    " ou au greffe, et les juges consulaires et prud'homaux français —"
                    " non professionnels — ne sont pas comptés dans ces barres. Ces"
                    " écarts expliquent une partie de la différence. Ils n'expliquent"
                    " pas qu'elle atteigne un facteur trois sur les procureurs.</p>",
                    genre="vigilance",
                ),
            ]),
            ancre="europe",
        ),

        section(
            "Les délais",
            "".join([
                fiches("delai_civil", "delai_appel", "delai_prudhommes",
                       "delai_instruction"),
                "<p>Ces moyennes additionnent des contentieux sans rapport : un"
                " divorce par consentement mutuel et une succession disputée"
                " comptent pour un dans la même statistique. Elles disent pourtant"
                " quelque chose de simple — un justiciable français qui saisit un"
                " juge en première instance, puis fait appel, attend couramment"
                " <strong class=\"cle-texte\">deux à trois ans</strong> une décision"
                " définitive.</p>",
                carte(
                    "<h3>Ce que le droit prévoit déjà</h3>"
                    "<p>L'article L. 141-1 du code de l'organisation judiciaire rend"
                    " l'État responsable du « fonctionnement défectueux du service de"
                    " la justice », et le délai déraisonnable en fait partie : des"
                    " justiciables obtiennent régulièrement une indemnisation à ce"
                    " titre. Mais la charge de la démonstration leur revient, l'action"
                    " se porte devant le tribunal judiciaire de Paris, et son existence"
                    " même est ignorée de la quasi-totalité de ceux qui pourraient s'en"
                    " prévaloir. Le droit existe ; il n'est pas praticable.</p>"
                ),
            ]),
            ancre="delais",
        ),

        section(
            "Ce que la loi a fait depuis 2019",
            "".join([
                "<p>Cinq textes structurent la justice telle qu'elle fonctionne"
                " aujourd'hui. Les citer ensemble montre la cadence : trois réformes"
                " d'organisation en six ans, chacune avant que la précédente ait pu"
                " être évaluée.</p>",
                encadre(
                    "<h3>Les cinq textes qui font le droit en vigueur</h3>"
                    "<dl class=\"gloses\">"
                    "<dt>Loi n° 2019-222 du 23 mars 2019, de programmation 2018-2022"
                    " et de réforme pour la justice</dt>"
                    "<dd>Fusion du tribunal d'instance et du tribunal de grande"
                    " instance en tribunal judiciaire ; refonte de l'échelle des"
                    " peines — le « bloc peines » — avec interdiction de principe des"
                    " peines d'emprisonnement ferme de moins d'un mois ; ouverture de"
                    " la publication en ligne de l'ensemble des décisions de"
                    " justice.</dd>"
                    "<dt>Code de la justice pénale des mineurs, en vigueur depuis le"
                    " 30 septembre 2021</dt>"
                    "<dd>Remplace l'ordonnance du 2 février 1945. Procédure en deux"
                    " temps : la culpabilité est jugée d'abord, la sanction quelques"
                    " mois plus tard, après une période de mise à l'épreuve"
                    " éducative.</dd>"
                    "<dt>Loi n° 2021-1729 du 22 décembre 2021 pour la confiance dans"
                    " l'institution judiciaire</dt>"
                    "<dd>Enregistrement et diffusion d'audiences, encadrement du"
                    " secret de l'enquête, généralisation des cours criminelles"
                    " départementales — qui jugent les crimes punis de quinze à vingt"
                    " ans sans jury populaire —, refonte des réductions de peine.</dd>"
                    "<dt>États généraux de la justice, rapport de juillet 2022</dt>"
                    "<dd>Le comité présidé par Jean-Marc Sauvé conclut à un état de"
                    " « délabrement » et recommande un effort budgétaire pluriannuel"
                    " massif. C'est le diagnostic officiel le plus sévère jamais rendu"
                    " sur l'institution, et il est rendu par elle-même.</dd>"
                    "<dt>Lois du 20 novembre 2023, organique n° 2023-1058 et ordinaire"
                    " n° 2023-1059</dt>"
                    "<dd>Programmation budgétaire 2023-2027, nouvelles voies de"
                    " recrutement des magistrats, création à titre expérimental des"
                    " tribunaux des activités économiques, simplification de la"
                    " procédure civile.</dd>"
                    "</dl>"
                ),
                "<p>S'y ajoute ce qui ne passe pas par la loi : la politique pénale"
                " est conduite par circulaires du garde des Sceaux, en application de"
                " l'article 30 du code de procédure pénale, qui autorise les"
                " instructions générales et interdit depuis 2013 les instructions"
                " individuelles dans les affaires en cours.</p>",
            ]),
            ancre="droit",
        ),

        section(
            "La confiance",
            "".join([
                fiches("confiance", "recidive", "reponse_penale",
                       "classement_auteur"),
                "<p>Ces quatre chiffres se lisent ensemble. Près de neuf affaires"
                " poursuivables sur dix reçoivent une réponse pénale — le taux est"
                " élevé, et il est sincère. Mais il ne porte que sur les affaires où"
                " un auteur a été identifié, c'est-à-dire une minorité des plaintes"
                " déposées. Pour la victime d'un cambriolage dont l'auteur n'a jamais"
                " été retrouvé, un taux de réponse pénale de 90 % décrit un monde"
                " qu'elle ne reconnaît pas.</p>",
                "<p>Quant à la récidive, l'étude de référence — "
                + valeur("recidive") + " de recondamnation dans les cinq ans après"
                " une sortie de prison — date de 2011 et n'a pas été reconduite sur"
                " une cohorte plus récente. Une politique publique qui ne mesure plus"
                " son principal indicateur de résultat ne peut ni se corriger ni se"
                " défendre.</p>",
            ]),
            ancre="confiance",
        ),

        suite("La justice pénale", "penale.html"),
    ])
