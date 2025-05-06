import numpy as np

# Función para calcular el polinomio interpolante de Lagrange
def lagrange_interpolation(y, y_points, x_points):
    """
    Interpola x en función de y usando el polinomio de Lagrange.

    Parámetros:
        y: Valor de y para el cual se desea aproximar x.
        y_points: Valores de y conocidos (nodos).
        x_points: Valores de x correspondientes a los y conocidos.

    Retorna:
        Aproximación de x correspondiente al valor de y.
    """
    n = len(y_points)
    result = 0.0
    for i in range(n):
        term = x_points[i]
        for j in range(n):
            if i != j:
                term *= (y - y_points[j]) / (y_points[i] - y_points[j])
        result += term
    return result

# Función para realizar la interpolación inversa
def inverse_interpolation(y_target, y_points, x_points):
    """
    Realiza la interpolación inversa para encontrar x dado un valor de y.

    Parámetros:
        y_target: Valor de y para el cual se desea aproximar x.
        y_points: Valores de y conocidos (nodos).
        x_points: Valores de x correspondientes a los y conocidos.

    Retorna:
        Aproximación de x correspondiente al valor de y_target.
    """
    return lagrange_interpolation(y_target, y_points, x_points)

# Ejemplo de uso
if __name__ == "__main__":
    # Datos conocidos: y = f(x)
    x_points = np.array([1.0, 2.0, 3.0, 4.0])  # Valores de x
    y_points = np.array([0.5, 1.0, 1.5, 2.0])  # Valores de y = f(x)

    # Valor de y para el cual queremos aproximar x
    y_target = 1.25

    # Aproximación de x usando interpolación inversa
    x_approx = inverse_interpolation(y_target, y_points, x_points)

    # Imprimir el resultado
    print(f"Para y = {y_target}, la aproximación de x es: {x_approx}")