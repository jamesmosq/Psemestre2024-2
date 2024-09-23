# 2.NameError: Juego de adivinanza con variable no definida
import  random
numero_secreto = random.randint(1,3)
def juego_adivinanza():

    intento = int(input("Adivina el número secreto: "))

    if intento == numero_secreto:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. El número era {numero_secreto}")  # Error: 'numero_secrete' no está definido


juego_adivinanza()