from Vert import MAIN_DIRECTORY, JSON_PATH
from Vert import FullPath
from Vert import FileLoader
from Vert import Configuration
from Vert import CalculateurPrix


config_full_path = FullPath(
    MAIN_DIRECTORY).get_full_path_from_relative_path(JSON_PATH)
fileLoader = FileLoader(config_full_path)
configuration = Configuration(fileLoader)
tva_actuelle = configuration.get_current_tva()
tva_allemagne = configuration.get_tva("DE")

print("Prix ttc defaut", CalculateurPrix(tva_actuelle).calcul_ttc(100))
print("Prix ttc DE", CalculateurPrix(tva_allemagne).calcul_ttc(100))
