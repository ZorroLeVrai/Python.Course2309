class Personne:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.prenom = prenom

    def info(self):
        return f"{self.__nom} {self.prenom}" 

    def afficher(self):
        print(self.info())

class Employee(Personne):
    def __init__(self, nom, prenom, titre):
        super().__init__(nom, prenom)
        self.titre = titre

    def info(self):
        text = super().info()
        return f"{text} {self.titre}"


per = Personne("Joe", "Doe")
emp = Employee("Jane", "Doe", "Chef de projet")

per.afficher()
emp.afficher()

emp.__nom = "Arthur"
print(emp.__nom)