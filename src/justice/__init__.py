"""Le site « Justice » du Parti libéral français.

Un site de programme, et non une application : huit pages statiques, écrites
ici en Python et déposées en HTML à la racine du dépôt par
``scripts/construire.py``. Il n'y a ni serveur, ni script côté navigateur —
une page de programme doit s'ouvrir sur un téléphone en 3G, se lire sans
JavaScript et s'imprimer.

Le texte vit dans ``pages/``, les chiffres dans ``chiffres.py``, la mise en
page dans ``gabarit.py``. La séparation n'est pas décorative : un chiffre cité
dans une page doit exister dans ``chiffres.py``, donc porter une source et une
année, et la page « Sources » le recense sans qu'on ait à y penser.
"""

__all__ = ["chiffres", "gabarit", "pages", "site"]
