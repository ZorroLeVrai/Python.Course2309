import os.path
import codecs
import csv

nom_fichier = "produit.csv"
delimiteur_csv = ";"

def ajouter_produit(titre, prix, stock):
    fichier_existe = os.path.exists(nom_fichier)

    with codecs.open(nom_fichier, "a", "utf-8") as fichier:
        csv_writer = csv.writer(fichier, delimiter=delimiteur_csv)
        if not fichier_existe:
            csv_writer.writerow(["Titre", "Prix", "Quantité"])
        csv_writer.writerow([titre, prix, stock])

titre = input("Entrez le nom du produit: ")
prix = float(input("Entrez le prix du produit: "))
stock = int(input("Entrer le nombre de produits: "))

ajouter_produit(titre, prix, stock)
