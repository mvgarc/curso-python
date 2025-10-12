import aiohttp
import asyncio

codigos = [206, 203, 204, 423, 444, 502]

async def descargar_gato(codigo):
    url = f"https://http.cat/{codigo}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200 and "image" in response.headers.get("Content-Type", ""):
                contenido = await response.read()
                with open(f"gatito_{codigo}.jpg", "wb") as f:
                    f.write(contenido)
                print(f"Imagen {codigo} descargada")
            else:
                print(f"Falló la descarga de {codigo}")

async def main():
    await asyncio.gather(*(descargar_gato(c) for c in codigos))

# Ejecutar
asyncio.run(main())