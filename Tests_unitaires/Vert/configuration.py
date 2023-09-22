import json
from .file_loader import FileLoader


CONFIG_CODE_PAYS = "codePays"
CONFIG_TVA_PAR_DEFAUT = "defaut"
CONFIG_TVA = "tva"
VALEURS_TVA = "valeurs"


class Configuration:
    def __init__(self, file_loader: FileLoader):
        self.__config_data = json.loads(file_loader.configuration_content)
        self.__codePays: str = self.__config_data[CONFIG_CODE_PAYS]
        tva_data = self.__config_data[CONFIG_TVA]
        self.__tva_defaut: float = tva_data[CONFIG_TVA_PAR_DEFAUT]
        self.__tva_list: dict[str, float] = self.__get_tva_list(
            tva_data[VALEURS_TVA])

    def __get_tva_list(self, valeurs_tva):
        tva_dico: dict[str, float] = dict()

        for item in valeurs_tva:
            code_pays: str = item["codePays"]
            valeur_tva: float = item["taux"]
            tva_dico[code_pays] = valeur_tva

        return tva_dico

    def get_tva(self, pays: str) -> float:
        tva = self.__tva_list.get(pays)
        if tva == None:
            tva = self.__tva_defaut
        return tva

    def get_current_tva(self) -> float:
        return self.get_tva(self.__codePays)
