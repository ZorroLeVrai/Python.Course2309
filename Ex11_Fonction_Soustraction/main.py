def soustraire(a, b):
    return a-b


def formater_resultat(a, b, resultat):
    return f"{a} moins {b} égale {resultat}"


def ecrire_resultat(a, b):
    resultat = soustraire(a, b)
    print(formater_resultat(a, b, resultat))


val1 = float(input("Entrez la première valeur: "))
val2 = float(input("Entrez la deuxième valeur: "))
ecrire_resultat(val1, val2)
