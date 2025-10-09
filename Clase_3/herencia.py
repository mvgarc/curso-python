# Clase padre (superclase)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Clase hija (subclase) que hereda de Animal
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} está ladrando. ¡Guau!")

# Otra clase hija
class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} está maullando. ¡Miau!")


perro1 = Perro("Firulais")
gato1 = Gato("Michi")

perro1.comer()   # método heredado de Animal
perro1.ladrar()  # método propio de Perro

gato1.comer()    # método heredado de Animal
gato1.maullar()  # método propio de Gato
