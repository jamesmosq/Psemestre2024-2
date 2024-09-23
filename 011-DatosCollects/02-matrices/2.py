import numpy as np

# Crear matrices con NumPy
matriz_np = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matriz2_np = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matriz NumPy:")
print(matriz_np)

# Operaciones básicas
print("\nSuma de matrices:")
print(matriz_np + matriz2_np)

print("\nResta de matrices:")
print(matriz_np - matriz2_np)

print("\nMultiplicación elemento por elemento:")
print(matriz_np * matriz2_np)

print("\nMultiplicación de matrices:")
print(np.dot(matriz_np, matriz2_np))

# Operaciones avanzadas
print("\nDeterminante:")
print(np.linalg.det(matriz_np))

print("\nInversa de la matriz:")
print(np.linalg.inv(matriz_np))

print("\nAutovalores:")
autovalores, autovectores = np.linalg.eig(matriz_np)
print(autovalores)

print("\nAutovectores:")
print(autovectores)

# Operaciones estadísticas
print("\nMedia de cada columna:")
print(np.mean(matriz_np, axis=0))

print("\nDesviación estándar de cada fila:")
print(np.std(matriz_np, axis=1))

# Reshape y concatenación
print("\nReshape de matriz 3x3 a 1x9:")
print(matriz_np.reshape(1, 9))

print("\nConcatenación vertical:")
print(np.vstack((matriz_np, matriz2_np)))

print("\nConcatenación horizontal:")
print(np.hstack((matriz_np, matriz2_np)))