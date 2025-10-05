"""import random

n = int(input("Ingrese un numero para generar los random"))

a = random.randint(1, n)
"""

import random

def generar_y_organizar_randoms():
    """
    Pide un número al usuario (N), genera N números aleatorios, 
    los añade a una lista y luego la organiza.
    """
    
    # 1. Solicitar el número de repeticiones (N)
    while True:
        try:
            # Pedimos al usuario el límite superior y también lo usaremos como cantidad
            entrada = input("Ingrese un número entero positivo para (1) generar el rango de aleatorios y (2) definir la cantidad de elementos: ")
            
            # Convertir y validar la entrada
            limite_y_cantidad = int(entrada)
            
            if limite_y_cantidad <= 0:
                print("El número debe ser mayor que cero.")
                continue
            
            break
        except ValueError:
            print("Entrada inválida. Ingrese solo números enteros.")

    # 2. Inicializar la lista y el contador para el bucle
    lista_aleatoria = []
    contador = 0
    
    # 3. Bucle WHILE para generar y añadir elementos
    print(f"\nGenerando {limite_y_cantidad} números aleatorios...")
    
    # El bucle se ejecutará mientras el contador sea menor que el número ingresado (N)
    while contador < limite_y_cantidad:
        
        # Generamos un número aleatorio entre 1 y el número ingresado (N)
        valor_aleatorio = random.randint(1, limite_y_cantidad)
        
        # Añadir a la lista con .append()
        lista_aleatoria.append(valor_aleatorio)
        
        # Incrementar el contador para evitar un bucle infinito
        contador += 1
        
    # 4. Organizar la lista
    # Usamos sorted() para crear una nueva lista ordenada y no modificar la original (opcional)
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
generar_y_organizar_randoms()