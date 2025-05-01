import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creación de arreglos con numpy
ventas_semana = np.array([150, 200, 170, 220, 300, 250, 190])
print("Ventas por semana:", ventas_semana)

# Operaciones con arreglos
print("Promedio de ventas:", np.mean(ventas_semana))
print("Ventas máxima:", np.max(ventas_semana))
print("Ventas mínima:", np.min(ventas_semana))

# Lectura de archivo CSV con pandas
datos_ventas = pd.read_csv(r"C:\Tec\Octavo\PLyF\Tema 4\ventas.csv", encoding='utf-8')
print("\nDatos de ventas:\n", datos_ventas)

# 3. Agregar columna de ventas totales
datos_ventas['Ventas Totales'] = datos_ventas['Unidades Vendidas'] * datos_ventas['Precio Unitario']
print("\nDatos con ventas totales:\n", datos_ventas)

# 1. Gráfica de barras con nuevos colores
colores = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']  # puedes agregar más si hay más productos
plt.figure(figsize=(8,5))
plt.bar(datos_ventas['Producto'], datos_ventas['Unidades Vendidas'], color=colores)
plt.title('Unidades Vendidas por Producto')
plt.xlabel('Producto')
plt.ylabel('Unidades Vendidas')
plt.grid(axis='y')
plt.show()

# 2. Gráfico de pastel de proporción de unidades vendidas
plt.figure(figsize=(7,7))
plt.pie(datos_ventas['Unidades Vendidas'], labels=datos_ventas['Producto'], autopct='%1.1f%%', colors=colores, startangle=140)
plt.title('Proporción de Unidades Vendidas')
plt.axis('equal')  # Hace el gráfico circular
plt.show()
