"""Les chiffres du site, et leur source.

Un chiffre sans source est une opinion. Aucun nombre n'est écrit dans le texte
des pages : il est déclaré ici, avec l'année à laquelle il se rapporte,
l'organisme qui le publie, **le document précis** où il se trouve et la date à
laquelle nous l'y avons vérifié, puis appelé par sa clé. La page « Sources »
se construit ensuite toute seule, et un chiffre qu'on ajouterait sans source ne
franchit pas les tests.

Trois règles, et elles sont tenues par des tests :

1. **Le document, pas le portail.** Renvoyer vers la page d'accueil d'un
   organisme n'est pas citer une source : c'est inviter le lecteur à chercher
   à notre place. Chaque chiffre porte le titre exact de la publication.
2. **La date de vérification, et sa péremption.** Un chiffre vérifié il y a
   deux ans n'est plus vérifié. ``verifie_le`` porte la date du dernier
   contrôle à la source ; au-delà de dix-huit mois, un test échoue.
3. **Le dénominateur est un chiffre comme un autre.** Une part de PIB suppose
   un PIB. Il est déclaré ici, avec sa source, comme le reste.

Les valeurs sont volontairement arrondies et introduites par « environ »,
« plus de », « de l'ordre de ». Ce site compare des ordres de grandeur — onze
juges pour cent mille habitants contre dix-huit — et un chiffre au dixième
près y donnerait une précision que la source, souvent, ne garantit pas
elle-même. Qui a besoin de la décimale suit le lien.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from html import escape

#: La date de la dernière campagne de vérification à la source.
DERNIERE_VERIFICATION = "2026-09-21"

#: Au-delà de ce délai, un chiffre vérifié cesse de l'être et un test échoue.
PEREMPTION_MOIS = 18


@dataclass(frozen=True)
class Source:
    """Un organisme qui publie, et l'endroit où il publie."""

    nom: str
    url: str
    detail: str = ""


SOURCES: dict[str, Source] = {
    "justice": Source(
        "Ministère de la Justice — service statistique ministériel",
        "https://www.justice.gouv.fr/documentation/etudes-et-statistiques",
        "Les « Références statistiques Justice », les « Chiffres clés de la"
        " Justice » et la collection « Infos rapides Justice », publiées par le"
        " service statistique, des études et de la recherche (SSER).",
    ),
    "penitentiaire": Source(
        "Ministère de la Justice — statistique mensuelle de la population détenue",
        "https://www.justice.gouv.fr/documentation/etudes-et-statistiques/statistiques-mensuelles-population-detenue-ecrouee-11",
        "La statistique mensuelle de la population écrouée et détenue :"
        " effectifs, places opérationnelles, densité par établissement. Elle"
        " paraît chaque mois et se révise : c'est la source la plus fraîche du"
        " site, et celle qui périme le plus vite.",
    ),
    "cepej": Source(
        "CEPEJ — Commission européenne pour l'efficacité de la justice",
        "https://www.coe.int/fr/web/cepej/evaluation-of-judicial-systems",
        "Le rapport d'évaluation des systèmes judiciaires européens, publié tous"
        " les deux ans par le Conseil de l'Europe. Il compte les juges, les"
        " procureurs et les budgets d'une quarantaine d'États sur les mêmes"
        " définitions — c'est ce qui le rend comparable.",
    ),
    "comptes": Source(
        "Cour des comptes",
        "https://www.ccomptes.fr/",
        "Rapports publics thématiques et insertions du rapport annuel"
        " consacrés à la justice, aux prisons et à l'exécution des peines.",
    ),
    "senat": Source(
        "Sénat — rapports budgétaires",
        "https://www.senat.fr/",
        "Les rapports de la commission des finances sur la mission « Justice »"
        " des lois de finances. Ils donnent, année après année, les crédits"
        " réels et l'état d'avancement des programmes annoncés.",
    ),
    "insee": Source(
        "Insee — comptes nationaux",
        "https://www.insee.fr/fr/statistiques/8996855",
        "Les comptes de la Nation, qui donnent le produit intérieur brut en"
        " euros courants — le dénominateur de toute part de PIB citée ici.",
    ),
    "legifrance": Source(
        "Légifrance",
        "https://www.legifrance.gouv.fr/",
        "Le texte des lois citées. Les références sont données en entier —"
        " numéro et date — de sorte qu'elles se retrouvent par la recherche du"
        " site, dont les adresses d'article ne sont pas stables.",
    ),
    "cedh": Source(
        "Cour européenne des droits de l'homme",
        "https://hudoc.echr.coe.int/",
        "La base HUDOC : le texte intégral des arrêts cités.",
    ),
    "cevipof": Source(
        "CEVIPOF — Baromètre de la confiance politique",
        "https://www.sciencespo.fr/cevipof/fr/le-barometre-de-la-confiance-politique/",
        "L'enquête annuelle de Sciences Po sur la confiance des Français dans"
        " leurs institutions, dont la justice.",
    ),
    "calcul": Source(
        "Calcul du site",
        "https://github.com/g-pliberal/Justice",
        "Une opération, faite ici, entre des chiffres publiés ailleurs. Le"
        " calcul est écrit dans le code, la précision dit lesquels, et les"
        " nombres d'entrée sont eux-mêmes déclarés sur cette page.",
    ),
}


@dataclass(frozen=True)
class Chiffre:
    """Une valeur, ce qu'elle mesure, quand, d'où elle vient, et depuis quand.

    ``document`` est le titre exact de la publication — pas le nom de
    l'organisme, pas l'intitulé d'un portail. ``url`` mène au document
    lui-même quand son adresse est stable. ``verifie_le`` porte la date du
    dernier contrôle effectué à la source ; vide, le chiffre est signalé
    comme non revérifié sur la page « Sources », et il le reste tant que
    personne ne l'a rouvert.
    """

    valeur: str
    libelle: str
    precision: str
    source: str
    annee: str
    document: str
    url: str = ""
    verifie_le: str = ""

    def __post_init__(self) -> None:
        if self.source not in SOURCES:
            raise KeyError(f"source inconnue : {self.source}")
        if self.verifie_le:
            date.fromisoformat(self.verifie_le)

    @property
    def verifie(self) -> bool:
        return bool(self.verifie_le)

    @property
    def lien(self) -> str:
        """L'adresse du document, à défaut celle de l'organisme."""
        return self.url or SOURCES[self.source].url


V = DERNIERE_VERIFICATION

CHIFFRES: dict[str, Chiffre] = {
    # -- les moyens ----------------------------------------------------------
    "budget": Chiffre(
        "10,6 Md€",
        "Budget de la justice",
        "Crédits de paiement de la mission « Justice » au projet de loi de"
        " finances pour 2026, hors contribution au compte d'affectation"
        " spéciale « Pensions » : 10 629 M€. Pensions comprises, la mission"
        " pèse 13 055 M€ — tout le site raisonne hors pensions, et le dit"
        " chaque fois qu'il cite ce périmètre.",
        "senat", "2026",
        "Rapport général sur le projet de loi de finances pour 2026 —"
        " mission « Justice », commission des finances du Sénat",
        "https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html",
        V,
    ),
    "budget_cible": Chiffre(
        "10,7 Md€",
        "La cible pour 2027",
        "Trajectoire fixée par la loi n° 2023-1059 du 20 novembre 2023"
        " d'orientation et de programmation du ministère de la justice"
        " 2023-2027 : 10 691 M€ hors pensions, à périmètre constant. Le budget"
        " 2026 en est à 62 M€ près : sur les crédits, la trajectoire est"
        " à peu près tenue. C'est sur les effectifs et les places de prison"
        " qu'elle ne l'est pas.",
        "senat", "2027",
        "Rapport général sur le projet de loi de finances pour 2026 —"
        " mission « Justice », commission des finances du Sénat",
        "https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html",
        V,
    ),
    "pib": Chiffre(
        "2 991 Md€",
        "Produit intérieur brut",
        "PIB de la France en 2025, en euros courants. Il n'est cité sur aucune"
        " page : il est ici parce qu'il est le dénominateur de la part de PIB"
        " ci-dessous, et qu'une division dont on cache le diviseur n'est pas"
        " une source.",
        "insee", "2025",
        "Les comptes de la Nation en 2025, Insee Première n° 2105",
        "https://www.insee.fr/fr/statistiques/8996855",
        V,
    ),
    "part_pib": Chiffre(
        "environ 0,36 %",
        "Part du PIB",
        "Budget de la mission « Justice » hors pensions rapporté au PIB :"
        " 10,63 ÷ 2 991. Pensions comprises, la part atteint 0,44 %. Les"
        " comparaisons internationales de budget ne retiennent pas toutes le"
        " même périmètre, et la France y inclut ses prisons quand d'autres"
        " États ne le font pas.",
        "calcul", "2026",
        "Division des deux chiffres déclarés ci-dessus, faite dans le code du"
        " site",
        "https://github.com/g-pliberal/Justice/blob/main/src/justice/chiffres.py",
        V,
    ),
    "juges": Chiffre(
        "11,1",
        "Juges pour 100 000 habitants",
        "Juges professionnels en France. La médiane des États du Conseil de"
        " l'Europe est de 17,6. L'édition suivante du rapport, sur les données"
        " 2025, paraît en décembre 2026 : ce chiffre est le plus proche de sa"
        " péremption de tout le site.",
        "cepej", "données 2022",
        "Systèmes judiciaires européens — rapport d'évaluation de la CEPEJ,"
        " édition 2024 (cycle d'évaluation 2024, données 2022)",
        "https://www.coe.int/fr/web/cepej/evaluation-of-judicial-systems",
        V,
    ),
    "procureurs": Chiffre(
        "3,2",
        "Procureurs pour 100 000 habitants",
        "France. La médiane des États du Conseil de l'Europe est de 11,1 :"
        " c'est l'écart le plus large de tout le tableau européen.",
        "cepej", "données 2022",
        "Systèmes judiciaires européens — rapport d'évaluation de la CEPEJ,"
        " édition 2024 (cycle d'évaluation 2024, données 2022)",
        "https://www.coe.int/fr/web/cepej/evaluation-of-judicial-systems",
        V,
    ),
    "magistrats": Chiffre(
        "environ 9 800",
        "Magistrats en fonction",
        "Magistrats du siège et du parquet, toutes juridictions judiciaires"
        " confondues. L'effectif budgétaire et l'effectif réellement en poste"
        " ne coïncident pas : les postes vacants se comptent par centaines.",
        "justice", "2025",
        "Chiffres clés de la Justice, édition annuelle",
        "",
        "",
    ),
    "recrutements": Chiffre(
        "+1 500 magistrats",
        "Recrutements programmés",
        "Et +1 800 greffiers d'ici 2027, prévus par la loi de programmation du"
        " 20 novembre 2023. Le budget 2026 crée 286 emplois de magistrat et"
        " 342 de greffier : au rythme voté, la cible suppose que rien ne"
        " ralentisse. La promesse porte d'ailleurs sur les recrutements, pas"
        " sur les effectifs en poste : les départs s'en déduisent.",
        "senat", "2023-2027",
        "Rapport général sur le projet de loi de finances pour 2026 —"
        " mission « Justice », commission des finances du Sénat",
        "https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html",
        V,
    ),
    # -- les délais ----------------------------------------------------------
    "delai_civil": Chiffre(
        "environ 14 mois",
        "Une affaire civile en première instance",
        "Durée moyenne des affaires civiles terminées devant les tribunaux"
        " judiciaires. La moyenne masque des écarts considérables d'un"
        " contentieux et d'une juridiction à l'autre.",
        "justice", "2023",
        "Références statistiques Justice, chapitre « La justice civile »",
        "",
        "",
    ),
    "delai_appel": Chiffre(
        "environ 16 mois",
        "Puis l'appel",
        "Durée moyenne d'une procédure civile devant une cour d'appel, qui"
        " s'ajoute à la première instance.",
        "justice", "2023",
        "Références statistiques Justice, chapitre « La justice civile »",
        "",
        "",
    ),
    "delai_prudhommes": Chiffre(
        "plus de 15 mois",
        "Un litige prud'homal",
        "Durée moyenne devant un conseil de prud'hommes, hors référé — et près"
        " de six décisions sur dix y sont frappées d'appel.",
        "justice", "2023",
        "Références statistiques Justice, chapitre « La justice civile »",
        "",
        "",
    ),
    "delai_instruction": Chiffre(
        "environ 3 ans",
        "Une information judiciaire",
        "Durée moyenne d'un dossier confié à un juge d'instruction, de"
        " l'ouverture à la clôture.",
        "justice", "2023",
        "Références statistiques Justice, chapitre « La justice pénale »",
        "",
        "",
    ),
    # -- le pénal ------------------------------------------------------------
    "reponse_penale": Chiffre(
        "près de 90 %",
        "Taux de réponse pénale",
        "Part des affaires « poursuivables » — auteur identifié, infraction"
        " caractérisée — qui reçoivent une réponse du parquet. Le taux ne dit"
        " rien des affaires classées faute d'auteur connu, qui sont la"
        " majorité des plaintes déposées.",
        "justice", "2023",
        "Références statistiques Justice, chapitre « L'activité des parquets »",
        "",
        "",
    ),
    "classement_auteur": Chiffre(
        "environ 2 plaintes sur 3",
        "Classées faute d'auteur identifié",
        "Part des affaires reçues par les parquets qui sont classées sans suite"
        " parce que l'auteur n'a pas été retrouvé : l'essentiel de l'écart"
        " entre ce que vivent les victimes et le taux de réponse pénale.",
        "justice", "2023",
        "Références statistiques Justice, chapitre « L'activité des parquets »",
        "",
        "",
    ),
    "execution_1an": Chiffre(
        "environ 79 %",
        "Peines fermes exécutées dans l'année",
        "Taux de mise à exécution des peines d'emprisonnement ferme un an"
        " après le jugement ; il est de l'ordre de 57 % au moment même du"
        " jugement. Le ministère publie plusieurs mesures de l'exécution, sur"
        " des périmètres et des définitions qui ne se recoupent pas : une"
        " publication antérieure, sur les peines devenues exécutoires en 2016,"
        " donnait 30 % à l'audience et plus de 70 % à un an. Que le même fait"
        " se mesure de trois façons est en soi le problème.",
        "justice", "2024",
        "Références statistiques Justice, édition 2024, chapitre 12"
        " « L'exécution et l'application des peines »",
        "https://www.justice.gouv.fr/sites/default/files/2024-12/RSJ2024%20Chapitre%2012.pdf",
        V,
    ),
    "execution_5ans": Chiffre(
        "90 à 92 %",
        "Peines fermes exécutées à cinq ans",
        "Taux de mise à exécution cinq ans après que la peine est devenue"
        " exécutoire, stable depuis plusieurs années. C'est le chiffre que le"
        " ministère publie ; c'est son complément qui nous intéresse.",
        "justice", "2024",
        "Références statistiques Justice, édition 2024, chapitre 12"
        " « L'exécution et l'application des peines »",
        "https://www.justice.gouv.fr/sites/default/files/2024-12/RSJ2024%20Chapitre%2012.pdf",
        V,
    ),
    "peines_perdues": Chiffre(
        "8 à 10 %",
        "Peines fermes jamais exécutées",
        "Complément à 100 du taux de mise à exécution à cinq ans publié"
        " ci-dessus. Passé ce délai, le taux ne bouge plus : ces peines-là ne"
        " seront pas exécutées. Nous n'en donnons pas le nombre absolu, faute"
        " de série publiée du stock — et c'est cette absence-là, et non"
        " l'absence de toute statistique, qui justifie la mesure 11.",
        "calcul", "2024",
        "Complément à 100 du taux publié par le ministère, calculé dans le"
        " code du site",
        "https://github.com/g-pliberal/Justice/blob/main/src/justice/chiffres.py",
        V,
    ),
    "recidive": Chiffre(
        "59 %",
        "Recondamnés dans les cinq ans",
        "Part des personnes sorties de prison recondamnées dans les cinq ans ;"
        " 46 % sont réincarcérées. L'étude porte sur les personnes libérées"
        " en 2002 et a été publiée en 2011. Elle n'a jamais été reconduite :"
        " c'est le seul suivi à cinq ans dont la France dispose, et il décrit"
        " une cohorte d'il y a plus de vingt ans.",
        "justice", "cohorte 2002, publiée en 2011",
        "Annie Kensey et Abdelmalik Benaouda, « Les risques de récidive des"
        " sortants de prison — une nouvelle évaluation », Cahiers d'études"
        " pénitentiaires et criminologiques n° 36",
        "",
        "",
    ),
    "recidive_1an": Chiffre(
        "34,2 %",
        "Recondamnés dans l'année",
        "Part des personnes sorties de prison en 2020 condamnées à nouveau"
        " pour une infraction commise dans l'année suivant leur libération."
        " La série existe et se poursuit : 33,2 % pour les sortants de 2016,"
        " 33,4 % en 2017, 33,1 % en 2018, 31,7 % en 2019. Elle s'arrête à un"
        " an, ne distingue ni l'établissement ni le mode de sortie, et les"
        " cohortes 2019 et 2020 sont déformées par la crise sanitaire.",
        "justice", "sortants 2020, publié en avril 2025",
        "Kevin Schmitt, « Récidive des sortants de prison après un an : des"
        " évolutions contrastées en lien avec la crise sanitaire », Infos"
        " rapides Justice n° 27, SSER",
        "https://www.justice.gouv.fr/sites/default/files/2025-04/Infos_Rapides_Justice_n27.pdf",
        V,
    ),
    "incriminations": Chiffre(
        "plus de 10 000",
        "Infractions pénales en vigueur",
        "Estimation courante du nombre d'incriminations, réparties entre le"
        " code pénal et plusieurs dizaines d'autres codes. Aucune"
        " administration n'en tient le compte exact, et nous ne connaissons"
        " aucun dénombrement officiel : c'est l'un des rares chiffres de ce"
        " site que nous ne pouvons pas sourcer, et nous l'écrivons.",
        "justice", "estimation, non sourcée",
        "Aucune publication ne fait autorité : estimation reprise de la"
        " doctrine et des rapports parlementaires, citée ici comme telle",
        "",
        "",
    ),
    # -- la prison -----------------------------------------------------------
    "detenus": Chiffre(
        "plus de 86 000",
        "Personnes détenues",
        "86 645 personnes détenues au 1er février 2026, record battu de mois"
        " en mois depuis : l'effectif approchait 89 500 au 1er juillet 2026."
        " Les chiffres de cette section sont tous pris à la même date, pour"
        " qu'ils se rapportent les uns aux autres.",
        "penitentiaire", "1er février 2026",
        "Statistique mensuelle de la population détenue et écrouée en France,"
        " au 1er février 2026",
        "",
        V,
    ),
    "places": Chiffre(
        "environ 63 300",
        "Places opérationnelles",
        "Capacité réelle des établissements pénitentiaires au 1er février"
        " 2026, cellules indisponibles déduites. L'écart avec l'effectif"
        " détenu — plus de 23 000 personnes — est le nombre de places qui"
        " manquent.",
        "penitentiaire", "1er février 2026",
        "Statistique mensuelle de la population détenue et écrouée en France,"
        " au 1er février 2026",
        "",
        V,
    ),
    "densite": Chiffre(
        "près de 137 %",
        "Densité carcérale",
        "Rapport des détenus aux places sur l'ensemble du parc au 1er février"
        " 2026. Vingt-cinq établissements dépassent 200 %.",
        "penitentiaire", "1er février 2026",
        "Statistique mensuelle de la population détenue et écrouée en France,"
        " au 1er février 2026",
        "",
        V,
    ),
    "densite_maison_arret": Chiffre(
        "plus de 170 %",
        "Densité en maison d'arrêt",
        "Là où sont détenus les prévenus — présumés innocents — et les"
        " condamnés à de courtes peines. C'est la densité qui compte : la"
        " moyenne du parc est tirée vers le bas par les établissements pour"
        " peine, qui fonctionnent en cellule individuelle.",
        "penitentiaire", "1er février 2026",
        "Statistique mensuelle de la population détenue et écrouée en France,"
        " au 1er février 2026",
        "",
        V,
    ),
    "matelas": Chiffre(
        "plus de 6 500",
        "Matelas au sol",
        "6 596 personnes détenues dormaient sur un matelas posé à même le sol"
        " au 1er février 2026, faute de lit. Le chiffre est publié avec la"
        " statistique mensuelle, et il a plus que doublé en cinq ans.",
        "penitentiaire", "1er février 2026",
        "Statistique mensuelle de la population détenue et écrouée en France,"
        " au 1er février 2026",
        "",
        V,
    ),
    "cedh": Chiffre(
        "30 janvier 2020",
        "Condamnation de la France",
        "Arrêt J.M.B. et autres c. France : la Cour européenne des droits de"
        " l'homme juge les conditions de détention contraires à l'article 3 de"
        " la Convention et demande à la France de résorber la surpopulation."
        " Six ans après, l'effectif détenu a augmenté de plus de 15 %.",
        "cedh", "2020",
        "J.M.B. et autres c. France, requêtes n° 9671/15 et 31 autres,"
        " arrêt du 30 janvier 2020",
        "https://hudoc.echr.coe.int/fre?i=001-200446",
        "",
    ),
    "cout_detention": Chiffre(
        "de l'ordre de 120 €",
        "Coût d'une journée de détention",
        "Coût moyen par personne détenue et par jour, tous régimes confondus —"
        " soit plus de 40 000 € par an et par place occupée.",
        "comptes", "2023",
        "Rapports de la Cour des comptes sur l'administration pénitentiaire",
        "",
        "",
    ),
    "cout_place": Chiffre(
        "environ 270 000 €",
        "Coût d'une place de prison",
        "Coût moyen constaté à la place nette du « plan 15 000 », toutes"
        " opérations confondues. Le plan, lancé en 2017 pour 2027, est"
        " réévalué de 3,9 à 5,7 Md€ et repoussé à 2031 : c'est le chiffre qui"
        " commande tout programme de construction, y compris le nôtre.",
        "comptes", "2025",
        "Cour des comptes, « Le plan 15 000 places de prison : une ambition"
        " forte, une concrétisation laborieuse »",
        "https://www.ccomptes.fr/fr/publications/le-plan-15000-places-de-prison-une-ambition-forte-une-concretisation-laborieuse",
        V,
    ),
    "places_livrees": Chiffre(
        "5 411 sur 15 000",
        "Places de prison livrées",
        "Places nettes livrées au titre du « plan 15 000 » à l'automne 2026,"
        " soit 36 % de la cible neuf ans après son lancement — et 30 % de la"
        " cible révisée à 18 000. Un programme de construction s'apprécie aux"
        " places livrées, pas aux places annoncées.",
        "senat", "2026",
        "Rapport général sur le projet de loi de finances pour 2026 —"
        " mission « Justice », commission des finances du Sénat",
        "https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html",
        V,
    ),
    # -- le civil et l'économique -------------------------------------------
    "juges_consulaires": Chiffre(
        "environ 3 500",
        "Juges consulaires bénévoles",
        "Les tribunaux de commerce sont rendus par des chefs d'entreprise élus"
        " par leurs pairs, non rémunérés. Depuis le 1er janvier 2025, douze"
        " d'entre eux sont devenus, à titre expérimental, des tribunaux des"
        " activités économiques.",
        "justice", "2025",
        "Chiffres clés de la Justice, édition annuelle",
        "",
        "",
    ),
    "aide_juridictionnelle": Chiffre(
        "environ 600 M€",
        "Aide juridictionnelle",
        "Dépense annuelle de l'État pour l'accès au juge des justiciables sans"
        " ressources suffisantes, pour près d'un million d'admissions.",
        "justice", "2024",
        "Chiffres clés de la Justice, édition annuelle",
        "",
        "",
    ),
    "confiance": Chiffre(
        "environ 1 sur 2",
        "Français qui font confiance à la justice",
        "Part des personnes interrogées déclarant faire confiance à"
        " l'institution judiciaire. Le chiffre varie d'une vague à l'autre ;"
        " sa stabilité à ce niveau, elle, ne varie pas.",
        "cevipof", "2024-2025",
        "Baromètre de la confiance politique du CEVIPOF, vague annuelle",
        "",
        "",
    ),
}


def chiffre(cle: str) -> Chiffre:
    return CHIFFRES[cle]


def valeur(cle: str) -> str:
    """La valeur seule, pour l'écrire au fil d'une phrase, en or."""
    return f'<strong class="cle-texte">{escape(CHIFFRES[cle].valeur)}</strong>'


def verifies() -> tuple[int, int]:
    """Combien de chiffres ont été revérifiés à la source, sur combien."""
    return sum(1 for c in CHIFFRES.values() if c.verifie), len(CHIFFRES)


def fiche(cle: str) -> str:
    """Une fiche : la valeur, ce qu'elle mesure, la précision et la source."""
    c = CHIFFRES[cle]
    s = SOURCES[c.source]
    return (
        '<div class="fiche">'
        f'<p class="valeur">{escape(c.valeur)}</p>'
        f'<p class="etiquette">{escape(c.libelle)}</p>'
        f'<p class="precision">{escape(c.precision)} '
        f'<a href="{c.lien}">{escape(s.nom.split(" — ")[0])}</a>, {escape(c.annee)}.</p>'
        "</div>"
    )


def fiches(*cles: str, reperes: bool = True) -> str:
    classe = "fiches reperes" if reperes else "fiches"
    return f'<div class="{classe}">' + "".join(fiche(cle) for cle in cles) + "</div>"
