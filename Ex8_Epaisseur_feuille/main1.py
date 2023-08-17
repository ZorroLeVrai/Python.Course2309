epaisseur_papier_mm = 0.1
epaisseur_cible_mm = 1000 * 400

nombre_de_plis = 0
epaisseur_actuelle = epaisseur_papier_mm
while epaisseur_actuelle <= epaisseur_cible_mm:
    epaisseur_actuelle *= 2
    nombre_de_plis += 1

print(f"Nombre de plis nécessaires: {nombre_de_plis}")
