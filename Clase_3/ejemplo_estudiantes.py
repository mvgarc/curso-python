#Ejemplo Ivanna
"""class gato:
    #Constructor
    def __init__ (self, color, edad):
        self.color = color
        self.edad = edad
    def describir(self):
        return (f"Horus es de color {self.color} y tiene {self.edad} años")

#Crear el objeto
horus = gato("blanco y negro", 0.5)
#Llamar al método
print (horus.describir())"""

#Ejemplo Martin
"""#clase
class casa:
        def __init__(self, hora, dia):
           self.hora = hora
           self.dia = dia

        def actividad(self):
            if self.hora >= 6 and self.dia.lower()== "sabado":
                  return "durmiendo"
            else:
                  return "despierto"
                  
hora = int(input("Ingrese la hora: "))
dia = input("Ingrese el día: ")

martin = casa(hora, dia)
print(f"Martín está {martin.actividad()}")"""

#Ejemplo Manuel
class videoGame:
    def __init__(self, Nombre, Genero):
        self.Nombre = Nombre
        self.Genero = Genero

    def jugar(self):
        print(f"Estoy jugando {self.Nombre}")

juego1 = videoGame("Celeste", "plataformero")

print(f"mi primer juego es {juego1.Nombre} y es un {juego1.Genero}")
juego1.jugar()