"""def recolectar_y_organizar_datos():
    
    numeros_ingresados = []

    # 1. Bucle de Solicitud de Datos
    print("Por favor, ingresa números enteros. Escribe 'listo' para terminar.")
    
    while True:
        entrada = input("Ingresa un número: ")
        
        # Condición de parada
        if entrada.lower() == 'listo':
            break
        
        # 2. Manejo de errores y Almacenamiento
        try:
            # Intenta convertir la entrada a un entero
            numero = int(entrada)
            numeros_ingresados.append(numero)
        except ValueError:
            # Maneja el caso en que el usuario no ingresa un número válido
            print(f"'{entrada}' no es un número entero válido. Intenta de nuevo o escribe 'listo'.")
            
    # 3. Clasificación
    
    # Crea una copia para el ordenamiento ascendente
    ascendente = sorted(numeros_ingresados)
    
    # Crea una copia para el ordenamiento descendente (reverse=True)
    descendente = sorted(numeros_ingresados, reverse=True)
    
    # 4. Salida de Resultados
    print("\n" + "="*30)
    print("--- Resultados de la Clasificación ---")
    print(f"Lista Original: {numeros_ingresados}")
    print(f"Lista Ascendente: {ascendente}")
    print(f"Lista Descendente: {descendente}")
    print("="*30)

# Ejecutar el programa
recolectar_y_organizar_datos()"""


"""def recolectar_y_organizar_datos_simple():
    
    numeros_ingresados = []

    # 1. Bucle de Solicitud de Datos
    print("Por favor, ingresa números enteros. Escribe 'listo' para terminar.")
    
    while True:
        entrada = input("Ingresa un número: ")
        
        # Condición de parada
        if entrada.lower() == 'listo':
            break
        
        # 2. Conversión Directa y Almacenamiento
        # NOTA: Esta línea fallará con un ValueError si el usuario ingresa texto o un decimal.
        numero = int(entrada)
        numeros_ingresados.append(numero)
            
    # 3. Clasificación
    
    # Crea la lista ordenada de forma ascendente
    ascendente = sorted(numeros_ingresados)
    
    # Crea la lista ordenada de forma descendente
    descendente = sorted(numeros_ingresados, reverse=True)
    
    # 4. Salida de Resultados
    print("\n" + "="*30)
    print("--- Resultados de la Clasificación ---")
    print(f"Lista Original: {numeros_ingresados}")
    print(f"Lista Ascendente: {ascendente}")
    print(f"Lista Descendente: {descendente}")
    print("="*30)

# Ejecutar el programa
recolectar_y_organizar_datos_simple()"""

def es_numero_simple(entrada):
    """Verifica si una cadena es un entero positivo (limitación de la simplicidad)."""
    return entrada.isdigit()

def recolectar_y_clasificar_datos_sin_errores():
    """Recoge letras y números, los clasifica en dos listas y los ordena sin try/except."""
    
    numeros_ingresados = []
    letras_ingresadas = []

    print("Por favor, ingresa números enteros positivos o letras/palabras.")
    print("Escribe 'listo' para terminar el proceso de entrada.")
    
    while True:
        entrada = input("Ingresa un valor: ")
        
        # 1. Condición de Parada
        if entrada.lower() == 'listo':
            break
        
        # 2. Clasificación
        if es_numero_simple(entrada):
            # Si se ve como un número entero positivo (usando .isdigit())
            # Convertimos a entero antes de añadirlo
            numeros_ingresados.append(int(entrada))
        else:
            # Si no es reconocido como un número, se trata como texto
            letras_ingresadas.append(entrada)

    # 3. Organización (Clasificación)
    
    # a. Organización de Números (Numérica)
    numeros_ordenados = sorted(numeros_ingresados)
    
    # b. Organización de Letras (Alfabética)
    letras_ordenadas = sorted(letras_ingresadas)
    
    # 4. Salida de Resultados
    print("\n" + "="*45)
    print("--- Resultados de la Clasificación y Organización ---")
    print("="*45)
    
    # Resultados de Números
    print("LISTA DE NÚMEROS:")
    print(f"  Números Ingresados: {numeros_ingresados}")
    print(f"  Números Ordenados:  {numeros_ordenados}")
    
    print("-" * 45)

    # Resultados de Letras
    print("LISTA DE LETRAS/PALABRAS:")
    print(f"  Letras Ingresadas: {letras_ingresadas}")
    print(f"  Letras Ordenadas:  {letras_ordenadas}")
    
    print("="*45)

# Ejecutar el programa
recolectar_y_clasificar_datos_sin_errores()