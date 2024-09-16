#6.Manejo de múltiples excepciones: Divisor de números
def dividir_numeros():
    try:
        numerador = float(input("Ingrese el numerador: "))
        denominador = float(input("Ingrese el denominador: "))
        resultado = numerador / denominador
        print(f"El resultado es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingrese solo números.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

dividir_numeros()

