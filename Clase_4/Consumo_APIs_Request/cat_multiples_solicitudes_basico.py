import requests
from concurrent.futures import ThreadPoolExecutor

codigos = [200, 101, 205, 407, 500, 505]

def descargar_gato(codigo):
    url = f"https://http.cat/{codigo}"
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
        nombre_archivo = f"gatito_{codigo}.jpg"
        with open(nombre_archivo, "wb") as f:
            f.write(response.content)
        print(f"Imagen {codigo} descargada")
    else:
        print(f"Falló la descarga de {codigo}")

# Ejecutamos varias descargas en paralelo con 5 hilos
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(descargar_gato, codigos)