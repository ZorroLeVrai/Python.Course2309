import json


class Configuration:
    def __init__(self, json_path):
        try:
            with open(json_path, 'r') as json_file:
                json_data = json.load(json_file)

            self.codePays = json_data["codePays"]
            tva_data = json_data["tva"]
            self.tva_defaut = tva_data["defaut"]
            self.tva_dico = self.__getTvaList(tva_data["valeurs"])
        except FileNotFoundError:
            print(f"File not found: {json_path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def __getTvaList(self, valeurs_tva):
        tva_dico = dict()

        for item in valeurs_tva:
            code_pays = item["codePays"]
            valeur_tva = item["taux"]
            tva_dico[code_pays] = valeur_tva

        return tva_dico
