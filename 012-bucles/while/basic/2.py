#Ejercicio 2: Adivinar un número
nu_secr = 7
intento = 0

while intento != nu_secr:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    if intento != nu_secr:
        print("Incorrecto, intenta de nuevo.")
    else:
        print("¡Correcto!")
