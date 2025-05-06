import numpy as np
import math

# Definir la función f(x)
def f(x):
    return 1 / (1 + x**2)

# Valor a aproximar
x_eval = 1 + math.sqrt(10)

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

# Función para construir la sucesión de valores interpolantes y_n
def build_sequence(n_max):
    y_sequence = []
    for n in range(1, n_max + 1):
        h = 10 / n
        x_points = [-5 + j * h for j in range(n + 1)]
        y_points = [f(x) for x in x_points]
        y_n = lagrange_interpolation(x_eval, x_points, y_points)
        y_sequence.append(y_n)
    return y_sequence

# Construir la sucesión para n = 1, 2, ..., 10
n_max = 10
y_sequence = build_sequence(n_max)

# Valor real de f(1 + sqrt(10))
real_value = f(x_eval)

# Imprimir resultados
print(f"Valor real de f(1 + sqrt(10)): {real_value}")
for n, y_n in enumerate(y_sequence, start=1):
    print(f"n = {n}, y_n = {y_n}, Error = {abs(y_n - real_value)}")