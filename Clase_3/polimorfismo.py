class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra: ¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maúlla: ¡Miau!")

# Polimorfismo en acción
animales = [Perro(), Gato(), Animal()]

for animal in animales:
    animal.hacer_sonido()

#polimorfismo con constructor

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} ladra: ¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} maúlla: ¡Miau!")

animales = [Perro("Bobby"), Gato("Misu")]

for animal in animales:
    animal.hacer_sonido()
