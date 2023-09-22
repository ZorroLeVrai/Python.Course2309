class CalculTtc:
    def __init__(self, config, codePays=None):
        if codePays == None:
            codePays = config.codePays

        if codePays in config.tva_dico:
            self.taux_tva = config.tva_dico[codePays]
        else:
            self.taux_tva = config.tva_defaut

    def calcul_tva(self, prix):
        return prix*self.taux_tva / 100

    def calcul_ttc(self, prix):
        return prix + self.calcul_tva(prix)
