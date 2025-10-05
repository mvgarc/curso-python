def es_palindromo (texto):

    texto_limpio = ""
    texto_procesar = texto.lower()

    for caracter in texto_procesar:
        if 'a' <= caracter <= 'z':
            texto_limpio = texto_limpio + caracter    
    print(f"DEBUG: Texto de entrada: '{texto}'")
    print(f"DEBUG: Texto Limpio: '{texto_limpio}'")
    print(f"DEBUG: Texto Invertido: '{texto_limpio[::-1]}'")

    return texto_limpio == texto_limpio[::-1]
    

print(f"¿'Ana' es palíndromo? {es_palindromo('Ana')}")
print("-" * 20)
print(f"¿'maria' es palíndromo? {es_palindromo('maria')}")
print("-" * 20)
print(f"¿'Amo la paloma' es palíndromo? {es_palindromo('Amo la paloma')}")