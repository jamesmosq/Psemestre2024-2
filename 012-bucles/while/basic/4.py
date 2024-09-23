#Ejercicio 4: Sumar hasta un límite con break
suma = 0

while True:
    numero = int(input("Introduce un número: "))
    suma += numero
    if suma >= 100:
        print("La suma ha alcanzado o superado 100.")
        break  # Rompemos el ciclo
    print("Suma actual:", suma)
