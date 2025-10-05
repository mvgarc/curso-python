import math

def es_primo(n):
    if n <=1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True

def imprimir_primos_hasta(limite):
    print (f"\nNúmeros primos menores o iguales a {limite}:")
    primos_encontrados = ""

# Recorremos el rango de números
    for numero in range(2, limite + 1):
        # Usamos la función es_primo() para verificar
        if es_primo(numero):
            # Concatenamos la cadena en lugar de usar una lista
            primos_encontrados = primos_encontrados + str(numero) + " "
            
    print(primos_encontrados.strip())


# Demostración
print(f"¿Es 13 primo? {es_primo(13)}")

# Llamamos a la nueva función sin usar listas en el cuerpo
imprimir_primos_hasta(20)