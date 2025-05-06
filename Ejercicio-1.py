import numpy as np
from scipy.interpolate import lagrange


# Definir las funciones
def f_a(x):
    return np.cos(x)


def f_b(x):
    return np.sqrt(1 + x)


def f_c(x):
    return np.log(x + 1)


def f_d(x):
    return np.tan(x)


# Puntos dados
x_points = np.array([0, 0.6, 0.9])
x_eval = 0.45


# Función para calcular el polinomio de interpolación y el error
def interpolate_and_error(f, x_points, x_eval):
    # Calcular los valores de la función en los puntos dados
    y_points = f(x_points)

    # Polinomio de grado uno (lineal)
    coef_linear = np.polyfit(x_points[:2], y_points[:2], 1)
    p_linear = np.poly1d(coef_linear)
    approx_linear = p_linear(x_eval)
    error_linear = abs(f(x_eval) - approx_linear)

    # Polinomio de grado dos (cuadrático)
    coef_quad = np.polyfit(x_points, y_points, 2)
    p_quad = np.poly1d(coef_quad)
    approx_quad = p_quad(x_eval)
    error_quad = abs(f(x_eval) - approx_quad)

    return approx_linear, error_linear, approx_quad, error_quad


# Aplicar la función a cada caso
results_a = interpolate_and_error(f_a, x_points, x_eval)
results_b = interpolate_and_error(f_b, x_points, x_eval)
results_c = interpolate_and_error(f_c, x_points, x_eval)
results_d = interpolate_and_error(f_d, x_points, x_eval)

# Imprimir resultados
print("a. f(x) = cos(x)")
print(f"Aproximación lineal: {results_a[0]}, Error lineal: {results_a[1]}")
print(f"Aproximación cuadrática: {results_a[2]}, Error cuadrático: {results_a[3]}\n")

print("b. f(x) = sqrt(1 + x)")
print(f"Aproximación lineal: {results_b[0]}, Error lineal: {results_b[1]}")
print(f"Aproximación cuadrática: {results_b[2]}, Error cuadrático: {results_b[3]}\n")

print("c. f(x) = ln(x + 1)")
print(f"Aproximación lineal: {results_c[0]}, Error lineal: {results_c[1]}")
print(f"Aproximación cuadrática: {results_c[2]}, Error cuadrático: {results_c[3]}\n")

print("d. f(x) = tan(x)")
print(f"Aproximación lineal: {results_d[0]}, Error lineal: {results_d[1]}")
print(f"Aproximación cuadrática: {results_d[2]}, Error cuadrático: {results_d[3]}\n")