#Ejercicio 1: Calculadora simple
def calculadora():
    print("Calculadora simple")
    print("Operaciones: suma (+), resta (-), multiplicación (*), división (/)")

    while True:
        entrada = input("Ingresa una operación (ejemplo: 5 + 3) o 'q' para salir: ")
        if entrada.lower() == 'q':
            break

        try:
            num1, operador, num2 = entrada.split()
            num1, num2 = float(num1), float(num2)

            match operador:
                case "+":
                    resultado = num1 + num2
                case "-":
                    resultado = num1 - num2
                case "*":
                    resultado = num1 * num2
                case "/":
                    if num2 == 0:
                        print("Error: División por cero")
                        continue
                    resultado = num1 / num2
                case _:
                    print("Operador no válido")
                    continue

            print(f"Resultado: {resultado}")
        except ValueError:
            print("Entrada no válida. Usa el formato: número operador número")


calculadora()
