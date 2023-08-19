from intro import Address, Person

class Contact(Person, Address):
    def __init__(self, name, email, street, city):
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)

    def show(self):
        Person.show(self)
        Address.show(self)

class Notebook:
    def __init__(self):
        self.dico = dict()

    def add(self, name, email, street, city):
        self.dico[name] = Contact(name, email, street, city)
    
    def show(self):
        for name, contact in self.dico.items():
            print(f"=== {name} ===")
            contact.show()
            print()


notes = Notebook()
notes.add("Alice", "alice@example.com", "Lv 24", "Sthlm")
notes.add("Bob", "bob@example.com", "Rtb 35", "Sthlm")
notes.show()