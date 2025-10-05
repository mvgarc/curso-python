import os

def manejar_archivos():
    # --- 1. ESCRITURA INICIAL (MODO 'w' - WRITE) ---
    # Crea o sobrescribe el archivo 'estudiantes.txt' en la carpeta actual.
    print("-> Escribiendo en 'estudiantes.txt' (Modo 'w').")
    with open("estudiantes.txt", "w") as archivo:
        archivo.write("Ana García\n")
        archivo.write("Carlos López\n")
        archivo.write("Beatriz Ruiz\n")

    # --- 2. LECTURA (MODO 'r' - READ) ---
    # Lee y muestra el contenido del archivo recién creado.
    print("\n-> Lectura de 'estudiantes.txt':")
    with open("estudiantes.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido.strip()) # strip() para limpiar espacios/saltos de línea extra al final

    # --- 3. ADICIÓN (MODO 'a' - APPEND) EN RUTA ESPECÍFICA ---
    
    # Definir la ruta relativa
    ruta_archivo = "./Clase_2/txt_csv/datos.txt"
    
    # Asegurarse de que la carpeta exista antes de intentar escribir en el archivo
    directorio = os.path.dirname(ruta_archivo)
    if directorio:
        os.makedirs(directorio, exist_ok=True)
        
    print(f"\n-> Añadiendo (Append) contenido a '{ruta_archivo}' (Modo 'a').")
    
    # El modo 'a' (append) añade al final. Si el archivo no existe, lo crea.
    # Si la carpeta no existe (como en este caso './Clase_2/txt_csv/'), 
    # Python generará un FileNotFoundError si no se usa os.makedirs.
    try:
        with open(ruta_archivo, "a") as archivo:
            archivo.write("Esta línea se añade al final de la anterior.\n")
            archivo.write("Una segunda línea de prueba.\n")
        print(f"Contenido añadido correctamente a '{ruta_archivo}'.")
        
        # Opcional: Leer el archivo 'datos.txt' para verificar la adición
        print(f"\n-> Lectura de '{ruta_archivo}' después de añadir:")
        with open(ruta_archivo, "r") as archivo_adicionado:
            contenido_adicionado = archivo_adicionado.read()
            print(contenido_adicionado.strip())
            
    except Exception as e:
        print(f"\nERROR: No se pudo acceder o escribir en la ruta especificada '{ruta_archivo}'.")
        print(f"Asegúrate de que los permisos de escritura sean correctos. Error: {e}")

# Ejecutar la función de manejo de archivos
manejar_archivos()