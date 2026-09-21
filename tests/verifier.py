#!/usr/bin/env python3
"""Les vérifications du site. Aucune dépendance : ``python3 tests/verifier.py``.

Elles portent sur ce qui, dans un site de programme, se dégrade sans qu'on
s'en aperçoive : un chiffre qui perd sa source, une mesure sans véhicule
juridique, un lien interne vers une page renommée, une balise mal fermée, et
surtout un HTML publié qui ne correspond plus au texte du dépôt.
"""

from __future__ import annotations

import re
import sys
import unittest
from html import escape
from html.parser import HTMLParser
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from justice import gabarit, site  # noqa: E402
from justice.chiffres import CHIFFRES, SOURCES  # noqa: E402

#: Les balises qui n'ont pas de fermeture, et qu'un contrôle d'équilibre doit
#: ignorer sous peine de croire le document cassé.
ORPHELINES = {"meta", "link", "br", "hr", "img", "input", "source", "col"}


class Equilibre(HTMLParser):
    """Vérifie que les balises se ferment, et dans l'ordre."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.pile: list[str] = []
        self.fautes: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag not in ORPHELINES:
            self.pile.append(tag)

    def handle_endtag(self, tag):
        if tag in ORPHELINES:
            return
        if not self.pile:
            self.fautes.append(f"</{tag}> sans ouverture")
        elif self.pile[-1] != tag:
            self.fautes.append(f"</{tag}> alors que <{self.pile[-1]}> est ouvert")
            self.pile.pop()
        else:
            self.pile.pop()


class Pages(unittest.TestCase):
    """Ce que chaque page doit porter."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.rendus = {fichier: site.rendre(fichier) for fichier in site.PAGES}

    def test_chaque_page_se_construit(self):
        for fichier, html in self.rendus.items():
            with self.subTest(fichier=fichier):
                self.assertTrue(html.startswith("<!doctype html>"))
                self.assertGreater(len(html), 4000, "page suspicieusement courte")

    def test_un_seul_titre_de_premier_niveau(self):
        for fichier, html in self.rendus.items():
            with self.subTest(fichier=fichier):
                self.assertEqual(html.count("<h1>"), 1)

    def test_balises_equilibrees(self):
        for fichier, html in self.rendus.items():
            with self.subTest(fichier=fichier):
                controle = Equilibre()
                controle.feed(html)
                self.assertEqual(controle.fautes, [], f"{fichier} : balisage")
                self.assertEqual(controle.pile, [], f"{fichier} : balises non fermées")

    def test_aucune_requete_vers_un_tiers(self):
        """Ni script, ni police, ni image chargés ailleurs que sur le site.

        Un lecteur de programme politique ne doit rien apprendre à personne.
        Les liens hypertexte vers l'extérieur restent permis : ce sont des
        liens, ils ne partent qu'au clic.
        """
        for fichier, html in self.rendus.items():
            with self.subTest(fichier=fichier):
                self.assertFalse("<script" in html, f"{fichier} : script")
                for attribut in ("src=", "@import"):
                    self.assertFalse(f'{attribut}"http' in html,
                                     f"{fichier} : ressource externe")
                for lien in re.findall(r'<link[^>]+href="([^"]+)"', html):
                    self.assertFalse(lien.startswith("http"),
                                     f"{fichier} : ressource externe {lien}")

    def test_liens_internes_existants(self):
        """Tout lien relatif mène à un fichier du dépôt, et toute ancre existe."""
        for fichier, html in self.rendus.items():
            ancres = set(re.findall(r'id="([^"]+)"', html))
            for cible in re.findall(r'href="([^"]+)"', html):
                if cible.startswith(("http", "mailto:")):
                    continue
                with self.subTest(fichier=fichier, cible=cible):
                    if cible.startswith("#"):
                        self.assertTrue(cible[1:] in ancres, f"{fichier} : ancre {cible} absente")
                        continue
                    page, _, ancre = cible.partition("#")
                    self.assertTrue((RACINE / page).exists(), "fichier absent")
                    if ancre:
                        cible_html = self.rendus.get(page, "")
                        self.assertTrue(f'id="{ancre}"' in cible_html,
                                        f"{fichier} : {cible} sans ancre")

    def test_navigation_et_registre_concordent(self):
        """Une page hors du bandeau est une page que personne n'atteint."""
        du_bandeau = {fichier for fichier, _ in gabarit.LIENS}
        du_registre = set(site.PAGES) - {"index.html"}
        self.assertEqual(du_bandeau, du_registre)

    def test_description_presente_et_utile(self):
        for fichier in site.PAGES:
            with self.subTest(fichier=fichier):
                description = site.module(fichier).DESCRIPTION
                self.assertGreater(len(description), 80)
                self.assertLess(len(description), 400)


class Chiffres(unittest.TestCase):
    """Un chiffre sans source est une opinion."""

    def test_chaque_chiffre_porte_une_source_et_une_annee(self):
        for cle, chiffre in CHIFFRES.items():
            with self.subTest(chiffre=cle):
                self.assertIn(chiffre.source, SOURCES)
                self.assertTrue(chiffre.annee)
                self.assertTrue(chiffre.precision)
                self.assertGreater(len(chiffre.precision), 40,
                                   "la précision doit dire ce que le chiffre ne dit pas")

    def test_chaque_source_est_consultable(self):
        for cle, source in SOURCES.items():
            with self.subTest(source=cle):
                self.assertTrue(source.url.startswith("https://"))
                self.assertTrue(source.detail)

    def test_chaque_chiffre_est_recense_sur_la_page_des_sources(self):
        page = site.rendre("sources.html")
        for cle, chiffre in CHIFFRES.items():
            with self.subTest(chiffre=cle):
                self.assertTrue(escape(chiffre.libelle) in page,
                                f"{cle} : absent de la page des sources")

    def test_aucun_chiffre_orphelin(self):
        """Un chiffre déclaré et jamais cité vieillit sans que personne le voie.

        Un chiffre se cite de deux manières : en fiche, et son libellé paraît ;
        au fil d'une phrase, et c'est alors sa valeur seule. Les deux comptent.
        """
        ailleurs = "".join(
            site.rendre(fichier) for fichier in site.PAGES if fichier != "sources.html"
        )
        for cle, chiffre in CHIFFRES.items():
            with self.subTest(chiffre=cle):
                self.assertTrue(
                    escape(chiffre.libelle) in ailleurs
                    or escape(chiffre.valeur) in ailleurs,
                    f"{cle} : déclaré mais cité sur aucune page",
                )


class Programme(unittest.TestCase):
    """Une mesure sans véhicule ni coût est un souhait."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.page = site.rendre("programme.html")

    def test_vingt_mesures(self):
        self.assertEqual(self.page.count('class="mesure"'), 20)

    def test_chaque_mesure_porte_son_vehicule_et_son_cout(self):
        self.assertEqual(self.page.count("<b>Véhicule</b>"), 20)
        self.assertEqual(self.page.count("<b>Coût</b>"), 20)

    def test_numerotation_continue(self):
        rangs = re.findall(r'<p class="rang">(\d\d)</p>', self.page)
        self.assertEqual(rangs, [f"{n:02d}" for n in range(1, 21)])


class Publication(unittest.TestCase):
    """Le HTML publié doit être celui que produit le code publié."""

    def test_les_fichiers_sont_a_jour(self):
        for fichier in site.PAGES:
            with self.subTest(fichier=fichier):
                chemin = RACINE / fichier
                self.assertTrue(chemin.exists(), "page jamais construite")
                self.assertTrue(
                    chemin.read_text(encoding="utf-8") == site.rendre(fichier),
                    f"{fichier} n'est pas à jour : relancez"
                    " « python3 scripts/construire.py »",
                )

    def test_les_ressources_de_la_charte_sont_presentes(self):
        for ressource in (
            "moteur/style.css",
            "moteur/complement.css",
            "moteur/icone.svg",
            "moteur/polices/public-sans-latin.woff2",
            "moteur/polices/instrument-serif-latin.woff2",
        ):
            with self.subTest(ressource=ressource):
                self.assertTrue((RACINE / ressource).exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
