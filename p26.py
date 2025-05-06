import numpy as np
import math
from scipy.special import erf

# Función para calcular la serie de Maclaurin de erf(x) con una exactitud de 10^-4
def erf_maclaurin(x, tol=1e-4):
    """
    Aproxima erf(x) usando la serie de Maclaurin con una tolerancia dada.
    """
    result = 0.0
    n = 0
    while True:
        term = ((-1)**n * x**(2*n + 1)) / (math.factorial(n) * (2*n + 1))
        result += term
        if abs(term) < tol:
            break
        n += 1
    return (2 / math.sqrt(math.pi)) * result

# a. Construir una tabla de erf(x_i) con x_i = 0.2i para i = 0, 1, ..., 5
x_values = [round(0.2 * i, 1) for i in range(6)]  # Redondear a 1 decimal
erf_table = {x: erf_maclaurin(x) for x in x_values}

# Imprimir la tabla de erf(x_i)
print("Tabla de erf(x_i) con exactitud de 10^-4:")
for x, erf_x in erf_table.items():
    print(f"erf({x:.1f}) = {erf_x:.6f}")

# b. Interpolación lineal y cuadrática para aproximar erf(1/3)
x_interp = 1 / 3

# Interpolación lineal usando x = 0.2 y x = 0.4
x0, x1 = 0.2, 0.4
y0, y1 = erf_table[x0], erf_table[x1]
linear_interp = y0 + (y1 - y0) * (x_interp - x0) / (x1 - x0)

# Interpolación cuadrática usando x = 0.2, x = 0.4 y x = 0.6
x2 = 0.6
y2 = erf_table[x2]  # Ahora x2 = 0.6 está en el diccionario
quad_interp = y0 * ((x_interp - x1) * (x_interp - x2)) / ((x0 - x1) * (x0 - x2)) + \
              y1 * ((x_interp - x0) * (x_interp - x2)) / ((x1 - x0) * (x1 - x2)) + \
              y2 * ((x_interp - x0) * (x_interp - x1)) / ((x2 - x0) * (x2 - x1))

# Valor real de erf(1/3) usando la función erf de scipy
erf_real = erf(x_interp)

# Imprimir resultados
print(f"\nAproximación de erf(1/3):")
print(f"Interpolación lineal: {linear_interp:.6f}")
print(f"Interpolación cuadrática: {quad_interp:.6f}")
print(f"Valor real de erf(1/3): {erf_real:.6f}")

# Determinar qué método es más adecuado
error_linear = abs(linear_interp - erf_real)
error_quad = abs(quad_interp - erf_real)

print(f"\nError de la interpolación lineal: {error_linear:.6f}")
print(f"Error de la interpolación cuadrática: {error_quad:.6f}")

if error_linear < error_quad:
    print("La interpolación lineal es más adecuada.")
else:
    print("La interpolación cuadrática es más adecuada.")