position_modules = ['A', 'B', 'C', 'D', 'E', 'F']

def echange_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]

def panne_moteur(list):
    premier_element = list.pop(0)
    list.append(premier_element)

def passe_en_tete(list):
    echange_positions(list, 0, 1)

def sauve_honneur(list):
    derniere_position = len(list) - 1
    echange_positions(list, derniere_position, derniere_position-1)

def tir_blaster(list):
    return list.pop(0)

def retour_innatendu(list, module):
    list.append(module)

#déroulement de la course
panne_moteur(position_modules)
passe_en_tete(position_modules)
sauve_honneur(position_modules)
module_elimine = tir_blaster(position_modules)
retour_innatendu(position_modules, module_elimine)

print("Positions en fin de course")
print(position_modules)