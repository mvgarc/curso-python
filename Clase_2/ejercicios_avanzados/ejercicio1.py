import csv

archivo = "personas.csv"

mayores = 0
menores = 0

with open (archivo, newline= "", encoding="utf-8") as csvfile:
    lector = csv.DictReader(csvfile)
    for fila in lector:
        edad = int(fila["edad"])
        if edad >= 18:
            mayores+= 1
        else:
            menores+= 1

print(f"Cantidad de personas mayores de edad: {mayores}")
print(f"Cantidad de personas menores de edad: {menores}")
