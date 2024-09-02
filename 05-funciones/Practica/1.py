def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_a_kelvin(celsius):
    return celsius + 273.15


def kelvin_a_celsius(kelvin):
    return kelvin - 273.15


def conversor_temperatura():
    print("Conversor de Temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")

    opcion = int(input("Elige una opción (1-4): "))
    temperatura = float(input("Ingresa la temperatura a convertir: "))

    if opcion == 1:
        resultado = celsius_a_fahrenheit(temperatura)
        print(f"{temperatura}°C es igual a {resultado:.2f}°F")
    elif opcion == 2:
        resultado = fahrenheit_a_celsius(temperatura)
        print(f"{temperatura}°F es igual a {resultado:.2f}°C")
    elif opcion == 3:
        resultado = celsius_a_kelvin(temperatura)
        print(f"{temperatura}°C es igual a {resultado:.2f}K")
    elif opcion == 4:
        resultado = kelvin_a_celsius(temperatura)
        print(f"{temperatura}K es igual a {resultado:.2f}°C")
    else:
        print("Opción no válida")


# Uso de la función principal
conversor_temperatura()

"""
Ejercicio : Conversor de temperatura
Descripción:
Crea funciones para convertir entre Celsius, Fahrenheit y Kelvin. Luego, 
crea una función principal que permita al 
usuario elegir la conversión que desea realizar.
"""