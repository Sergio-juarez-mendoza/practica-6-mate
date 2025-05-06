import numpy as np


def neville(x, y, target):
    n = len(x)
    Q = np.zeros((n, n))
    Q[:, 0] = y

    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = ((target - x[i - j]) * Q[i, j - 1] - (target - x[i]) * Q[i - 1, j - 1]) / (x[i] - x[i - j])

    return Q[n - 1, n - 1]


# Valores dados
x = [-2, -1, 0, 1, 2]
y = [3 ** xi for xi in x]
target = 3

# Aproximación
result = neville(x, y, target)
print(f"Aproximación de la raíz de 3: {result}")