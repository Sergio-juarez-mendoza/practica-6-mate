import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Datos dados
days = np.array([0, 6, 10, 13, 17, 20, 28])
weight_sample1 = np.array([6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74])
weight_sample2 = np.array([6.67, 16.11, 18.89, 15.00, 10.56, 9.44, 8.89])

# Función para calcular el polinomio interpolante de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Función para encontrar el máximo del polinomio interpolante
def find_max_polynomial(x_points, y_points):
    def neg_polynomial(x):
        return -lagrange_interpolation(x, x_points, y_points)
    res = minimize_scalar(neg_polynomial, bounds=(min(x_points), max(x_points)), method='bounded')
    return res.x, -res.fun

# Aproximar la curva del peso promedio de las muestras
x_vals = np.linspace(min(days), max(days), 500)
y_vals_sample1 = [lagrange_interpolation(x, days, weight_sample1) for x in x_vals]
y_vals_sample2 = [lagrange_interpolation(x, days, weight_sample2) for x in x_vals]

# Encontrar el peso promedio máximo aproximado de cada muestra
max_day_sample1, max_weight_sample1 = find_max_polynomial(days, weight_sample1)
max_day_sample2, max_weight_sample2 = find_max_polynomial(days, weight_sample2)

# Imprimir resultados
print(f"Muestra 1: Peso máximo aproximado de {max_weight_sample1:.2f} mg en el día {max_day_sample1:.2f}")
print(f"Muestra 2: Peso máximo aproximado de {max_weight_sample2:.2f} mg en el día {max_day_sample2:.2f}")

# Graficar las curvas de interpolación
plt.plot(days, weight_sample1, 'o', label='Muestra 1 (Datos)')
plt.plot(x_vals, y_vals_sample1, label='Muestra 1 (Interpolación)')
plt.plot(days, weight_sample2, 's', label='Muestra 2 (Datos)')
plt.plot(x_vals, y_vals_sample2, label='Muestra 2 (Interpolación)')
plt.xlabel('Días')
plt.ylabel('Peso promedio (mg)')
plt.title('Interpolación de Lagrange del Peso Promedio de las Muestras')
plt.legend()
plt.grid()
plt.show()