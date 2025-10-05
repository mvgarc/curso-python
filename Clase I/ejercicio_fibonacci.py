def fibonacci(n):
    if n <= 0:
        print ("El número de términos debe ser un entero positivo")
        return

    a = 0
    b = 1

    contador = 0

    salida = ""

    while contador < n:
        salida = salida + str(a) + " "
        siguiente_termino = a + b
        a = b
        b = siguiente_termino

        contador += 1

    print (salida.strip())
print ("Serie de Fibonacci (25 terminos):")
fibonacci(25)

print ("Serie de Fibonacci (05 terminos):")
fibonacci(5)
