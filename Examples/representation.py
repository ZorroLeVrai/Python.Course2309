class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __repr__(self):
        return f"La personne s'appelle {self.prenom} {self.nom}"
    
personne = Personne("Doe", "John")
print(personne)