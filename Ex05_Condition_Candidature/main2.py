age = int(input("Saisir age: "))
salaire = float(input("Saisir le salaire souhaité: "))
annees_experience = int(input("Saisir le nombre d'années d'expérience: "))

condition_age = age >= 30
condition_salaire = salaire <= 40000
condition_experience = annees_experience >= 5

if not condition_age:
    print("L'âge minimum pour le poste est 30 ans.")

if not condition_salaire:
    print("Le salaire maximum possible est 40 000 euros.")

if not condition_experience:
    print("Le nombre d'années d'expérience minimum est de 5 ans.")

if condition_age and condition_salaire and condition_experience:
    print("Toutes les conditions sont respectées pour le poste")
