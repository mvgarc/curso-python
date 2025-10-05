import random

def generar_y_organizar_randoms_simple():
    """
    Pide un número al usuario (N), genera N números aleatorios (entre 1 y N), 
    los añade a una lista usando un bucle while y luego la organiza.
    """
    
    # 1. Solicitar el número de repeticiones (N)
    # NOTA: ASUME QUE EL USUARIO INGRESA UN ENTERO.
    entrada = input("Ingrese un número entero positivo para (1) generar el rango de aleatorios y (2) definir la cantidad de elementos: ")
    
    limite_y_cantidad = int(entrada)

    # 2. Inicializar la lista y el contador para el bucle
    lista_aleatoria = []
    contador = 0
    
    # 3. Bucle WHILE para generar y añadir elementos
    print(f"\nGenerando {limite_y_cantidad} números aleatorios...")
    
    # El bucle se ejecutará mientras el contador sea menor que N
    while contador < limite_y_cantidad:
        
        # Generamos un número aleatorio entre 1 y N
        valor_aleatorio = random.randint(1, limite_y_cantidad)
        
        # Añadir a la lista con .append()
        lista_aleatoria.append(valor_aleatorio)
        
        # Incrementar el contador para controlar la repetición
        contador += 1
        
    # 4. Organizar la lista
    # Creamos una nueva lista ordenada
    lista_organizada = sorted(lista_aleatoria)
    
    # 5. Mostrar resultados
    print("\n" + "="*40)
    print("RESULTADOS:")
    print(f"Número N ingresado: {limite_y_cantidad}")
    print(f"Lista original generada ({limite_y_cantidad} elementos):")
    print(lista_aleatoria)
    print("-" * 40)
    print("Lista organizada (Ascendente):")
    print(lista_organizada)
    print("="*40)

# Ejecutar la función
generar_y_organizar_randoms_simple()