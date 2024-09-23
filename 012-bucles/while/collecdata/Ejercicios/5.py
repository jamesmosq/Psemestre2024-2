#Llenar una lista con los primeros n números de la secuencia de Fibonacci:

fibonacci = [0, 1]
n = 10

while len(fibonacci) < n:
    siguiente = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente)

print(f"Los primeros {n} números de Fibonacci:", fibonacci)