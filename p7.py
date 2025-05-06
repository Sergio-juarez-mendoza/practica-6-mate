import numpy as np
from scipy.interpolate import lagrange

# Definir las funciones
def f_a(x):
    return x * np.log(x)

def f_b(x):
    return x ** 3 + 4.001 * x ** 2 + 4.002 * x + 1.101

def f_c(x):
    return x * np.cos(x) - 2 * x ** 2 + 3 * x - 1

def f_d(x):
    return np.sin(np.exp(x) - 2)

# Puntos dados
x_points = np.array([0.5, 1.0, 1.5])
x_eval = 0.75

# Función para calcular el polinomio de interpolación, el error y la cota de error
def interpolate_and_error(f, f_deriv2, f_deriv3, x_points, x_eval):
    # Calcular los valores de la función en los puntos dados
    y_points = f(x_points)

    # Polinomio de grado uno (lineal)
    coef_linear = np.polyfit(x_points[:2], y_points[:2], 1)
    p_linear = np.poly1d(coef_linear)
    approx_linear = p_linear(x_eval)
    error_linear = abs(f(x_eval) - approx_linear)

    # Cota de error para el polinomio lineal
    xi_linear = np.linspace(min(x_points[:2]), max(x_points[:2]), 100)
    max_deriv_linear = max(abs(f_deriv2(x)) for x in xi_linear)
    product_linear = abs((x_eval - x_points[0]) * (x_eval - x_points[1]))
    error_bound_linear = (max_deriv_linear / 2) * product_linear

    # Polinomio de grado dos (cuadrático)
    coef_quad = np.polyfit(x_points, y_points, 2)
    p_quad = np.poly1d(coef_quad)
    approx_quad = p_quad(x_eval)
    error_quad = abs(f(x_eval) - approx_quad)

    # Cota de error para el polinomio cuadrático
    xi_quad = np.linspace(min(x_points), max(x_points), 100)
    max_deriv_quad = max(abs(f_deriv3(x)) for x in xi_quad)
    product_quad = abs((x_eval - x_points[0]) * (x_eval - x_points[1]) * (x_eval - x_points[2]))
    error_bound_quad = (max_deriv_quad / 6) * product_quad

    return approx_linear, error_linear, error_bound_linear, approx_quad, error_quad, error_bound_quad

# Derivadas de las funciones
def f_a_deriv2(x):
    return 1 / x

def f_a_deriv3(x):
    return -1 / x ** 2

def f_b_deriv2(x):
    return 6 * x + 8.002

def f_b_deriv3(x):
    return 6

def f_c_deriv2(x):
    return -x * np.cos(x) - 2 * np.sin(x) - 4

def f_c_deriv3(x):
    return x * np.sin(x) - 3 * np.cos(x)

def f_d_deriv2(x):
    return np.exp(x) * np.cos(np.exp(x) - 2) - np.exp(2 * x) * np.sin(np.exp(x) - 2)

def f_d_deriv3(x):
    return np.exp(x) * np.cos(np.exp(x) - 2) - 3 * np.exp(2 * x) * np.sin(np.exp(x) - 2) - np.exp(3 * x) * np.cos(
        np.exp(x) - 2)

# Aplicar la función a cada caso
results_a = interpolate_and_error(f_a, f_a_deriv2, f_a_deriv3, x_points, x_eval)
results_b = interpolate_and_error(f_b, f_b_deriv2, f_b_deriv3, x_points, x_eval)
results_c = interpolate_and_error(f_c, f_c_deriv2, f_c_deriv3, x_points, x_eval)
results_d = interpolate_and_error(f_d, f_d_deriv2, f_d_deriv3, x_points, x_eval)

# Imprimir resultados
print("a. f(x) = x ln(x)")
print(f"Aproximación lineal: {results_a[0]}, Error lineal: {results_a[1]}, Cota de error lineal: {results_a[2]}")
print(
    f"Aproximación cuadrática: {results_a[3]}, Error cuadrático: {results_a[4]}, Cota de error cuadrático: {results_a[5]}\n")

print("b. f(x) = x^3 + 4.001x^2 + 4.002x + 1.101")
print(f"Aproximación lineal: {results_b[0]}, Error lineal: {results_b[1]}, Cota de error lineal: {results_b[2]}")
print(
    f"Aproximación cuadrática: {results_b[3]}, Error cuadrático: {results_b[4]}, Cota de error cuadrático: {results_b[5]}\n")

print("c. f(x) = x cos(x) - 2x^2 + 3x - 1")
print(f"Aproximación lineal: {results_c[0]}, Error lineal: {results_c[1]}, Cota de error lineal: {results_c[2]}")
print(
    f"Aproximación cuadrática: {results_c[3]}, Error cuadrático: {results_c[4]}, Cota de error cuadrático: {results_c[5]}\n")

print("d. f(x) = sen(e^x - 2)")
print(f"Aproximación lineal: {results_d[0]}, Error lineal: {results_d[1]}, Cota de error lineal: {results_d[2]}")
print(
    f"Aproximación cuadrática: {results_d[3]}, Error cuadrático: {results_d[4]}, Cota de error cuadrático: {results_d[5]}\n")