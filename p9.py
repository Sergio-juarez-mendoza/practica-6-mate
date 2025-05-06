import numpy as np

# Puntos dados
x_points = np.array([0, 0.5, 1, 2])
y_points = np.array([0, None, 3, 2])  # y es desconocido

# Función para encontrar y
def find_y():
    # El coeficiente de x^3 debe ser 6
    # Construimos el sistema de ecuaciones para encontrar y
    # El polinomio interpolante es P_3(x) = a x^3 + b x^2 + c x + d
    # Usamos los puntos dados para formar las ecuaciones:
    # P_3(0) = 0 => d = 0
    # P_3(0.5) = y => a (0.5)^3 + b (0.5)^2 + c (0.5) + d = y
    # P_3(1) = 3 => a (1)^3 + b (1)^2 + c (1) + d = 3
    # P_3(2) = 2 => a (2)^3 + b (2)^2 + c (2) + d = 2
    # Además, el coeficiente de x^3 es a = 6

    # Sabemos que a = 6
    a = 6

    # Sustituimos a en las ecuaciones
    # P_3(1) = 6(1)^3 + b(1)^2 + c(1) + d = 3 => 6 + b + c + d = 3
    # P_3(2) = 6(2)^3 + b(2)^2 + c(2) + d = 2 => 48 + 4b + 2c + d = 2
    # P_3(0) = d = 0

    # Sabemos que d = 0
    d = 0

    # Ahora tenemos dos ecuaciones:
    # 6 + b + c = 3  => b + c = -3
    # 48 + 4b + 2c = 2 => 4b + 2c = -46

    # Resolvemos el sistema de ecuaciones
    A = np.array([[1, 1], [4, 2]])
    B = np.array([-3, -46])
    b, c = np.linalg.solve(A, B)

    # Ahora usamos la ecuación para y:
    # P_3(0.5) = 6(0.5)^3 + b(0.5)^2 + c(0.5) + d = y
    y = 6 * (0.5)**3 + b * (0.5)**2 + c * 0.5 + d

    return y

# Encontrar y
y = find_y()

# Imprimir el resultado
print(f"El valor de y es: {y}")