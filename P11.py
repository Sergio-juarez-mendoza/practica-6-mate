import numpy as np
import math

# Puntos dados
x_points = np.array([1.00, 1.05, 1.10, 1.15])
y_points = np.array([0.1924, 0.2414, 0.2933, 0.3492])

# Valor a aproximar
x_eval = 1.09

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

# Función original
def f(x):
    return math.log10(math.tan(x))

# Valor real
real_value = f(x_eval)

# Error real
error_real = abs(real_value - approx)

# Cota de error
def error_bound(x, x_points, f_deriv4):
    n = len(x_points)
    product = 1.0
    for i in range(n):
        product *= abs(x - x_points[i])
    max_deriv4 = max(abs(f_deriv4(x)) for x in x_points)
    return (max_deriv4 / math.factorial(n)) * product

# Derivada cuarta de f(x) = log10(tan(x))
def f_deriv4(x):
    tan_x = math.tan(x)
    sec_x = 1 / math.cos(x)
    return (8 * sec_x**4 * tan_x**3 - 16 * sec_x**4 * tan_x) / (math.log(10) * tan_x**4)

# Calcular la cota de error
error_bound_value = error_bound(x_eval, x_points, f_deriv4)

# Imprimir resultados
print(f"Aproximación de f(1.09): {approx}")
print(f"Valor real de f(1.09): {real_value}")
print(f"Error real: {error_real}")
print(f"Cota de error: {error_bound_value}")