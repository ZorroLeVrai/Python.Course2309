def additionner(a,b):
    return f"La somme est {a+b}"

def soustraire(a,b):
    return f"La différence est {a-b}"

def diviser(a,b):
    return f"Le quotient est {a/b}"

def multiplier(a,b):
    return f"Le produit est {a*b}"

val1 = float(input("Entrez la première valeur: "))
val2 = float(input("Entrez la deuxième valeur: "))

for fonction in [additionner, soustraire, diviser, multiplier]:
    print(fonction(val1, val2))