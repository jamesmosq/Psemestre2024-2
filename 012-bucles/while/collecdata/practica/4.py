#Remover elementos de un set mientras no esté vacío
numeros = {1, 2, 3, 4, 5}
while numeros:
    elemento = numeros.pop()
    print(f"Removido: {elemento}")

print("Set vacío:", numeros)