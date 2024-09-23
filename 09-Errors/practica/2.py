try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("el programa ha termindado de ejecutar")
