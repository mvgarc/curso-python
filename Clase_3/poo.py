class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    def cumplir_años(self):
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tengo {self.edad} años"
    # Crear objetos (instancias)
persona1 = Persona("María", 20)
persona2 = Persona("Carlos", 22)
print(persona1.saludar())
persona1.cumplir_años()