def calculer_valeurs(a,b):
    return (a+b, a-b, a/b, a*b)

val1 = float(input("Entrez la première valeur: "))
val2 = float(input("Entrez la deuxième valeur: "))
(somme, difference, quotient, produit) = calculer_valeurs(val1, val2)

print(f"La somme est {somme}")
print(f"La différence est {difference}")
print(f"Le quotient est {quotient}")
print(f"Le produit est {produit}")