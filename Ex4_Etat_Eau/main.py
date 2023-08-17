temp = float(input("Entrez la température de l'eau: "))
etat_eau = ""
if temp <= 0:
    etat_eau = "solide"
elif temp < 100:
    etat_eau = "liquide"
else:
    etat_eau = "gazeux"

print(f"Etat {etat_eau}")
