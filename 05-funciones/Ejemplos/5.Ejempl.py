#Función con número variable de argumentos:

def suma_varios(*numeros):
    return sum(numeros)

print(suma_varios(1, 2, 3))  # Imprime: 6
print(suma_varios(1, 2, 3, 4, 5))  # Imprime: 15