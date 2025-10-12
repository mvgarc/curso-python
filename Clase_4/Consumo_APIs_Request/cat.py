import requests

url = "https://http.cat/400"

response = requests.get(url, allow_redirects=True)

# Información de diagnóstico
print("Código de respuesta:", response.status_code)
print("Tipo de contenido:", response.headers.get("Content-Type"))

# Verificamos si la respuesta es una imagen
if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
    with open("gatito_400.jpg", "wb") as file:
        file.write(response.content)
    print("Imagen descargada correctamente.")
else:
    print(" No se recibió una imagen válida.")