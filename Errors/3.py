#3.TypeError: Conversor de temperatura con tipo de dato incorrecto
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

temperatura = input("Ingrese la temperatura en Celsius: ")
fahrenheit = celsius_a_fahrenheit(temperatura)  # Error: 'temperatura' es str, no float
print(f"{temperatura}°C es igual a {fahrenheit}°F")