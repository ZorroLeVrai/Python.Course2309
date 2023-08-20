class EtreVivant:
    def __init__(self):
        self.point_de_vie = 100

    def se_nourrir(self):
        self.point_de_vie += 1

class Animal(EtreVivant):
    def dormir(self):
        self.point_de_vie += 1

    def se_nourrir(self):
        print("Animal.se_nourrir")
        self.point_de_vie += 5

class Carnivore(EtreVivant):
    def chasser(self):
        self.point_de_vie -= 1
    
    def se_nourrir(self):
        print("Carnivore.se_nourrir")
        self.point_de_vie += 10

class Toutou(Animal, Carnivore):
    pass

toutou = Toutou()
toutou.se_nourrir()
print(toutou.point_de_vie)