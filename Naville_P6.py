import numpy as np


# Definir la función
def f(x):
    return np.sqrt(x)


# Puntos dados
x_points = np.array([0, 1, 2, 4, 5])
y_points = f(x_points)

# Valor a aproximar
x_eval = 3


# Método de Neville
def neville(x, y, x_eval):
    n = len(x)
    Q = np.zeros((n, n))

    # Inicializar la primera columna con los valores de y
    Q[:, 0] = y

    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = ((x_eval - x[i - j]) * Q[i, j - 1] - (x_eval - x[i]) * Q[i - 1, j - 1]) / (x[i] - x[i - j])

    return Q[n - 1, n - 1]


# Aplicar el método de Neville
approx = neville(x_points, y_points, x_eval)

# Valor real
real_value = f(x_eval)

# Error
error = abs(real_value - approx)

# Imprimir resultados
print(f"Aproximación de sqrt(3) usando Neville: {approx}")
print(f"Valor real de sqrt(3): {real_value}")
print(f"Error: {error}")