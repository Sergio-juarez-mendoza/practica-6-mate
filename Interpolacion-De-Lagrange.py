import numpy as np
from scipy.interpolate import lagrange

# Datos del inciso a
x_a = np.array([8.1, 8.3, 8.6, 8.7])
y_a = np.array([16.94410, 17.56492, 18.50515, 18.82091])
x_eval_a = 8.4

# Construcción del polinomio interpolante de Lagrange de grado 1, 2 y 3
poly_a_1 = lagrange(x_a[:2], y_a[:2])  # Grado 1
poly_a_2 = lagrange(x_a[:3], y_a[:3])  # Grado 2
poly_a_3 = lagrange(x_a, y_a)          # Grado 3

# Evaluación en x = 8.4
f_a_1 = poly_a_1(x_eval_a)
f_a_2 = poly_a_2(x_eval_a)
f_a_3 = poly_a_3(x_eval_a)

# Imprimir los resultados
print(f"Interpolación en x = 8.4 usando polinomios de Lagrange:")
print(f"  - Grado 1: {f_a_1}")
print(f"  - Grado 2: {f_a_2}")
print(f"  - Grado 3: {f_a_3}")

# Datos del inciso b
x_b = np.array([-0.75, -0.5, -0.25, 0.0])
y_b = np.array([-0.07181250, -0.02475000, 0.334993750, 1.10100000])
x_eval_b = -1/3

# Construcción del polinomio interpolante de Lagrange de grado 1, 2 y 3
poly_b_1 = lagrange(x_b[:2], y_b[:2])  # Grado 1
poly_b_2 = lagrange(x_b[:3], y_b[:3])  # Grado 2
poly_b_3 = lagrange(x_b, y_b)          # Grado 3

# Evaluación en x = -1/3
f_b_1 = poly_b_1(x_eval_b)
f_b_2 = poly_b_2(x_eval_b)
f_b_3 = poly_b_3(x_eval_b)

# Imprimir los resultados
print(f"\nInterpolación en x = -1/3 usando polinomios de Lagrange:")
print(f"  - Grado 1: {f_b_1}")
print(f"  - Grado 2: {f_b_2}")
print(f"  - Grado 3: {f_b_3}")

# Datos del inciso c
x_c = np.array([0.1, 0.2, 0.3, 0.4])
y_c = np.array([0.62049958, -0.28398668, 0.00660095, 0.24842440])
x_eval_c = 0.25

# Construcción del polinomio interpolante de Lagrange de grado 1, 2 y 3
poly_c_1 = lagrange(x_c[:2], y_c[:2])  # Grado 1
poly_c_2 = lagrange(x_c[:3], y_c[:3])  # Grado 2
poly_c_3 = lagrange(x_c, y_c)          # Grado 3

# Evaluación en x = 0.25
f_c_1 = poly_c_1(x_eval_c)
f_c_2 = poly_c_2(x_eval_c)
f_c_3 = poly_c_3(x_eval_c)

# Imprimir los resultados
print(f"\nInterpolación en x = 0.25 usando polinomios de Lagrange:")
print(f"  - Grado 1: {f_c_1}")
print(f"  - Grado 2: {f_c_2}")
print(f"  - Grado 3: {f_c_3}")

# Datos del inciso d
x_d = np.array([0.6, 0.7, 0.8, 1.0])
y_d = np.array([-0.17694460, 0.01375227, 0.22363362, 0.65809197])
x_eval_d = 0.9

# Construcción del polinomio interpolante de Lagrange de grado 1, 2 y 3
poly_d_1 = lagrange(x_d[:2], y_d[:2])  # Grado 1
poly_d_2 = lagrange(x_d[:3], y_d[:3])  # Grado 2
poly_d_3 = lagrange(x_d, y_d)          # Grado 3

# Evaluación en x = 0.9
f_d_1 = poly_d_1(x_eval_d)
f_d_2 = poly_d_2(x_eval_d)
f_d_3 = poly_d_3(x_eval_d)

# Imprimir los resultados
print(f"\nInterpolación en x = 0.9 usando polinomios de Lagrange:")
print(f"  - Grado 1: {f_d_1}")
print(f"  - Grado 2: {f_d_2}")
print(f"  - Grado 3: {f_d_3}")