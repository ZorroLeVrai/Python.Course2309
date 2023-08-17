epaisseur_cible = 0.1
epaisseur_actuelle = 1000 * 400

nombre_de_plis = 0
while epaisseur_actuelle >= epaisseur_cible:
    epaisseur_actuelle /= 2
    nombre_de_plis += 1

print(f"Nombre de plis nécessaires: {nombre_de_plis}")
