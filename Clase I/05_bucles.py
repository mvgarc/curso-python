"""numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

for multiplicador in range(1, 11, 5):
    resultado = numero * multiplicador
    #print(f"{numero} x {multiplicador} = {resultado}")
    print (numero , "x", multiplicador, "=", resultado)"""

"""suma = 0
numero = 1
while suma <= 20:
    suma += numero
    numero += 1
    print (suma , numero)
print(f"La suma alcanzó {suma}")"""

"""# 1. Inicialización
numero = 1

# 2. Condición
# La condición es: ¿Es 1 menor que 10? Sí. Siempre lo será si 'numero' no cambia.
while numero < 10:
    
    # 3. Lo que se ejecuta (imprime el mismo valor una y otra vez)
    print("El número es:", numero)
    
    # 4. ¡EL ERROR! La variable 'numero' NO se actualiza.
    # El valor de 'numero' se queda permanentemente en 1.
    
    # Si olvidamos esta línea:
    numero = numero + 1 
    
    # El bucle nunca terminará.

# Este mensaje nunca se mostrará:
print("¡El bucle ha terminado!")"""

"""# Usamos range() para generar los números que queremos (del 5 al 1, sin incluir el 0)
# range(inicio, parada, paso)
# range(5, 0, -1) genera: 5, 4, 3, 2, 1
for contador in range(5, 0, -1):
    
    # El valor actual de la secuencia se asigna automáticamente a 'contador'
    print(contador)

print("¡Despegue! 🚀")

# 1. Inicializamos la variable de control (el "contador")"""
contador = 5

print("Iniciando cuenta regresiva:")

# 2. Definimos el bucle while
# El bucle se ejecutará MIENTRAS la condición sea Verdadera (True)
while contador > 0:
    
    # 3. Lo que queremos que haga el bucle:
    print(contador)
    
    # 4. ¡LA PARTE CRÍTICA!
    # Actualizamos la variable de control. Esto eventualmente hará que la condición sea Falsa.
    contador -=1 
    # (Se puede usar la forma abreviada: contador -= 1)

# 5. Código después del bucle
print("¡Despegue! 🚀")