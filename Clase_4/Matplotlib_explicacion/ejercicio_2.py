import matplotlib.pyplot as plt
# Datos de ejemplo
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
ventas = [15000, 18000, 12000, 22000, 25000, 28000]
# Crear gráfico de líneas

#Tamaño del  gráfico (en pulgadas)
plt.figure(figsize=(10, 6))
plt.plot(meses, ventas, marker='o', linewidth=2, color="#E718D9")
plt.title('Evolución de Ventas 2024', fontsize=16)
plt.xlabel('Mes')
plt.ylabel('Ventas ($)')
#Lineas de fondo
plt.grid(True, alpha=0.3)
plt.show()

plt.savefig("grafico_ventass.png")

print("Gráfico guardado como 'grafico_ventass.png'")