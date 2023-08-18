from os.path import isfile
import json

fichier_sauvegarde = "Contacts.json"
annuaire_telephonique = dict()
deco_menu = "="*3

def deco_text(text):
    return f"{deco_menu} {text} {deco_menu}"

def afficher_contacts():
    for nom, numero in annuaire_telephonique.items():
        print(f"{nom}: {numero}")

def saisir_numero(message):
    numero_str = input(message)
    if not numero_str.isdigit():
        print("Le numéro de téléphone doit contenir que des chiffres")
        return None
    return numero_str

def ajouter_contact():
    nom = input("Entrez le nom du contact: ")
    numero_str = saisir_numero("Entrez le numéro du contact: ")
    if numero_str is None:
        return
    
    annuaire_telephonique[nom] = numero_str
    print(f"Le contact a été enregistré {nom}: {numero_str}")

def editer_contact():
    nom = input("Entrez le nom du contact à éditer: ")
    if nom not in annuaire_telephonique:
        print(f"Le contact {nom} n'est pas présent dans l'annuaire")
        return
    numero_str = saisir_numero("Entrez le nouveau numéro du contact: ")
    if numero_str is None:
        return
    
    annuaire_telephonique[nom] = numero_str
    print(f"Le contact a été mis à jour {nom}: {numero_str}")

def supprimer_contact():
    nom = input("Entrez le nom du contact à supprimer: ")
    if nom not in annuaire_telephonique:
        print(f"Le contact {nom} n'est pas présent dans l'annuaire")
        return
    
    del annuaire_telephonique[nom]
    print(f"Le contact {nom} a été supprimé")

def rechercher_numero():
    nom = input("Entrez le nom du contact à rechercher: ")
    if nom not in annuaire_telephonique:
        print(f"Le contact {nom} n'est pas présent dans l'annuaire")
        return
    
    print(f"Le numéro est: {annuaire_telephonique[nom]}")


def choix_option():
    print(f"""{deco_text("MENU PRINCIPAL")}
1. Voir l'annuaire
2. Ajouter un contact
3. Editer un contact
4. Supprimer un contact
5. Rechercher un numéro de téléphone
0. Quitter le programme""")
    while True:
        choix = input("Votre choix: ")
        try:
            option = int(choix)
            if 0 <= option <= 5:
                return option
            print("Option non disponible. L'option doit être entre >= 0 et <= 5")
        except ValueError:
            print("L'option doit être un entier")

def chargement_contacts():
    if isfile(fichier_sauvegarde):
        with open(fichier_sauvegarde, "r") as fichier:
            return json.load(fichier)
    
    return dict()

def sauvegarder_contacts():
    with open(fichier_sauvegarde, "w") as fichier:
        json.dump(annuaire_telephonique, fichier, indent = 2)

def run():
    while True:
        option = choix_option()

        match option:
            case 0:
                print("Fin du programme")
                sauvegarder_contacts()
                break
            case 1:
                print(deco_text("LISTE DES CONTACTS"))
                afficher_contacts()
            case 2:
                print(deco_text("AJOUTER UN CONTACT"))
                ajouter_contact()
            case 3:
                print(deco_text("EDITER UN CONTACT"))
                editer_contact()
            case 4:
                print(deco_text("SUPPRIMER UN NOM DE FAMILLE"))
                supprimer_contact()
            case 5:
                print(deco_text("RECHERCHER UN NUMÉRO DE TÉLÉPHONE"))
                rechercher_numero()
            case _:
                print("Option non valide")

annuaire_telephonique = chargement_contacts()
run()