import numpy as np

# Valores dados (asumimos que estos son los valores correctos de f(x))
f_values = {
    -2: 4,  # f(-2) = 4 (valor asumido)
    -1: 1,  # f(-1) = 1 (valor asumido)
    1: 1,  # f(1) = 1 (valor asumido)
    2: 4  # f(2) = 4 (valor asumido)
}

# Valores con errores
f_values_error = {
    -2: 4,  # f(-2) no tiene error
    -1: 1 + 2,  # f(-1) sobreexpresado por 2
    1: 1 - 3,  # f(1) subexpresado por 3
    2: 4  # f(2) no tiene error
}

# Puntos de interpolación
x_points = np.array([-2, -1, 1, 2])

# Valores correctos de y
y_points = np.array([f_values[x] for x in x_points])

# Valores con errores de y
y_points_error = np.array([f_values_error[x] for x in x_points])


# Función para el algoritmo de Neville
def neville(x, x_points, y_points):
    n = len(x_points)
    Q = np.zeros((n, n))

    # Inicializar la primera columna con los valores de y
    Q[:, 0] = y_points

    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = ((x - x_points[i - j]) * Q[i, j - 1] - (x - x_points[i]) * Q[i - 1, j - 1]) / (
                        x_points[i] - x_points[i - j])

    return Q[n - 1, n - 1]

# Aproximación original de f(0)
approx_original = neville(0, x_points, y_points)

# Aproximación con errores en f(-1) y f(1)
approx_error = neville(0, x_points, y_points_error)

# Error en la aproximación original
error = abs(approx_original - approx_error)

# Imprimir resultados
print(f"Aproximación original de f(0): {approx_original}")
print(f"Aproximación con errores en f(-1) y f(1): {approx_error}")
print(f"Error en la aproximación original: {error}")