from abc import ABC, abstractmethod

class AbstractBase(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractBase):
    def abstract_method(self):
        print("Implemented abstract_method in ConcreteClass")

class AnotherConcreteClass(AbstractBase):
    def abstract_method(self):
        print("Implemented abstract_method in AnotherConcreteClass")

# Trying to create an instance of AbstractBase will raise an error
# abstract_method is not implemented in the abstract base class
# obj = AbstractBase()  # Uncommenting this line will raise an error

# Creating instances of concrete subclasses
concrete_obj = ConcreteClass()
concrete_obj.abstract_method()  # Output: Implemented abstract_method in ConcreteClass

another_concrete_obj = AnotherConcreteClass()
another_concrete_obj.abstract_method()  # Output: Implemented abstract_method in AnotherConcreteClass
