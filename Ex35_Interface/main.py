from abc import ABC, abstractmethod

# Classe Interface avec __subclasshook__
class Interface(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return all(
            hasattr(subclass, method)
            for method in cls.__abstractmethods__
        )
    
# Classe Container avec __contains__
class Container(ABC):
    @abstractmethod
    def __contains__(self, item):
        pass

# Classe Sized avec __len__
class Sized(ABC):
    @abstractmethod
    def __len__(self):
        pass

# Classe SizedContainer avec __len__ et __contains__
class SizedContainer(Container, Sized):
    pass

# Classe Iterable avec __iter__
class Iterable(ABC):
    @abstractmethod
    def __iter__(self):
        pass

# Exemples d'implémentation de classes

class MyContainer(SizedContainer):
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

container = MyContainer([1, 2, 3])
print(2 in container)  # Output: True
print(len(container))  # Output: 3

####################################################

class Printable(Interface):
    @abstractmethod
    def print(self):
        pass

class Document(Printable):
    def __init__(self, content):
        self.content = content

    def print(self):
        print(self.content)

document = Document("This is a document.")
print(isinstance(document, Printable))