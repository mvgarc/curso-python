# 1. ESTADO INICIAL: UNA LISTA (Mutable, acepta duplicados, mantiene el orden)
print("--- 1. LISTA INICIAL ---")
datos_iniciales = ["manzana", "pera", "naranja", "manzana", "uva"]
print(f"Tipo: {type(datos_iniciales)}")
print(f"Contenido: {datos_iniciales}")
print(f"¿Acepta duplicados? Sí.")
print("-" * 30)

# 2. CONVERSIÓN A SET (El filtro de unicidad)
print("--- 2. CONVERSIÓN: Lista a SET ---")
# Usamos set() para convertir la lista
datos_set = set(datos_iniciales) 
print(f"Tipo: {type(datos_set)}")
print(f"Contenido: {datos_set}")
print("¡Observación! El 'manzana' duplicado ha sido eliminado y el orden original se perdió.")
print("-" * 30)

# 3. CONVERSIÓN A TUPLA (La inmutabilidad)
print("--- 3. CONVERSIÓN: Set a TUPLA ---")
# Usamos tuple() para convertir el set
datos_tupla = tuple(datos_set)
print(f"Tipo: {type(datos_tupla)}")
print(f"Contenido: {datos_tupla}")
print("¡Observación! Ahora es una colección inmutable y el orden se ha fijado.")
print("-" * 30)

# 4. CONVERSIÓN FINAL A LISTA (Volver a la mutabilidad)
print("--- 4. CONVERSIÓN: Tupla a LISTA ---")
# Usamos list() para convertir la tupla
datos_finales_lista = list(datos_tupla)
print(f"Tipo: {type(datos_finales_lista)}")
print(f"Contenido: {datos_finales_lista}")
print("¡Observación! Es una Lista de nuevo, ahora mutable, pero sigue sin tener el 'manzana' duplicado.")
print("-" * 30)