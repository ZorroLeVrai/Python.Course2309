class CalculateurPrix:
    def __init__(self, taux_tva: float):
        self.__taux_tva = taux_tva

    def calcul_tva(self, prix: float):
        return prix*self.__taux_tva / 100

    def calcul_ttc(self, prix: float):
        return prix + self.calcul_tva(prix)
