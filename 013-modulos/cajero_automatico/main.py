from cajero import iniciar_sesion, consultar_saldo, depositar, retirar
from inicializar_datos import inicializar_archivo_json


def menu():
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    return input("Seleccione una opción: ")


def main():
    inicializar_archivo_json()

    cuenta = iniciar_sesion()
    if not cuenta:
        print("No se pudo iniciar sesión. El programa se cerrará.")
        return

    while True:
        opcion = menu()
        if opcion == '1':
            consultar_saldo(cuenta)
        elif opcion == '2':
            monto = float(input("Ingrese el monto a depositar: "))
            depositar(cuenta, monto)
        elif opcion == '3':
            monto = float(input("Ingrese el monto a retirar: "))
            retirar(cuenta, monto)
        elif opcion == '4':
            print("Gracias por usar nuestro cajero automático.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()