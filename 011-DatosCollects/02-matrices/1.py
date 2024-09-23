# Crear una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimir la matriz
print("Matriz original:")
for fila in matriz:
    print(fila)

# Acceder a elementos
print("\nElemento en la fila 1, columna 2:", matriz[1][2])

# Modificar un elemento
matriz[0][0] = 10
print("\nMatriz después de modificar un elemento:")
for fila in matriz:
    print(fila)

# Suma de dos matrices
matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

suma_matriz = []
for i in range(len(matriz)):
    fila_suma = []
    for j in range(len(matriz[0])):
        fila_suma.append(matriz[i][j] + matriz2[i][j])
    suma_matriz.append(fila_suma)

print("\nSuma de matrices:")
for fila in suma_matriz:
    print(fila)

# Transponer una matriz
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)

# Multiplicación de matrices
def multiplicar_matrices(a, b):
    if len(a[0]) != len(b):
        return None
    resultado = [[sum(a[i][k] * b[k][j] for k in range(len(b)))
                  for j in range(len(b[0]))] for i in range(len(a))]
    return resultado

matriz_producto = multiplicar_matrices(matriz, matriz2)
print("\nProducto de matrices:")
for fila in matriz_producto:
    print(fila)