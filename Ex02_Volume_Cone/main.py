import math

# Les entrées de l'utilisateur / utilisatrice
rayon_cm = float(input("Entrez le rayon (en cm): "))
hauteur_cm = float(input("Entrez la hauteur (en cm): "))

#Les calculs
base_cm2 = math.pi*rayon_cm**2
volume_cm3 = hauteur_cm*base_cm2 / 3

#Affchage du résultat
print(f"Le volume est de {round(volume_cm3, 2)} cm\u00b3")
