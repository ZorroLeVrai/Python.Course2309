liste_nom = set()
deco_menu = "="*3

def deco_text(text):
    return f"{deco_menu} {text} {deco_menu}"

def afficher_liste_noms():
    print("\n".join(liste_nom))

def ajouter_nom_famille():
    nom_famille = input("Nom de famille: ")
    liste_nom.add(nom_famille)

def editer_nom_famille():
    ancien_nom = input("Entrez l'ancien nom de famille: ")
    if ancien_nom not in liste_nom:
        print("Ce nom n'existe pas")
        return
    nouveau_nom = input("Entrez le nouveau nom de famille: ")
    liste_nom.remove(ancien_nom)
    liste_nom.add(nouveau_nom)
    print(f"{ancien_nom} remplacé par {nouveau_nom}")

def supprimer_nom_famille():
    ancien_nom = input("Entrez le nom de famille à supprimer: ")
    liste_nom.discard(ancien_nom)

def choix_option():
    print(f"""{deco_menu} MENU PRINCIPAL {deco_menu}
1. Voir les noms de famille
2. Ajouter un nom de famille
3. Editer un nom de famille
4. Supprimer un nom de famille
0. Quitter le programme""")
    while True:
        choix = input("Votre choix: ")
        try:
            option = int(choix)
            if 0 <= option <= 5:
                return option
            print("Option non disponible. L'option doit être entre >= 0 et <= 4")
        except ValueError:
            print("L'option doit être un entier")

while True:
    option = choix_option()

    match option:
        case 0:
            print("Fin du programme")
            break
        case 1:
            print(deco_text("LISTE NOMS DE FAMILLE"))
            afficher_liste_noms()
        case 2:
            print(deco_text("AJOUTER UN NOM DE FAMILLE"))
            ajouter_nom_famille()
        case 3:
            print(deco_text("EDITER UN NOM DE FAMILLE"))
            editer_nom_famille()
        case 4:
            print(deco_text("SUPPRIMER UN NOM DE FAMILLE"))
            supprimer_nom_famille()
        case _:
            print("Option non valide")
