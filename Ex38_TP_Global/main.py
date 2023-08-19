from enum import Enum
from short_path import short_path

class Ville:
    def __init__(self, nom):
        self.nom = nom
        # self.out_edges contient les transports à partir de cette ville.
        self.out_edges = []

    def ajouter_transport(self, ville_arrivee, nom, cout, temps):
        self.out_edges.append(Transport(self, ville_arrivee, nom, cout, temps))    

class TypeTransport(Enum):
    TRAIN = 1
    BUS = 2

class Transport:
    def __init__(self, ville_depart, ville_arrivee, nom, cout, temps):
        self.tail = ville_depart
        self.head = ville_arrivee
        self.nom = nom
        self.cout = cout
        self.temps = temps

    def __repr__(self):
        return f"{self.tail.nom} => {self.head.nom} - {self.nom} cout:{self.cout} temps:{self.temps}"

#Initialiser les villes
lyon = Ville("Lyon")
strasbourg = Ville("Strasbourg")
paris = Ville("Paris")
lille = Ville("Lille")

#Initialiser les transports
lyon.ajouter_transport(strasbourg, TypeTransport.TRAIN, 50, 160)
lyon.ajouter_transport(paris, TypeTransport.TRAIN, 100, 120)
strasbourg.ajouter_transport(lille, TypeTransport.BUS, 20, 180)
paris.ajouter_transport(lille, TypeTransport.TRAIN, 60, 60 )
paris.ajouter_transport(lille, TypeTransport.BUS, 10, 100 )

path = short_path(lyon, lille, lambda transport: transport.temps)
print(path)