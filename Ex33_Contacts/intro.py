class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city
    def show(self):
        print(self.street)
        print(self.city)

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def show(self):
        print(f"{self.name} - {self.email}" )
