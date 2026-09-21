#!/usr/bin/env python3
"""Construit le site : huit fichiers HTML à la racine du dépôt.

    python3 scripts/construire.py

Les fichiers produits sont versionnés, et c'est voulu : le dépôt est servi tel
quel par GitHub Pages, sans étape de construction chez l'hébergeur. Le HTML
engagé doit donc toujours être celui que produit le code engagé — un test le
vérifie, et la construction se relance après toute modification du texte.
"""

from __future__ import annotations

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from justice.site import construire  # noqa: E402


def main() -> int:
    for chemin in construire(RACINE):
        print(f"écrit  {chemin.relative_to(RACINE)}  "
              f"({chemin.stat().st_size // 1024} Ko)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
