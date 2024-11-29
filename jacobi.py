import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    print(f"{'Iteración':>10} {'x':>10} {'y':>10} {'z':>10}")
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        print(f"{k+1:>10} {x_new[0]:>10.6f} {x_new[1]:>10.6f} {x_new[2]:>10.6f}")
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    return x

# Capturar el sistema de ecuaciones del usuario
n = 3  # Número de ecuaciones es fijo a 3 para x, y, z

A = np.zeros((n, n))
b = np.zeros(n)

print("Ingrese los coeficientes de las ecuaciones:")
variables = ['x', 'y', 'z']
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"Ingrese el coeficiente de {variables[j]} en la ecuación {i+1}: "))
    b[i] = float(input(f"Ingrese el término independiente de la ecuación {i+1}: "))

# Mostrar las ecuaciones despejadas
print("\nEcuaciones despejadas:")
for i in range(n):
    equation = f"{variables[i]} = (1/{A[i][i]}) * ({b[i]}"
    for j in range(n):
        if j != i:
            sign = "+" if A[i][j] < 0 else "-"
            equation += f" {sign} {abs(A[i][j])}*{variables[j]}"
    equation += " )"
    print(equation)

x0 = np.zeros_like(b)

# Parámetros del método de Jacobi
tol = 1e-10
max_iter = 100

# Resolver el sistema
sol = jacobi(A, b, x0, tol, max_iter)
print("Solución con ecuaciones ingresadas por el usuario:", sol)