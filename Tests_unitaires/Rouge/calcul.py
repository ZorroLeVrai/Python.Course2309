import json

JSON_PATH = r"D:\Users\Amine\Prgm\Python\Python.Course2309\Tests_unitaires\config.json"


class Calcul:
    def __init__(self, codePays=None):
        self.__load_configuration()

        if codePays == None:
            codePays = self.codePays

        if codePays in self.tva_dico:
            self.taux_tva = self.tva_dico[codePays]
        else:
            self.taux_tva = self.tva_defaut

    def __load_configuration(self):
        try:
            with open(JSON_PATH, 'r') as json_file:
                json_data = json.load(json_file)

            self.codePays = json_data["codePays"]
            tva_data = json_data["tva"]
            self.tva_defaut = tva_data["defaut"]
            self.tva_dico = self.__getTvaList(tva_data["valeurs"])
        except FileNotFoundError:
            print(f"File not found: {JSON_PATH}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def __getTvaList(self, valeurs_tva):
        tva_dico = dict()

        for item in valeurs_tva:
            code_pays = item["codePays"]
            valeur_tva = item["taux"]
            tva_dico[code_pays] = valeur_tva

        return tva_dico

    def calcul_tva(self, prix):
        return prix*self.taux_tva / 100

    def calcul_ttc(self, prix):
        return prix + self.calcul_tva(prix)
