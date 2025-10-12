import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [120, 580, 320, 120, 795, 147]

plt.plot(ventas, meses)
plt.title("Ventas del primer semestre")
plt.ylabel("Meses")
plt.xlabel("Cantidad de Ventas")

plt.show()

plt.savefig("grafico_ventas2.png")

print("Gráfico guardado como 'grafico_ventas.png'")