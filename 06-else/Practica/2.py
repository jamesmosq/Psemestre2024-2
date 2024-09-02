#Conversor de unidades de temperatura

temperatura = float(input("Ingresa la temperatura: "))
unidad = input("¿Es Celsius o Fahrenheit? (C/F): ").upper()

if unidad == "C":
    fahrenheit = (temperatura * 9/5) + 32
    print(f"{temperatura}°C es igual a {fahrenheit:.1f}°F")
elif unidad == "F":
    celsius = (temperatura - 32) * 5/9
    print(f"{temperatura}°F es igual a {celsius:.1f}°C")
else:
    print("Unidad no válida")