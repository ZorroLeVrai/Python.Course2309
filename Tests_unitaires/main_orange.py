from Orange import Configuration
from Orange import CalculTtc
from Orange import JSON_PATH

configuration = Configuration(JSON_PATH)
calculatriceTtcDefault = CalculTtc(configuration)
calculatriceTtcAllemagne = CalculTtc(configuration, "DE")
print("TVA par défaut", calculatriceTtcDefault.calcul_tva(100))
print("TVA par défaut", calculatriceTtcAllemagne.calcul_tva(100))
