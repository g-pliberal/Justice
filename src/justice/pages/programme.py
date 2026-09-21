"""Le programme : vingt mesures, leur véhicule, leur coût et leur objection.

Chaque mesure porte quatre mentions obligatoires : par quel texte elle se
prend, ce qu'elle pèse, la meilleure objection qu'on lui fasse et ce que nous
y répondons. Une mesure dont on ne sait dire ni l'une ni l'autre n'est pas une
mesure, et un test refuse de construire la page sans elles.

Le chiffrage n'est pas écrit à côté des mesures : il est **calculé à partir
d'elles**. Chaque mesure déclare son coût en millions d'euros par an à terme,
chaque poste du tableau final est la somme des mesures qui lui sont affectées,
et un test vérifie que les vingt mesures sont affectées à un poste et à un
seul. Il n'est donc pas possible d'annoncer un total qui ne soit pas la somme
de ce qu'on a promis — c'était le cas de la version précédente de cette page,
dont les mesures additionnées dépassaient de près d'un milliard le total
affiché.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..chiffres import CHIFFRES, valeur
from ..gabarit import (
    affiche, encadre, mesure, mesures, note, plan, section, suite, tableau,
)

TITRE = "Le programme"
DESCRIPTION = (
    "Vingt mesures pour la justice : rejoindre la médiane européenne de"
    " magistrats, garantir les délais, exécuter les peines en 90 jours, réduire"
    " le champ pénal et achever l'indépendance du parquet. Avec le véhicule"
    " juridique, le coût et l'objection de chacune."
)


@dataclass(frozen=True)
class Cout:
    """Ce qu'une mesure pèse, en millions d'euros.

    ``recurrent`` est la dépense annuelle une fois la trajectoire parcourue :
    c'est elle, et elle seule, qui entre dans le total. ``transitoire`` est une
    dépense annuelle qui s'éteint (un plan d'apurement), ``investissement`` une
    dépense faite une fois. Les deux dernières sont dites à part, parce que les
    confondre avec la première est la manière la plus courante de faire passer
    un programme pour moins cher qu'il n'est.
    """

    recurrent: float
    libelle: str
    transitoire: float = 0.0
    investissement: float = 0.0


#: Le coût de chaque mesure, par son rang. En millions d'euros courants 2026.
COUTS: dict[int, Cout] = {
    1: Cout(1100, "1,1 Md€ par an à terme"),
    2: Cout(80, "environ 80 M€ par an"),
    3: Cout(900, "0,9 Md€ par an à terme"),
    4: Cout(5, "moins de 5 M€ par an"),
    5: Cout(5, "moins de 5 M€ par an"),
    6: Cout(0, "nul"),
    7: Cout(0, "économie nette, non comptée dans le total"),
    8: Cout(0, "nul"),
    9: Cout(250, "environ 250 M€ par an"),
    10: Cout(0, "compris dans la mesure 9"),
    11: Cout(0, "150 M€ par an pendant cinq ans, puis nul", transitoire=150),
    12: Cout(5, "moins de 5 M€ par an"),
    13: Cout(0, "nul"),
    14: Cout(800, "environ 800 M€ par an d'investissement"),
    15: Cout(100, "100 M€ par an, partiellement compensés"),
    16: Cout(50, "environ 50 M€ par an, décroissants"),
    17: Cout(0, "50 M€ une fois, puis économie nette", investissement=50),
    18: Cout(0, "30 M€ une fois", investissement=30),
    19: Cout(0, "nul"),
    20: Cout(20, "moins de 20 M€ par an"),
}

#: Les postes du chiffrage, et les mesures qui les composent. Chaque mesure
#: figure dans un poste et un seul : c'est ce qui fait du tableau final une
#: somme et non une affirmation.
POSTES: tuple[tuple[str, str, tuple[int, ...]], ...] = (
    ("Magistrats", "environ +9 900 postes", (1,)),
    ("Greffe et équipe autour du magistrat", "environ +13 000 postes", (3,)),
    ("Formation et recrutement", "écoles portées au triple", (2,)),
    ("Statistique, publication, ouverture des données", "—", (4, 5, 12, 18)),
    ("Exécution des peines", "—", (9, 10, 11)),
    ("Prison : places et activité", "environ +30 000 places en dix ans", (13, 14, 15)),
    ("Garanties, délais, libertés", "—", (16, 17, 19, 20)),
    ("Réduction du champ pénal", "sans effet budgétaire compté", (6, 7, 8)),
)

#: Le budget de la mission « Justice » aujourd'hui, hors pensions, en M€.
BUDGET_ACTUEL = 10629
#: Le produit intérieur brut, en M€, qui sert de dénominateur à la part de PIB.
PIB = 2991100


def total_recurrent() -> float:
    """Le coût annuel du programme à terme : la somme de ses mesures."""
    return sum(cout.recurrent for cout in COUTS.values())


def total_poste(rangs: tuple[int, ...]) -> float:
    return sum(COUTS[rang].recurrent for rang in rangs)


def _md(millions: float) -> str:
    """Des millions en milliards, à la décimale, à la française."""
    return f"{millions / 1000:.1f}".replace(".", ",")


def _lignes_du_chiffrage() -> tuple[tuple[str, ...], ...]:
    lignes = [
        (poste, volume, f"{_md(total_poste(rangs))} Md€")
        for poste, volume, rangs in POSTES
    ]
    lignes.append((
        "<strong>Total</strong>", "—",
        f"<strong>{_md(total_recurrent())} Md€</strong>",
    ))
    return tuple(lignes)


def corps() -> str:
    budget_final = BUDGET_ACTUEL + total_recurrent()
    part_pib = f"{100 * budget_final / PIB:.2f}".replace(".", ",")
    transitoire = sum(c.transitoire for c in COUTS.values())
    investissement = sum(c.investissement for c in COUTS.values())

    return "\n".join([
        affiche(
            "La proposition",
            "Vingt mesures, leur texte, leur prix et leur objection",
            "Un programme qui ne dit pas par quelle loi il passe ni ce qu'il coûte"
            " est un tract. Chacune des vingt mesures ci-dessous porte donc son"
            " <strong class=\"cle-texte\">véhicule juridique</strong>, son"
            " <strong class=\"cle-texte\">ordre de grandeur budgétaire</strong> et"
            " <strong class=\"cle-texte\">la meilleure objection</strong> que nous"
            " lui connaissions, avec ce que nous y répondons. Le chiffrage de fin"
            " de page est la somme de ces mesures, et rien d'autre.",
        ),

        plan((
            ("moyens", "Les moyens"),
            ("champ", "Le champ pénal"),
            ("execution", "L'exécution des peines"),
            ("prison", "La prison"),
            ("civil", "La justice civile"),
            ("libertes", "Les libertés"),
            ("chiffrage", "Le chiffrage"),
            ("absences", "Ce que ce programme ne dit pas"),
        )),

        section("Les moyens", mesures(
            mesure(
                1, "Une loi de programmation décennale, et non quinquennale",
                "<p>Trajectoire d'effectifs votée pour dix ans, avec pour cible la"
                " médiane européenne : 17,6 juges et 11,1 procureurs pour"
                " 100 000 habitants, soit environ 19 700 magistrats contre 9 800"
                " aujourd'hui. Le rythme est contraint par la formation, pas par le"
                " budget : c'est pourquoi l'horizon est décennal et non"
                " quinquennal.</p>",
                porte="Loi de programmation", cout=COUTS[1].libelle,
                objection="Aucune législature n'engage la suivante. Une trajectoire"
                " à dix ans sera abandonnée à la première alternance, comme l'ont"
                " été les lois de programmation précédentes.",
                reponse="C'est exact, et nous ne prétendons pas le contraire : une"
                " loi de programmation n'a pas de valeur supérieure aux lois de"
                " finances qui la démentent. Ce qu'elle produit est un point de"
                " comparaison public et annuel, et c'est la raison d'être de la"
                " mesure 4. On n'empêche pas un gouvernement de renoncer ; on"
                " l'oblige à renoncer devant tout le monde.",
            ),
            mesure(
                2, "Tripler les capacités de formation, et ouvrir les voies latérales",
                "<p>Atteindre la cible suppose près de 1 000 magistrats nets par an"
                " pendant dix ans ; départs déduits, c'est de l'ordre de 1 300 à"
                " 1 400 recrutements annuels, contre 400 à 550 aujourd'hui. Doubler"
                " les écoles n'y suffit pas : il faut les tripler, et élargir le"
                " recrutement aux avocats, juristes d'entreprise et universitaires"
                " expérimentés, avec formation probatoire et évaluation par le"
                " jury — sans abaisser l'exigence d'entrée.</p>",
                porte="Loi organique et décrets", cout=COUTS[2].libelle,
                objection="On n'improvise pas des magistrats. Tripler les promotions"
                " en dix ans revient à recruter au rabais, et la justice paiera"
                " pendant quarante ans la qualité de ces promotions-là.",
                reponse="Le concours reste le concours et le jury reste souverain :"
                " nous ne touchons ni à l'un ni à l'autre, et nous proposons de"
                " publier chaque année le taux de sélection, précisément pour que"
                " l'on voie si l'exigence baisse. Si le vivier ne suit pas, c'est la"
                " trajectoire qui s'allonge, pas le niveau qui descend — et nous"
                " préférons le dire maintenant.",
            ),
            mesure(
                3, "Une équipe autour de chaque magistrat",
                "<p>Un greffier par magistrat, et des juristes assistants en nombre"
                " suffisant pour préparer les dossiers. Un juge qui rédige ses propres"
                " convocations est un juge qui ne juge pas : c'est la réforme la moins"
                " visible et la plus rentable du programme.</p>",
                porte="Loi de finances", cout=COUTS[3].libelle,
                objection="Les juristes assistants existent déjà, et leur effet sur"
                " les délais n'a jamais été démontré. Vous dépensez 0,9 Md€ par an"
                " sur une intuition.",
                reponse="L'effet n'a jamais été démontré parce qu'il n'a jamais été"
                " mesuré : aucune donnée publique ne relie l'équipe d'un magistrat au"
                " délai de ses dossiers. La mesure 4 produit cette donnée, et nous"
                " acceptons d'être jugés dessus. Nous assumons entre-temps un pari"
                " documenté : les systèmes européens qui jugent plus vite que nous"
                " confient au greffe des tâches que nous laissons au juge.",
            ),
            mesure(
                4, "Publier, tous les trimestres, ce que chaque juridiction fait",
                "<p>Délais moyens et médians, stocks, effectifs réels, taux d'appel et"
                " d'infirmation, par juridiction et par contentieux, en données"
                " ouvertes et réutilisables. Sans publication, aucune des mesures"
                " suivantes n'est vérifiable.</p>",
                porte="Décret", cout=COUTS[4].libelle,
                objection="Publier les performances juridiction par juridiction met"
                " les tribunaux en concurrence, pousse au chiffre contre la qualité,"
                " et prépare la notation des juges.",
                reponse="Par juridiction et par contentieux, jamais par magistrat."
                " L'article 33 de la loi du 23 mars 2019 interdit le profilage des"
                " magistrats et nous ne proposons pas de l'abroger. Publier le délai"
                " moyen d'une cour d'appel n'est pas noter un conseiller ; c'est"
                " rendre compte de l'emploi d'un budget public, ce que fait déjà"
                " chaque hôpital et chaque université.",
            ),
        ), ancre="moyens"),

        section("Le champ pénal", mesures(
            mesure(
                5, "Inventorier les incriminations",
                "<p>Recensement exhaustif et public des infractions en vigueur, tous"
                " codes confondus, tenu à jour et publié. L'inventaire précède la"
                " réforme : on ne réduit pas ce qu'on n'a pas compté. C'est aussi la"
                " seule manière de sourcer un jour le seul chiffre de ce site que"
                " nous ne savons pas sourcer.</p>",
                porte="Décret et rapport annuel au Parlement", cout=COUTS[5].libelle,
                objection="Un inventaire est un exercice bureaucratique coûteux dont"
                " personne ne se servira, et qui sera périmé le jour de sa"
                " publication.",
                reponse="Il coûte quelques millions, soit le prix d'une demi-journée"
                " de détention nationale, et il est la condition d'application de la"
                " mesure 6 : on ne compense pas ce qu'on n'a pas compté. Quant à la"
                " péremption, c'est un argument pour le tenir à jour en continu, ce"
                " que la mesure prévoit, pas pour renoncer à le faire.",
            ),
            mesure(
                6, "Aucune incrimination nouvelle sans abrogation",
                "<p>Règle de compensation portée par l'étude d'impact : aucun projet"
                " de loi créant une infraction n'est recevable sans le tableau des"
                " incriminations qu'il abroge en regard, ou sans une motivation"
                " spéciale du Gouvernement. La contrainte est procédurale et"
                " s'exerce devant la conférence des présidents.</p>",
                porte="Loi organique relative aux études d'impact (art. 39 de la"
                     " Constitution)",
                cout=COUTS[6].libelle,
                objection="Le législateur ne peut pas se lier lui-même, et le domaine"
                " de la loi organique se limite à ce que la Constitution y renvoie :"
                " une telle règle serait déclassée ou privée d'effet.",
                reponse="L'objection est juste, et elle nous a fait changer de"
                " véhicule : la version précédente de ce programme rangeait cette"
                " mesure en « loi organique » tout court, ce qui était une erreur de"
                " droit. L'article 39 de la Constitution renvoie bien à une loi"
                " organique le contenu des études d'impact, et c'est un domaine"
                " organique authentique. La règle contraint donc la procédure — la"
                " recevabilité d'un texte — et non le fond, que seule une révision"
                " constitutionnelle pourrait lier. Nous ne promettons que ce que ce"
                " véhicule permet.",
            ),
            mesure(
                7, "Sortir du pénal ce qui n'a pas à y être",
                "<p>Déclassement en sanction administrative, en contravention ou en"
                " responsabilité civile des manquements de pure forme — obligations"
                " déclaratives, seuils, formalités — qui ne portent atteinte ni aux"
                " personnes, ni aux biens, ni aux libertés, ni à l'environnement. Le"
                " temps de juge, de procureur et d'enquêteur ainsi rendu est"
                " l'équivalent d'un recrutement, et il est immédiat.</p>",
                porte="Loi ordinaire", cout=COUTS[7].libelle,
                objection="C'est la dépénalisation de la délinquance économique sous"
                " un autre nom : les puissants y gagneront l'impunité que les autres"
                " n'auront pas.",
                reponse="Alors disons-le par une liste, dans les deux sens. Ne sortent"
                " pas du pénal, et ne sortiront pas : les atteintes aux personnes, les"
                " atteintes sexuelles, la corruption, la fraude fiscale, les"
                " manquements à la sécurité au travail, les atteintes à"
                " l'environnement. Sortent : les obligations déclaratives, les défauts"
                " de formalité, les franchissements de seuil sans dommage. Et une"
                " sanction administrative n'est pas une absence de sanction — elle"
                " tombe plus vite et plus sûrement qu'une correctionnelle dont le"
                " parquet classera 60 % des dossiers.",
            ),
            mesure(
                8, "Évaluer toute loi pénale au bout de trois ans",
                "<p>Clause de réexamen obligatoire : trois ans après son entrée en"
                " vigueur, toute incrimination nouvelle fait l'objet d'une évaluation"
                " publique — combien de poursuites, combien de condamnations, quel"
                " effet — inscrite de droit à l'ordre du jour du Parlement.</p>",
                porte="Loi organique relative aux études d'impact, et règlements"
                     " des assemblées",
                cout=COUTS[8].libelle,
                objection="Trois ans, c'est trop court pour juger d'une loi pénale :"
                " le temps que les affaires remontent jusqu'au jugement, il ne s'est"
                " presque rien passé.",
                reponse="C'est vrai pour le quantum des condamnations, et c'est"
                " précisément ce que l'évaluation dira. Mais une incrimination qui n'a"
                " donné lieu à aucune poursuite en trois ans n'a pas besoin d'un recul"
                " de dix ans pour qu'on en parle. Le réexamen n'abroge rien de"
                " lui-même : il oblige à un débat documenté, et laisse le Parlement"
                " conclure qu'il faut attendre encore.",
            ),
        ), ancre="champ"),

        section("L'exécution des peines", mesures(
            mesure(
                9, "Quatre-vingt-dix jours entre la décision et l'exécution",
                "<p>Délai maximal inscrit dans le code de procédure pénale entre une"
                " décision définitive et sa mise à exécution, aménagement compris."
                " Aujourd'hui, " + valeur("execution_1an") + " des peines fermes sont"
                " mises à exécution dans l'année, et " + valeur("peines_perdues")
                + " ne le seront jamais. Le dépassement est signalé au président de"
                " la juridiction et compté dans la publication trimestrielle.</p>",
                porte="Loi ordinaire (code de procédure pénale)",
                cout=COUTS[9].libelle,
                objection="Un délai inscrit dans la loi sans sanction est un vœu ;"
                " assorti d'une sanction, il crée une nullité dont profiteront les"
                " condamnés qu'on n'aura pas su convoquer à temps.",
                reponse="Il n'y a ni nullité, ni prescription, ni extinction de la"
                " peine : le dépassement ne libère personne et ne fait rien tomber."
                " Il est signalé, compté et publié. La sanction est politique et"
                " budgétaire, pas procédurale — c'est la seule forme de contrainte"
                " qui ne se retourne pas contre la victime.",
            ),
            mesure(
                10, "La convocation remise à l'audience, jamais par courrier",
                "<p>Généralisation du bureau de l'exécution des peines dans toutes les"
                " juridictions : le condamné repart de l'audience avec sa convocation"
                " et ses obligations, et la victime avec l'information sur ses"
                " droits.</p>",
                porte="Loi de finances (emplois de greffe), et circulaire"
                     " d'application",
                cout=COUTS[10].libelle,
                objection="Les bureaux de l'exécution des peines existent depuis 2004."
                " Annoncer leur généralisation, c'est présenter l'existant comme une"
                " réforme.",
                reponse="Ils existent et ils sont inégalement dotés : là où le greffe"
                " manque, le bureau ferme ou ne reçoit pas. C'est pourquoi la mesure"
                " ne passe pas par une circulaire — la version précédente de ce"
                " programme le prévoyait, et c'était une faute : une circulaire ne"
                " crée pas d'emplois. Elle passe par la loi de finances, et elle est"
                " adossée à la mesure 3.",
            ),
            mesure(
                11, "Publier le stock, puis l'éteindre",
                "<p>Publication trimestrielle du stock de peines fermes en attente"
                " d'exécution — qui n'existe aujourd'hui dans aucune série"
                " publique —, puis plan d'apurement avec objectif annuel par ressort"
                " et revue publique devant le Parlement. Les peines les plus anciennes"
                " sont traitées en premier. L'engagement chiffré porte sur le taux de"
                " mise à exécution à un an, qui est publié : le porter de"
                " " + valeur("execution_1an") + " à 95 %.</p>",
                porte="Décret (publication) et loi de finances (apurement)",
                cout=COUTS[11].libelle,
                objection="Vous ne connaissez pas le stock, donc vous ne pouvez pas"
                " promettre de l'éteindre en cinq ans, ni chiffrer ce que cela coûte.",
                reponse="L'objection est juste, et elle a modifié la mesure : elle"
                " commence désormais par publier le stock, et l'engagement chiffré"
                " porte sur le seul indicateur que le ministère publie — le taux de"
                " mise à exécution. L'objectif d'apurement sera révisé à la première"
                " publication du stock, et nous nous engageons à le réviser en public"
                " plutôt qu'à défendre un chiffre que nous aurions inventé.",
            ),
            mesure(
                12, "Porter la mesure de la récidive à cinq ans",
                "<p>Le ministère publie chaque année la récidive des sortants de"
                " prison <strong>à un an</strong> — " + valeur("recidive_1an")
                + " pour les sortants de 2020. Ce que la France n'a plus, c'est le"
                " suivi à cinq ans : le dernier porte sur la cohorte 2002 et date de"
                " 2011. Nous demandons l'extension de la série existante à cinq ans,"
                " et sa ventilation par type de peine, par établissement et par mode"
                " de sortie.</p>",
                porte="Décret", cout=COUTS[12].libelle,
                objection="La récidive est mesurée, et publiée chaque année. Vous"
                " proposez de créer ce qui existe — et vous l'aviez d'ailleurs écrit"
                " vous-mêmes.",
                reponse="Nous l'avions écrit, et c'était faux : la première version de"
                " ce programme affirmait que la récidive n'était plus mesurée depuis"
                " 2011. Elle l'est, à un an, et nous avons corrigé la page et le"
                " constat qui la portait. Ce qui manque est le suivi long et la"
                " ventilation : un taux global à un an ne dit pas si un aménagement de"
                " peine vaut mieux qu'une sortie sèche, qui est la seule question que"
                " l'on se pose en écrivant une politique pénale.",
            ),
        ), ancre="execution"),

        section("La prison", mesures(
            mesure(
                13, "Rendre la densité carcérale opposable",
                "<p>Publication mensuelle par établissement, et obligation pour"
                " l'administration, au-delà d'un seuil, de <em>saisir</em> le juge de"
                " l'application des peines des situations aménageables au regard des"
                " critères publiés. Le juge décide, et peut refuser. Sont exclues du"
                " dispositif les personnes condamnées pour atteinte aux personnes,"
                " atteinte sexuelle, terrorisme ou criminalité organisée.</p>",
                porte="Loi ordinaire", cout=COUTS[13].libelle,
                objection="C'est une libération automatique déguisée : au-delà d'un"
                " seuil, on ouvre les portes pour faire de la place.",
                reponse="Rien n'est automatique. L'administration saisit, le juge"
                " décide, et il refuse s'il l'estime nécessaire ; les aménagements"
                " dont il s'agit existent déjà dans le code, avec leurs conditions."
                " Nous changeons qui doit les proposer, pas qui les accorde, et nous"
                " excluons nommément les condamnations qui menacent autrui. Ce que"
                " nous refusons, c'est l'état actuel : à " + CHIFFRES["densite_maison_arret"].valeur
                + " de densité en maison d'arrêt, la question de savoir qui sort est"
                " déjà tranchée — par la place disponible, et par personne.",
            ),
            mesure(
                14, "Construire, et publier le coût complet",
                "<p>Programme de construction porté à environ 3 000 places nettes par"
                " an — à " + valeur("cout_place") + " la place nette constatée par la"
                " Cour des comptes, c'est ce que coûtent 800 M€ par an. Recours à la"
                " conception-réalisation et à la gestion déléguée lorsque le coût"
                " complet publié — construction, exploitation, maintenance sur trente"
                " ans — la donne gagnante. Le principe ne décide pas ; le coût"
                " décide.</p>",
                porte="Loi de finances", cout=COUTS[14].libelle,
                objection="Le « plan 15 000 » montre que le problème n'est pas"
                " l'argent : neuf ans après son lancement, " + CHIFFRES["places_livrees"].valeur
                + " places sont livrées et le coût a été réévalué de 46 %. Ajouter des"
                " crédits à une machine qui ne livre pas ne produira rien.",
                reponse="C'est la meilleure objection du programme, et elle est en"
                " partie imparable : la contrainte est autant le foncier et"
                " l'acceptabilité locale que le budget. Elle nous a conduits à deux"
                " corrections. D'abord le montant : la version précédente prévoyait"
                " 500 M€ par an, ce qui n'achète pas 2 000 places au coût réel et ne"
                " rattrape donc même pas la croissance de l'effectif détenu. Ensuite"
                " la méthode : la mesure porte sur la publication du coût complet"
                " opération par opération, seule manière connue de rendre les"
                " dérapages visibles avant qu'ils soient acquis. Nous ne promettons"
                " pas de construire vite ; nous promettons de dire chaque année"
                " combien de places ont été livrées et à quel prix.",
            ),
            mesure(
                15, "Une activité pour toute personne détenue",
                "<p>Travail rémunéré, formation ou enseignement, avec ouverture des"
                " ateliers aux entreprises selon une procédure simple, et une"
                " rémunération dont une part indemnise les parties civiles et une part"
                " est bloquée jusqu'à la sortie.</p>",
                porte="Loi ordinaire et décrets", cout=COUTS[15].libelle,
                objection="Les entreprises ne viendront pas, et le travail"
                " pénitentiaire, moins payé, concurrence l'emploi libre.",
                reponse="Le contrat d'emploi pénitentiaire créé par la loi du"
                " 22 décembre 2021 a réglé la question des droits ; ce qui manque est"
                " la simplicité d'entrée, et c'est l'objet de la mesure. Sur la"
                " concurrence : elle serait fondée si la rémunération restait"
                " symbolique, ce que nous proposons justement de corriger. Et la"
                " première bénéficiaire d'un détenu qui travaille est la partie"
                " civile, qui aujourd'hui n'est presque jamais indemnisée.",
            ),
        ), ancre="prison"),

        section("La justice civile", mesures(
            mesure(
                16, "Un délai de jugement garanti",
                "<p>Douze mois en première instance civile, six pour les litiges"
                " simples. Au-delà, indemnisation forfaitaire de plein droit, sans"
                " faute à prouver, portée par une dotation distincte et non"
                " fongible — elle ne se prélève pas sur les greffes dont dépend le"
                " délai.</p>",
                porte="Loi ordinaire (code de l'organisation judiciaire)",
                cout=COUTS[16].libelle,
                objection="Ce droit existe déjà : l'article L. 141-1 du code de"
                " l'organisation judiciaire permet d'engager la responsabilité de"
                " l'État pour délai déraisonnable. Vous proposez l'existant, et vous"
                " financez les indemnités avec l'argent qui manque aux tribunaux.",
                reponse="Il existe, et il est impraticable : il faut démontrer une"
                " faute, saisir le tribunal judiciaire de Paris, et attendre — ce que"
                " presque aucun justiciable ne fait. Nous renversons la charge et"
                " forfaitisons le montant : c'est la différence entre un droit et un"
                " droit exerçable. Sur le financement, l'objection portait juste"
                " contre notre première rédaction : l'indemnisation est désormais"
                " portée par une ligne distincte et non fongible, de sorte qu'un"
                " retard ne se paie jamais en moyens retirés à celui qui juge.",
            ),
            mesure(
                17, "Une voie rapide pour les petits litiges",
                "<p>Procédure simplifiée en ligne sous un seuil de montant :"
                " formulaire, échange écrit, décision motivée en quelques semaines,"
                " appel limité aux points de droit. Médiation préalable gratuite, sans"
                " obligation de transiger. Droit inconditionnel à une audience sur"
                " simple demande, et guichet physique dans chaque tribunal.</p>",
                porte="Loi ordinaire et décret", cout=COUTS[17].libelle,
                objection="C'est une justice au rabais, qui exclura ceux qui ne sont"
                " pas à l'aise avec un écran — c'est-à-dire souvent ceux dont le"
                " litige est le plus modeste.",
                reponse="D'où les trois garanties inscrites dans la mesure : audience"
                " de droit sur simple demande, guichet physique dans chaque tribunal,"
                " et aucune décision rendue par un traitement automatisé. La justice"
                " au rabais, aujourd'hui, c'est le litige de huit cents euros que"
                " personne ne porte parce que le délai et le coût excèdent l'enjeu :"
                " le droit y existe sur le papier et pas dans la vie.",
            ),
            mesure(
                18, "Achever l'ouverture des décisions de justice",
                "<p>Publication intégrale, pseudonymisée, libre et réutilisable de"
                " toutes les décisions, tous degrés et toutes matières, avec"
                " calendrier public de déploiement et compte rendu annuel du retard."
                " L'opacité profite à ceux qui plaident souvent, contre ceux qui"
                " plaident une fois dans leur vie.</p>",
                porte="Décret", cout=COUTS[18].libelle,
                objection="La loi du 7 octobre 2016 et le décret du 29 juin 2020 l'ont"
                " déjà prévu. Vous proposez d'appliquer une loi votée il y a dix ans.",
                reponse="Oui — et c'est une mesure, parce que dix ans après le vote la"
                " couverture reste partielle hors Cour de cassation et cours d'appel,"
                " et qu'aucun calendrier public ne dit quand elle sera complète. Une"
                " part de ce programme consiste à faire ce qui a déjà été décidé :"
                " nous préférons le dire ainsi plutôt que de déguiser l'exécution"
                " d'une loi en innovation.",
            ),
        ), ancre="civil"),

        section("Les libertés", mesures(
            mesure(
                19, "Achever l'indépendance du parquet",
                "<p>Révision constitutionnelle : nomination des magistrats du parquet"
                " sur avis conforme du Conseil supérieur de la magistrature, et"
                " transfert au Conseil du pouvoir disciplinaire. La politique pénale"
                " générale reste au garde des Sceaux, par instructions publiées, comme"
                " le prévoit l'article 30 du code de procédure pénale.</p>",
                porte="Loi constitutionnelle (Congrès ou référendum)",
                cout=COUTS[19].libelle,
                objection="Deux choses. D'une part, il faut les trois cinquièmes du"
                " Congrès : c'est hors de portée, et l'annoncer est une facilité."
                " D'autre part, un parquet indépendant est un parquet qui ne rend de"
                " comptes à personne.",
                reponse="Sur la faisabilité : ce n'est pas hors de portée, c'est"
                " inachevé — plusieurs projets ont été déposés et retirés faute de"
                " réunion du Congrès, pas faute de majorité. Sur la responsabilité,"
                " c'est l'objection sérieuse, et la réponse tient à une distinction :"
                " ce qui sort de la main du ministre est la <em>carrière</em> des"
                " procureurs, pas la <em>politique pénale</em>, qui lui reste et qui"
                " est publiée. La discipline, elle, ne disparaît pas : elle passe au"
                " CSM, qui l'exerce publiquement, ce qui est davantage de contrôle"
                " qu'aujourd'hui et non moins.",
            ),
            mesure(
                20, "Un juge du siège pour toute atteinte à la vie privée",
                "<p>Dans les enquêtes judiciaires : autorisation préalable par un juge"
                " du siège de toute technique attentatoire à la vie privée. Dans tous"
                " les régimes, y compris le renseignement administratif : extinction"
                " automatique des expérimentations à leur terme, et information de la"
                " personne surveillée une fois la mesure achevée et l'enquête close,"
                " sauf décision motivée.</p>",
                porte="Loi ordinaire", cout=COUTS[20].libelle,
                objection="Soumettre toute technique de surveillance à un juge, c'est"
                " désarmer les services de renseignement face au terrorisme et au"
                " narcotrafic.",
                reponse="La mesure distingue deux régimes, et la distinction est"
                " inscrite dans son texte parce que son absence était un défaut de"
                " notre première rédaction. L'autorisation par un juge du siège porte"
                " sur la <strong>police judiciaire</strong>. Le renseignement"
                " administratif reste sous le régime de la loi du 24 juillet 2015, le"
                " contrôle de la CNCTR et celui du Conseil d'État : nous ne lui"
                " appliquons que les deux autres règles — l'extinction des"
                " expérimentations et l'information a posteriori —, dont aucune"
                " n'empêche une surveillance de commencer.",
            ),
        ), ancre="libertes"),

        section(
            "Le chiffrage",
            "".join([
                "<p>Le programme est dominé par une seule dépense : des gens. Le"
                " tableau ci-dessous n'est pas une estimation posée à côté des"
                " mesures — c'est leur somme, calculée à la construction de la page."
                " Chacune des vingt mesures est affectée à un poste et à un seul, et"
                " un test refuse de publier la page si l'une d'elles n'y est pas."
                " Les montants sont en euros de 2026, à population constante, une"
                " fois la trajectoire de dix ans parcourue.</p>",
                tableau(
                    "Coût annuel du programme, à l'issue de la trajectoire décennale",
                    ("Poste", "Effectif ou volume", "Coût annuel à terme"),
                    _lignes_du_chiffrage(),
                    source="Somme des coûts déclarés par les vingt mesures."
                           " Hypothèses : coût complet employeur d'environ"
                           " 110 000 € pour un magistrat et 65 000 € pour un"
                           " greffier, cible d'effectifs égale à la médiane"
                           " européenne rapportée à la population française, place"
                           " de prison à 270 000 € d'après la Cour des comptes."
                           " Le détail du calcul est dans le code du site, et se"
                           " rediscute.",
                ),
                f"<p>S'y ajoutent, et ne sont pas comptés dans ce total parce"
                f" qu'ils s'éteignent : <strong class=\"cle-texte\">{transitoire:.0f} M€"
                " par an pendant cinq ans</strong> pour l'apurement du stock de"
                " peines, et"
                f" <strong class=\"cle-texte\">{investissement:.0f} M€</strong>"
                " d'investissement une fois, pour la procédure en ligne et"
                " l'ouverture des décisions.</p>",
                f"<p>Porté au terme de la trajectoire, le budget de la mission"
                f" « Justice » atteindrait <strong class=\"cle-texte\">{_md(budget_final)}"
                " Md€ hors pensions</strong>, contre " + valeur("budget")
                + f" aujourd'hui, soit environ {part_pib} % du produit intérieur"
                " brut contre " + valeur("part_pib") + ". Tous les montants de"
                " cette page s'entendent hors contribution au compte d'affectation"
                " spéciale « Pensions » : pensions comprises, la mission pèse"
                " aujourd'hui 13,1 Md€, et confondre les deux périmètres est la"
                " manière la plus simple de faire dire n'importe quoi à un"
                " chiffrage.</p>",
                encadre(
                    "<h3>L'équation carcérale, écrite en entier</h3>"
                    "<p>Trois de nos mesures agissent en sens contraire sur le même"
                    " nombre, et un programme sérieux doit poser l'addition plutôt"
                    " que de laisser chacune briller de son côté.</p>"
                    "<p><strong>Ce qui remplit.</strong> Il manque aujourd'hui plus de"
                    " 23 000 places. Exécuter les peines en quatre-vingt-dix jours"
                    " (mesure 9) et apurer le stock (mesure 11) ajoutent des entrées :"
                    " de l'ordre de 3 000 à 5 000 personnes détenues en régime"
                    " permanent, selon la durée moyenne des peines concernées.</p>"
                    "<p><strong>Ce qui vide.</strong> À 800 M€ par an et"
                    " 270 000 € la place nette, la mesure 14 livre environ 3 000"
                    " places par an, soit 30 000 en dix ans. La mesure 7 retire du"
                    " champ pénal des manquements qui n'y conduisent presque jamais :"
                    " son effet sur l'effectif détenu est réel mais faible, et nous"
                    " ne le chiffrons pas.</p>"
                    "<p><strong>Ce que cela donne.</strong> 30 000 places livrées"
                    " contre 23 000 manquantes et 3 000 à 5 000 entrées"
                    " supplémentaires : l'équation se referme tout juste, et"
                    " seulement si l'effectif détenu cesse de croître au rythme des"
                    " trois dernières années. S'il continue, elle ne se referme pas,"
                    " et il faudra soit construire davantage, soit prononcer moins de"
                    " courtes peines. Nous préférons écrire cette incertitude que la"
                    " passer sous silence : c'est la première chose qu'un adversaire"
                    " calculerait.</p>"
                ),
                encadre(
                    "<h3>D'où vient l'argent</h3>"
                    "<p>Nous ne proposons pas d'impôt nouveau. La justice est l'une"
                    " des rares fonctions que le libéralisme assume de vouloir mieux"
                    " dotées, parce qu'elle est la condition de tout le reste : il n'y"
                    " a pas de marché sans contrat exécutoire, ni de liberté sans juge"
                    " pour la faire respecter. L'effort — un peu plus de trois"
                    " milliards par an, soit environ 0,2 % de la dépense"
                    " publique — est un redéploiement au sein du budget de l'État."
                    "</p>"
                    "<p><strong>Et nous ne disons pas encore ce que nous coupons.</strong>"
                    " C'est la question que l'on nous posera en premier, et il serait"
                    " malhonnête d'y répondre par une formule. Nommer 3,3 Md€"
                    " d'économies relève du programme budgétaire d'ensemble du parti,"
                    " pas de sa page justice ; nous nous engageons à ce que les deux"
                    " soient publiés ensemble, et à ce que celui-ci ne soit pas"
                    " présenté comme financé tant que l'autre ne l'a pas été.</p>"
                ),
                note(
                    "<p><strong>Ce chiffrage est un ordre de grandeur, et il est de"
                    " nous.</strong> Il n'émane ni du ministère, ni de la Cour des"
                    " comptes. Les hypothèses sont écrites au-dessus précisément pour"
                    " qu'on puisse les contester une par une : si l'une d'elles est"
                    " fausse, le total change, et nous le corrigerons. Il a d'ailleurs"
                    " déjà changé — la première version de cette page annonçait"
                    " 2,8 Md€ alors que ses propres mesures, additionnées, en"
                    " pesaient davantage. Le tableau est désormais calculé à partir"
                    " des mesures, ce qui rend l'écart impossible plutôt"
                    " qu'improbable.</p>",
                    genre="vigilance",
                ),
            ]),
            ancre="chiffrage",
        ),

        section(
            "Ce que ce programme ne dit pas",
            "".join([
                "<p>Un programme se juge autant à ses absences qu'à ses mesures, et"
                " mieux vaut les écrire soi-même. Voici ce que ces vingt mesures ne"
                " traitent pas, et sur quoi nous n'avons donc, à ce jour, rien à"
                " faire valoir.</p>",
                encadre(
                    "<h3>Six sujets que nous n'avons pas traités</h3>"
                    "<ul class=\"serree\">"
                    "<li><strong>La justice des mineurs.</strong> Le code de la"
                    " justice pénale des mineurs est en vigueur depuis 2021 et"
                    " n'a pas été évalué. Nous n'avons pas de mesure à ce"
                    " stade.</li>"
                    "<li><strong>Les victimes.</strong> Elles n'apparaissent ici"
                    " qu'en creux, dans les mesures 10 et 15. C'est insuffisant"
                    " pour un programme qui prétend rendre la justice plus"
                    " sûre.</li>"
                    "<li><strong>La loi du 13 juin 2025 contre le narcotrafic.</strong>"
                    " Elle crée un parquet national anticriminalité organisée et le"
                    " « dossier coffre », et le Conseil constitutionnel en a censuré"
                    " six articles. C'est le texte pénal le plus important depuis"
                    " 2019, et nous n'avons pas encore arrêté de position."
                    "</li>"
                    "<li><strong>La justice administrative.</strong> Aucune de ces"
                    " vingt mesures ne la concerne, alors que le contentieux des"
                    " étrangers en occupe une part considérable.</li>"
                    "<li><strong>Les stupéfiants.</strong> La question commande une"
                    " part importante de la population détenue et touche directement"
                    " la mesure 7. Ne pas la trancher est aussi une position ; nous"
                    " préférons la signaler que la laisser deviner.</li>"
                    "<li><strong>L'outre-mer.</strong> Les délais et les densités"
                    " carcérales y dépassent tout ce que ce site décrit, et aucune"
                    " des mesures ci-dessus n'est adaptée à cette échelle.</li>"
                    "</ul>"
                ),
            ]),
            ancre="absences",
        ),

        suite("Les sources et la méthode", "sources.html"),
    ])
