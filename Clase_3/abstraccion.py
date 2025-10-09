from abc import ABC, abstractmethod

# Clase abstracta
class Animal(ABC):

    @abstractmethod
    def sonido(self):
        pass  # Método abstracto, sin implementación

# Clases que heredan e implementan el método
class Perro(Animal):
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def sonido(self):
        return "Miau!"

# No puedo hacer esto:
# animal = Animal() Error, porque es abstracta

# Pero sí puedo crear objetos de las clases hijas:
perro = Perro()
gato = Gato()

print(perro.sonido())  # Guau!
print(gato.sonido())   # Miau!
