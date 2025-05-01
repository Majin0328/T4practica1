import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parte 1: Productividad
productividad = np.array([75, 80, 90, 85, 70])
print("Productividad semanal:", productividad)
print("Promedio de productividad:", np.mean(productividad))
print("Valor máximo de productividad:", np.max(productividad))

# Parte 2: Leer archivo CSV
datos_empleados = pd.read_csv("empleados.csv")

print("\nEmpleados del departamento de Ventas:")
print(datos_empleados[datos_empleados['Departamento'] == 'Ventas']['Nombre'])

# Parte 3: Calcular salario total (Salario + Bono)
datos_empleados['Salario Total'] = datos_empleados['Salario'] + datos_empleados['Bono']

# Parte 4: Gráfica de barras del salario total
plt.figure(figsize=(12,6))
plt.bar(datos_empleados['Nombre'], datos_empleados['Salario Total'], color='seagreen')
plt.title('Salario Total de Empleados (Salario + Bono)')
plt.xlabel('Empleado')
plt.ylabel('Salario Total ($)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
