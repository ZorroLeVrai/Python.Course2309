from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    "Animal est une classe abstraite"

    @abstractmethod
    def crier(self):
        pass

class Chien(Animal):
    def crier(self):
        print("wouaf!")

a = Chien()
a.crier()