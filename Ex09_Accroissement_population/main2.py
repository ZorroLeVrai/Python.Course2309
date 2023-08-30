from math import log

population_initiale = float(input("Entrez la population initiale: "))
taux_accroissement = float(
    input("Entrez un taux d'accroissement (en pourcentage): "))
population_cible = float(input("Entrez la population cible: "))

nb_annees = log(population_cible / population_initiale) / \
    log(1 + taux_accroissement / 100)
print(
    f"Il faut exactement {nb_annees:0.2f} pour atteindre ou dépasser la population cible")
