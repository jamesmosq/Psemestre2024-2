#5.ValueError: Calculadora de edad con entrada inválida

def calcular_edad():
    año_nacimiento = input("Ingrese su año de nacimiento: ")
    año_actual = 2023
    edad = año_actual - int(año_nacimiento)
    print(f"Tienes {edad} años.")

calcular_edad()  # Error si el usuario ingresa algo que no sea un número