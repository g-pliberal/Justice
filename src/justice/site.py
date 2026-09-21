"""Le registre des pages : quel module écrit quel fichier.

L'ordre est celui du parcours de lecture, qui est aussi celui du bandeau. Le
fichier est l'adresse : le site est un dossier de fichiers HTML, servi tel
quel, sans routeur ni serveur.
"""

from __future__ import annotations

from importlib import import_module
from pathlib import Path
from types import ModuleType

from . import gabarit

#: ``fichier -> module``. Les fichiers listés ici doivent être exactement ceux
#: du bandeau, plus l'accueil — un test le vérifie : une page absente de la
#: navigation est une page que personne n'atteint.
PAGES: dict[str, str] = {
    "index.html": "accueil",
    "etat-des-lieux.html": "etat_des_lieux",
    "penale.html": "penale",
    "prison.html": "prison",
    "civile.html": "civile",
    "libertes.html": "libertes",
    "programme.html": "programme",
    "sources.html": "sources",
}


def module(fichier: str) -> ModuleType:
    return import_module(f".pages.{PAGES[fichier]}", package="justice")


def rendre(fichier: str) -> str:
    """Le HTML complet d'une page."""
    page = module(fichier)
    return gabarit.document(
        fichier=fichier,
        titre=page.TITRE,
        description=page.DESCRIPTION,
        corps=page.corps(),
    )


def construire(racine: Path) -> list[Path]:
    """Écrit les huit pages à la racine du dépôt, et rend leurs chemins."""
    ecrits = []
    for fichier in PAGES:
        chemin = racine / fichier
        chemin.write_text(rendre(fichier), encoding="utf-8")
        ecrits.append(chemin)
    return ecrits
