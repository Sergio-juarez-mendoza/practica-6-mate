import numpy as np

# Definir la función
def f(x):
    return np.sqrt(x - x ** 2)

# Función para calcular el polinomio interpolante P_2(x)
def P_2(x, x1):
    x_points = np.array([0, x1, 1])
    y_points = f(x_points)
    coef = np.polyfit(x_points, y_points, 2)
    p = np.poly1d(coef)
    return p(x)

# Función para calcular la diferencia f(0.5) - P_2(0.5)
def difference(x1):
    return f(0.5) - P_2(0.5, x1)

# Método de bisección para encontrar x1
def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2

# Definir la función objetivo para la bisección
def objective(x1):
    return difference(x1) + 0.25

# Verificar el comportamiento de la función objetivo en el intervalo [0, 1]
x_values = np.linspace(0.1, 0.9, 100)
objective_values = [objective(x) for x in x_values]

# Encontrar un intervalo donde la función cambie de signo
a, b = None, None
for i in range(len(x_values) - 1):
    if np.sign(objective_values[i]) != np.sign(objective_values[i + 1]):
        a, b = x_values[i], x_values[i + 1]
        break

if a is None or b is None:
    raise ValueError("No se encontró un intervalo donde la función cambie de signo.")

# Encontrar el valor de x1 usando el método de bisección
x1 = bisection_method(objective, a, b)

# Imprimir el resultado
print(f"El valor más grande de x1 en (0, 1) para el cual f(0.5) - P_2(0.5) = -0.25 es: {x1}")