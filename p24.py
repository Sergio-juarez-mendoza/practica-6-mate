import numpy as np

# Datos dados
years = np.array([1940, 1950, 1960, 1970, 1980, 1990])
population = np.array([132165, 151326, 179323, 203302, 226542, 249633])  # En miles de habitantes

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

# Años a aproximar
years_to_approximate = [1930, 1965, 2010]

# Aproximaciones
approximations = {}
for year in years_to_approximate:
    pop_thousands = lagrange_interpolation(year, years, population)
    pop_millions = pop_thousands / 1000  # Convertir a millones
    approximations[year] = pop_millions

# Imprimir resultados
for year, pop in approximations.items():
    print(f"Aproximación de la población en {year}: {pop:.3f} millones")