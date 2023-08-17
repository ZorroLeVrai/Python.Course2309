population_initiale = float(input("Entrez la population initiale: "))
taux_accroissement = float(
    input("Entrez un taux d'accroissement (en pourcentage): "))
population_cible = float(input("Entrez la population cible: "))

population_actuelle = population_initiale
nombre_annees = 0
while population_actuelle <= population_cible:
    population_actuelle *= 1 + taux_accroissement / 100
    nombre_annees += 1

print(f"Il faut {nombre_annees} pour atteindre ou dépasser la population cible")
