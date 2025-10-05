import csv

def manejar_registro_csv():
    # Datos de los estudiantes
    estudiantes = [
        ["Nombre", "Edad", "Carrera", "Nota"],
        ["Ana García", 21, "Informática", 8.5],
        ["Carlos López", 22, "Matemáticas", 9.2],
        ["Beatriz Ruiz", 20, "Física", 8.8]
    ]

    # --- 1. ESCRITURA DE DATOS CSV (MODO 'w') ---
    # La opción newline="" es vital en Windows para evitar líneas en blanco extra.
    print("-> Escribiendo datos en 'registro.csv'...")
    with open("registro.csv", "w", newline="") as archivo:
        # Crea el objeto escritor para interactuar con el archivo
        escritor = csv.writer(archivo) 
        
        # Escribe todas las filas de la lista de una vez
        escritor.writerows(estudiantes)

    # --- 2. LECTURA DE DATOS CSV (MODO 'r') ---
    print("\n-> Lectura del contenido de 'registro.csv':")
    with open("registro.csv", "r") as archivo:
        # Crea el objeto lector
        lector = csv.reader(archivo)
        
        # Itera sobre cada fila leída del archivo
        for fila in lector:
            # Imprime la fila como una lista de strings
            print(fila)

# Ejecutar la función
manejar_registro_csv()