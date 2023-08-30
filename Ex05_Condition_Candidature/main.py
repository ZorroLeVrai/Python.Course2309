age = int(input("Saisir age: "))
salaire = float(input("Saisir le salaire souhaité: "))
annees_experience = int(input("Saisir le nombre d'années d'expérience: "))

if age < 30:
    print("L’âge minimum pour le poste est 30 ans.")
if salaire > 40_000:
    print("Le salaire maximum possible est 40 000 euros.")
if annees_experience < 5:
    print("Le nombre d’années d’expérience minimum est de 5 ans.")
