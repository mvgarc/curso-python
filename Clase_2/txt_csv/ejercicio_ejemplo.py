#Leer un archivo completo

with open("data.txt", "r" )as archivo:
    contenido = archivo.read()
    print (contenido)

#Leer línea por línea
with open("data.txt", "r" )as archivo:
    for linea in archivo:
        print (linea.strip())
