def calcular_promedio(notas):
    try:
        # Intentamos calcular el promedio
        total = sum(notas)
        cantidad = len(notas)
        promedio = total / cantidad
        return promedio

    except ZeroDivisionError:
        print("Error: No se pueden calcular promedios sin notas")
        return 0

    except TypeError:
        print("Error: Las notas deben ser números")
        return None

    finally:
        print("Cálculo de promedio finalizado")
# Ejemplos de uso
print(f"Promedio 1: {calcular_promedio([8.5, 9.2, 7.8])}") # Funciona
print(f"Promedio 2: {calcular_promedio([])}") # Lista vacía
print(f"Promedio 3: {calcular_promedio(['a', 'b'])}") # Datos incorrectos
