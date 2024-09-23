#Ejercicio 6: Usar pass en una condición
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        pass  # No hacer nada cuando el contador es 3
    print("El contador es:", contador)
