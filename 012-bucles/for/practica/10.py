#Desempaquetar múltiples listas simultáneamente
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
for a, b, c in zip(lista1, lista2, lista3):
    print(f"Suma: {a + b + c}")