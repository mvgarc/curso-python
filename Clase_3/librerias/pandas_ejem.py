import pandas as pd

df = pd.read_csv("ventas.csv")

print(df.head())

df["Total"] = df["Precio"] * df["Cantidad"]

ventas_por_vendedor = df.groupby("Vendedor")["Total"].sum()

print("\n Ventas totales por vendedor:")
print(ventas_por_vendedor)

promedio_precio = df.groupby("Producto")["Precio"].mean()

print("\n Promedio de precio por producto:")
print(promedio_precio)

productos_top = df.groupby("Producto")["Total"].sum().sort_values(ascending=False)

print("\n Productos más vendidos:")
print(productos_top)

# Exportar el resumen a un nuevo archivo CSV
productos_top.to_csv("resumen_productos.csv")