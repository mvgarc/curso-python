"""numero = 25
numero_2 = int(input("Ingrese un numero: "))
resta = numero - numero_2
print("El resultado de la resta es: ", resta)
print (numero - numero_2)
"""

"""n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
suma = n1 + n2
print("El resultado de la suma es: ", suma)
resta = n1 - n2
print("El resultado de la resta es: ", resta)
multiplicacion = n1 * n2
print("El resultado de la multiplicacion es: ", multiplicacion)
division = n1/n2
print (type(division))
print("El resultado de la division es: ", division)
division_entera = n1//n2
print (type(division_entera))
print("El resultado de la division entera es: ", division_entera)
exponente = n1**n2
print("El resultado del exponente es: ", exponente)
modulo = n1%n2
print("El resultado del modulo es: ", modulo)"""

"""#Operadores de comparación
n1 = 20
n2 = 20
igual = n1 == n2
print("El resultado de la igualdad es: ", igual)
diferente = n1!= n2
print("El resultado de la diferencia es: ", diferente)
mayor_que = n1 > n2
print("El resultado de mayor que es: ", mayor_que)
menor_que = n1 < n2
print("El resultado de menor que es: ", menor_que)
mayor_igual_que = n1 >= n2
print("El resultado de mayor o igual que es: ", mayor_igual_que)
menor_igual_que = n1 < n2
print("El resultado de menor o igual que es: ", menor_igual_que)"""

"""es_mayor_de_edad = True
tiene_licencia = False

# Operador 'and': Devuelve True si *ambas* condiciones son True
# Resultado esperado: False (True AND False es False)
puede_conducir_legalmente = es_mayor_de_edad and tiene_licencia
print("¿Puede conducir legalmente? (Mayor de edad Y con licencia):", puede_conducir_legalmente)

# Operador 'or': Devuelve True si *al menos una* de las condiciones es True
# Resultado esperado: True (True OR False es True)
puede_votar = es_mayor_de_edad or tiene_licencia
print("¿Puede votar? (Mayor de edad O con licencia):", puede_votar)

# Operador 'not': Invierte el valor booleano
# Resultado esperado: False (NOT True es False)
es_menor_de_edad = not es_mayor_de_edad
print("¿Es menor de edad? (NO mayor de edad):", es_menor_de_edad)"""

"""edad = int(input("Ingrese su edad: "))
if edad >= 18:
    b = edad
    a = 1
    b +=a
    print ("Eres mayor de edad")
    print (b)

elif edad == 15:
    print("Eres una quinceañera")

else:
    print("Eres menor de edad")

a = -1
if a>0:
    print (a)
elif a==0:
    print (-a)
else: 
    print (a)"""


# 1. Pedimos la entrada al usuario.
# La función input() siempre guarda la respuesta como texto (string).
genero = input("Por favor, introduce tu género (M/F): ")

# 2. Convertimos la respuesta a minúsculas para manejar 'm', 'M', 'f', 'F' sin problemas.
genero_normalizado = genero.lower()

# 3. Estructura Condicional: Comprobamos el valor.

if genero_normalizado == "f":
    # Este bloque se ejecuta si el usuario introdujo 'f' o 'F'.
    print("Has seleccionado el género femenino.")

elif genero_normalizado == "m":
    # Este bloque se ejecuta si el usuario introdujo 'm' o 'M'.
    print("Has seleccionado el género masculino.")

else:
    # Este bloque se ejecuta si la respuesta no fue ni 'f' ni 'm'.
    print("Respuesta no reconocida. Intenta solo con 'M' o 'F'.")