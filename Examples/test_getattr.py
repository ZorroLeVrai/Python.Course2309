class Toto:
    def __init__(self, name):
        self.name = name

    @property
    def nom(self):
        return self.name
    
    def __getattr__(self, param):
        print(f"Get param {param}")
        return 0
    
test = Toto("Rex")
print(test.nom)
print(getattr(test, "nom"))
test.toto


