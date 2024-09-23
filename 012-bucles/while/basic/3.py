#Ejercicio 3: Usar continue para saltar números pares
contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Si es par, saltamos a la siguiente iteración
    print(contador)
