annuaire_telephonique = dict()

def voir_annuaire():
    print("Contenu de l'annuaire:")
    for nom, numero in annuaire_telephonique.items():
        print(f"{nom}: {numero}")
    print()

def ajouter_contact(nom, numero):
    if nom in annuaire_telephonique:
        print("Attention ce nom existe déjà")
        return
    
    annuaire_telephonique[nom] = numero

def editer_contact(nom, nouveau_numero):
    if nom not in annuaire_telephonique:
        print(f"Le nom {nom} n'existe pas dans le dictionnaire")
        return
    
    annuaire_telephonique[nom] = nouveau_numero

def supprimer_contact(nom):
    if nom not in annuaire_telephonique:
        print(f"Le nom {nom} n'existe pas dans le dictionnaire")
        return
    
    del annuaire_telephonique[nom]

def rechercher_numero(nom):
    if nom not in annuaire_telephonique:
        print(f"Le contact {nom} n'est pas présent dans l'annuaire")
        return

    return annuaire_telephonique[nom]


ajouter_contact("John", "123456")
ajouter_contact("Jane", "123890")
ajouter_contact("Arthur", "123890")
voir_annuaire()
print("Numero de John ", rechercher_numero("John"))
editer_contact("John", "999999")
print("Numero de John ", rechercher_numero("John"))
supprimer_contact("Arthur")
voir_annuaire()
