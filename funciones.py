def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def restar(a, b):
    """Devuelve la resta del primer número menos el segundo."""
    return a - b

def saludar(nombre):
    """Devuelve un saludo personalizado."""
    return f"¡Hola, {nombre}! Bienvenido a la calculadora."

def dividir(a, b):
    """Devuelve la división, manejando el error de división por cero."""
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b