
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el primer número: "))
    division = num1 / num2
    print(division)
except ValueError:
    print("Error: datos invalidos.")
    division = None
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
