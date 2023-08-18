class Gateau:
    """Cette classe contient les ingrédients ainsi que la recette d'un gâteau"""

    def __init__(self, nom, tps_cuisson, ingredients, etapes_recette, createur):
        self.nom = nom
        self.tps_cuisson = tps_cuisson
        self.ingredients = ingredients
        self.etapes_recette = etapes_recette
        self.createur = createur

    def afficher_ingredients(self):
        print("Ingrédients de la recette: ")
        print("\n".join(self.ingredients))
        print()

    def afficher_etapes_recette(self):
        print("Étapes de la recette: ")
        print("\n".join(self.etapes_recette))
        print()


ingredients = [
    "Farine",
    "Oeufs",
    "Beurre",
    "Sucre",
    "Citron"
]
etapes_recette = [
    "Réaliser la pâte",
    "Enfourner le fond de pâte",
    "Réaliser la crème au citron",
    "Garnisser la tarte avec la crème au citron"
]
gateau = Gateau("Tarte aux citrons", 30, ingredients, etapes_recette, "Moi")

gateau.afficher_ingredients()
gateau.afficher_etapes_recette()