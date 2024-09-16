# 2.NameError: Juego de adivinanza con variable no definida

def juego_adivinanza():
    numero_secreto = 42
    intento = int(input("Adivina el número secreto: "))

    if intento == numero_secreto:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. El número era {numero_secrete}")  # Error: 'numero_secrete' no está definido


juego_adivinanza()