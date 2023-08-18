def imprimer_resultat(titre):
    def imprimer_resultat_interne(func):
        def imprimer_resultat_locale(*args, **kwargs):
            resultat = func(*args, **kwargs)
            print(f"{titre}: {resultat}")
            return resultat

        return imprimer_resultat_locale
    return imprimer_resultat_interne

class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
    
    @imprimer_resultat("Perimetre")
    def perimetre(self):
        return 2 * (self.largeur + self.longueur)
    
    @imprimer_resultat("Surface")
    def surface(self):
        return self.largeur * self.longueur
    
class Parallelepipede(Rectangle):
    def __init__(self, largeur, longueur, hauteur):
        super().__init__(largeur, longueur);
        self.hauteur = hauteur

    @imprimer_resultat("Volume")
    def volume(self):
        return self.hauteur * self.largeur * self.longueur
    
    @imprimer_resultat("Perimetre")
    def perimetre(self):
        return 2 * 2 * (self.largeur + self.longueur) + 4 * self.hauteur
    
    @imprimer_resultat("Surface")
    def surface(self):
        return 2 * self.largeur * self.longueur + 2 * self.largeur * self.hauteur + 2 * self.longueur * self.hauteur

print("Rectangle:")
rect = Rectangle(3,5)
rect.perimetre()
rect.surface()

print("Parallélépipède:")
parallelepipede = Parallelepipede(1,2,3)
parallelepipede.perimetre()
parallelepipede.surface()
parallelepipede.volume()