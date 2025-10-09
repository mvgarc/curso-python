import pandas as pd
 # Crear un DataFrame
datos = {
    'Nombre': ['Ana', 'Luis', 'Pedro'],
    'Edad': [21, 23, 20],
    'Carrera': ['Ingeniería', 'Diseño', 'Medicina']
 }
df = pd.DataFrame(datos)
print(df)