from Rouge import Calcul

calculatriceTtcDefault = Calcul()
calculatriceTtcAllemagne = Calcul("DE")
print("TVA par défaut", calculatriceTtcDefault.calcul_tva(100))
print("TVA par défaut", calculatriceTtcAllemagne.calcul_tva(100))
