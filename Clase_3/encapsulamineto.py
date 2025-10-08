# Ejemplo: Encapsulamiento y Reutilización

class Persona:
    def __init__(self, nombre, edad):
        # Encapsulamiento: los datos están dentro de la clase
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        # Método que usa los datos internos de la clase
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Reutilización: creamos varios objetos a partir de la misma clase
persona1 = Persona("Ana", 17)
persona2 = Persona("Luis", 25)
persona3 = Persona("María", 30)

# Usamos los métodos de la clase
persona1.saludar()
persona2.saludar()

# Reutilizamos la lógica en varios objetos
for persona in [persona1, persona2, persona3]:
    if persona.es_mayor_de_edad():
        print(f"{persona.nombre} es mayor de edad.")
    else:
        print(f"{persona.nombre} es menor de edad.")
