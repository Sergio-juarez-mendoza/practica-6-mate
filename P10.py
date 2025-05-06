import numpy as np
import math  # Usamos el módulo math de Python

# Puntos dados
x_points = np.array([0.698, 0.733, 0.768, 0.803])
y_points = np.array([0.7661, 0.7432, 0.7193, 0.6946])

# Valor a aproximar
x_eval = 0.750

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

# Aproximación usando el polinomio interpolante de Lagrange
approx = lagrange_interpolation(x_eval, x_points, y_points)

# Valor real
real_value = 0.7317

# Error real
error_real = abs(real_value - approx)

# Cota de error
def error_bound(x, x_points, f_deriv4):
    n = len(x_points)
    product = 1.0
    for i in range(n):
        product *= abs(x - x_points[i])
    max_deriv4 = max(abs(f_deriv4(x)) for x in x_points)
    return (max_deriv4 / math.factorial(n)) * product  # Usamos math.factorial en lugar de np.math.factorial

# Derivada cuarta de cos(x) es cos(x)
def f_deriv4(x):
    return np.cos(x)

# Calcular la cota de error
error_bound_value = error_bound(x_eval, x_points, f_deriv4)

# Imprimir resultados
print(f"Aproximación de cos(0.750): {approx}")
print(f"Valor real de cos(0.750): {real_value}")
print(f"Error real: {error_real}")
print(f"Cota de error: {error_bound_value}")