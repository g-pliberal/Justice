"""Les chiffres du site, et leur source.

Un chiffre sans source est une opinion. Aucun nombre n'est écrit dans le texte
des pages : il est déclaré ici, avec l'année à laquelle il se rapporte,
l'organisme qui le publie et l'adresse où le vérifier, puis appelé par sa clé.
La page « Sources » se construit ensuite toute seule, et un chiffre qu'on
ajouterait sans source ne franchit pas les tests.

Les valeurs sont volontairement arrondies et introduites par « environ »,
« plus de », « de l'ordre de ». Ce site compare des ordres de grandeur — onze
juges pour cent mille habitants contre dix-huit — et un chiffre au dixième
près y donnerait une précision que la source, souvent, ne garantit pas
elle-même. Qui a besoin de la décimale suit le lien.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape


@dataclass(frozen=True)
class Source:
    """Un organisme qui publie, et l'endroit où il publie."""

    nom: str
    url: str
    detail: str = ""


SOURCES: dict[str, Source] = {
    "justice": Source(
        "Ministère de la Justice — chiffres clés et statistiques",
        "https://www.justice.gouv.fr/documentation/etudes-et-statistiques",
        "Les « Chiffres clés de la Justice », publiés chaque année, et les"
        " séries détaillées du service statistique du ministère.",
    ),
    "penitentiaire": Source(
        "Ministère de la Justice — statistique des personnes détenues",
        "https://www.justice.gouv.fr/documentation/etudes-et-statistiques",
        "La statistique mensuelle de la population écrouée et détenue :"
        " effectifs, places opérationnelles, densité par type d'établissement.",
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
        "https://github.com/g-pliberal/justice",
        "Une division, faite ici, entre deux chiffres publiés ailleurs. Le"
        " calcul est écrit dans le code et la précision dit lesquels.",
    ),
}


@dataclass(frozen=True)
class Chiffre:
    """Une valeur, ce qu'elle mesure, quand, et d'où elle vient."""

    valeur: str
    libelle: str
    precision: str
    source: str
    annee: str

    def __post_init__(self) -> None:
        if self.source not in SOURCES:
            raise KeyError(f"source inconnue : {self.source}")


CHIFFRES: dict[str, Chiffre] = {
    # -- les moyens ----------------------------------------------------------
    "budget": Chiffre(
        "10,2 Md€",
        "Budget de la justice",
        "Crédits de paiement de la mission « Justice » pour 2025, administration"
        " pénitentiaire et protection judiciaire de la jeunesse comprises.",
        "justice", "2025",
    ),
    "budget_cible": Chiffre(
        "près de 11 Md€",
        "La cible pour 2027",
        "Trajectoire fixée par la loi n° 2023-1059 du 20 novembre 2023"
        " d'orientation et de programmation du ministère de la justice"
        " 2023-2027.",
        "legifrance", "2023",
    ),
    "part_pib": Chiffre(
        "environ 0,35 %",
        "Part du PIB",
        "Budget de la mission « Justice » rapporté au produit intérieur brut"
        " français. Calcul du site à partir du budget ci-dessus et du PIB"
        " publié par l'Insee.",
        "calcul", "2025",
    ),
    "juges": Chiffre(
        "11,1",
        "Juges pour 100 000 habitants",
        "Juges professionnels en France. La médiane des États du Conseil de"
        " l'Europe est de 17,6.",
        "cepej", "données 2022",
    ),
    "procureurs": Chiffre(
        "3,2",
        "Procureurs pour 100 000 habitants",
        "France. La médiane des États du Conseil de l'Europe est de 11,1 :"
        " c'est l'écart le plus large de tout le tableau européen.",
        "cepej", "données 2022",
    ),
    "magistrats": Chiffre(
        "environ 9 500",
        "Magistrats en fonction",
        "Magistrats du siège et du parquet, toutes juridictions judiciaires"
        " confondues.",
        "justice", "2024",
    ),
    "recrutements": Chiffre(
        "+1 500 magistrats",
        "Recrutements programmés",
        "Et +1 800 greffiers d'ici 2027, prévus par la loi de programmation du"
        " 20 novembre 2023. La promesse porte sur les recrutements, pas sur les"
        " effectifs en poste : les départs s'en déduisent.",
        "legifrance", "2023-2027",
    ),
    # -- les délais ----------------------------------------------------------
    "delai_civil": Chiffre(
        "environ 14 mois",
        "Une affaire civile en première instance",
        "Durée moyenne des affaires civiles terminées devant les tribunaux"
        " judiciaires. La moyenne masque des écarts considérables d'un"
        " contentieux et d'une juridiction à l'autre.",
        "justice", "2023",
    ),
    "delai_appel": Chiffre(
        "environ 16 mois",
        "Puis l'appel",
        "Durée moyenne d'une procédure civile devant une cour d'appel, qui"
        " s'ajoute à la première instance.",
        "justice", "2023",
    ),
    "delai_prudhommes": Chiffre(
        "plus de 15 mois",
        "Un litige prud'homal",
        "Durée moyenne devant un conseil de prud'hommes, hors référé — et près"
        " de six décisions sur dix y sont frappées d'appel.",
        "justice", "2023",
    ),
    "delai_instruction": Chiffre(
        "environ 3 ans",
        "Une information judiciaire",
        "Durée moyenne d'un dossier confié à un juge d'instruction, de"
        " l'ouverture à la clôture.",
        "justice", "2023",
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
    ),
    "classement_auteur": Chiffre(
        "environ 2 plaintes sur 3",
        "Classées faute d'auteur identifié",
        "Part des affaires reçues par les parquets qui sont classées sans suite"
        " parce que l'auteur n'a pas été retrouvé : l'essentiel de l'écart"
        " entre ce que vivent les victimes et le taux de réponse pénale.",
        "justice", "2023",
    ),
    "peines_attente": Chiffre(
        "des dizaines de milliers",
        "Peines de prison ferme non exécutées",
        "Stock de peines d'emprisonnement ferme prononcées et non mises à"
        " exécution, régulièrement relevé par la Cour des comptes et par les"
        " rapports budgétaires du Parlement. Le ministère ne publie pas de"
        " série continue : c'est en soi le problème.",
        "comptes", "2022-2024",
    ),
    "recidive": Chiffre(
        "59 %",
        "Recondamnés dans les cinq ans",
        "Part des personnes sorties de prison qui sont recondamnées dans les"
        " cinq ans ; 46 % sont réincarcérées. Étude de référence du ministère"
        " de la Justice, non réactualisée depuis.",
        "justice", "2011",
    ),
    "incriminations": Chiffre(
        "plus de 10 000",
        "Infractions pénales en vigueur",
        "Estimation courante du nombre d'incriminations, réparties entre le"
        " code pénal et plusieurs dizaines d'autres codes. Aucune"
        " administration n'en tient le compte exact — c'est l'un des faits les"
        " plus éloquents de ce site.",
        "justice", "estimation",
    ),
    # -- la prison -----------------------------------------------------------
    "detenus": Chiffre(
        "plus de 80 000",
        "Personnes détenues",
        "Record historique, franchi puis dépassé depuis 2024. L'effectif est"
        " publié chaque mois.",
        "penitentiaire", "2025",
    ),
    "places": Chiffre(
        "environ 62 000",
        "Places opérationnelles",
        "Capacité réelle des établissements pénitentiaires, cellules"
        " indisponibles déduites.",
        "penitentiaire", "2025",
    ),
    "densite": Chiffre(
        "plus de 130 %",
        "Densité carcérale",
        "Rapport des détenus aux places sur l'ensemble du parc ; il dépasse"
        " 150 % dans les maisons d'arrêt, où sont les prévenus et les courtes"
        " peines.",
        "penitentiaire", "2025",
    ),
    "matelas": Chiffre(
        "plusieurs milliers",
        "Matelas au sol",
        "Personnes détenues dormant sur un matelas posé à même le sol, faute de"
        " lit. Le chiffre est publié avec la statistique mensuelle.",
        "penitentiaire", "2025",
    ),
    "cedh": Chiffre(
        "30 janvier 2020",
        "Condamnation de la France",
        "Arrêt J.M.B. et autres c. France : la Cour européenne des droits de"
        " l'homme juge les conditions de détention contraires à l'article 3 de"
        " la Convention et demande à la France de résorber la surpopulation.",
        "cedh", "2020",
    ),
    "cout_detention": Chiffre(
        "de l'ordre de 120 €",
        "Coût d'une journée de détention",
        "Coût moyen par personne détenue et par jour, tous régimes confondus —"
        " soit plus de 40 000 € par an et par place occupée.",
        "comptes", "2023",
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
    ),
    "aide_juridictionnelle": Chiffre(
        "environ 600 M€",
        "Aide juridictionnelle",
        "Dépense annuelle de l'État pour l'accès au juge des justiciables sans"
        " ressources suffisantes, pour près d'un million d'admissions.",
        "justice", "2024",
    ),
    "confiance": Chiffre(
        "environ 1 sur 2",
        "Français qui font confiance à la justice",
        "Part des personnes interrogées déclarant faire confiance à"
        " l'institution judiciaire. Le chiffre varie d'une vague à l'autre ;"
        " sa stabilité à ce niveau, elle, ne varie pas.",
        "cevipof", "2024-2025",
    ),
}


def chiffre(cle: str) -> Chiffre:
    return CHIFFRES[cle]


def valeur(cle: str) -> str:
    """La valeur seule, pour l'écrire au fil d'une phrase, en or."""
    return f'<strong class="cle-texte">{escape(CHIFFRES[cle].valeur)}</strong>'


def fiche(cle: str) -> str:
    """Une fiche : la valeur, ce qu'elle mesure, la précision et la source."""
    c = CHIFFRES[cle]
    s = SOURCES[c.source]
    return (
        '<div class="fiche">'
        f'<p class="valeur">{escape(c.valeur)}</p>'
        f'<p class="etiquette">{escape(c.libelle)}</p>'
        f'<p class="precision">{escape(c.precision)} '
        f'<a href="{s.url}">{escape(s.nom.split(" — ")[0])}</a>, {escape(c.annee)}.</p>'
        "</div>"
    )


def fiches(*cles: str, reperes: bool = True) -> str:
    classe = "fiches reperes" if reperes else "fiches"
    return f'<div class="{classe}">' + "".join(fiche(cle) for cle in cles) + "</div>"
