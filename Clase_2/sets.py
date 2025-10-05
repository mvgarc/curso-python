# Lenguajes que conocen los estudiantes
ana_lenguajes = {"Python", "Java", "JavaScript","Python"}
carlos_lenguajes = {"JavaScript", "C++", "Python","Go"}
print(f"Ana conoce: {ana_lenguajes}")
# Lenguajes en común
comunes = ana_lenguajes & carlos_lenguajes
print(f"Lenguajes en común: {comunes}")
# Todos los lenguajes únicos
todos = ana_lenguajes | carlos_lenguajes
print(f"Todos los lenguajes: {todos}")
# Eliminar duplicados de una lista
numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = list(set(numeros))
print(f"Sin duplicados: {unicos}")
print (type(unicos))