# Escribir en un archivo
with open("estudiantes.txt", "w") as archivo:
 archivo.write("Ana García\n")
 archivo.write("Carlos López\n")
 archivo.write("Beatriz Ruiz\n")


# Leer desde un archivo
with open("estudiantes.txt", "r") as archivo:
 contenido = archivo.read()
 print(contenido)

with open("datos.txt", "a") as archivo:
    archivo.write("Esta línea se añade al final de la anterior.\n")