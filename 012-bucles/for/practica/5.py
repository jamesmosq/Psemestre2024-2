#Encontrar índices de elementos específicos
numeros = [10, 20, 30, 40, 20, 50, 20]
indices_20 = [indice for indice, num in enumerate(numeros) if num == 20]
print(f"El número 20 aparece en los índices: {indices_20}")