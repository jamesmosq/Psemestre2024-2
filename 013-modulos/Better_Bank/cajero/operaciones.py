from .utils import cargar_datos, guardar_datos


def iniciar_sesion():
    cuentas = cargar_datos()
    numero_cuenta = input("Ingrese el número de cuenta: ")
    pin = input("Ingrese el PIN: ")

    for cuenta in cuentas:
        if cuenta['numero'] == numero_cuenta and cuenta['pin'] == pin:
            print(f"Bienvenido, usuario de la cuenta {numero_cuenta}")
            return cuenta

    print("Número de cuenta o PIN incorrectos.")
    return None


def consultar_saldo(cuenta):
    print(f"Su saldo actual es: ${cuenta['saldo']:.2f}")


def depositar(cuenta, monto):
    if monto > 0:
        cuenta['saldo'] += monto
        guardar_datos(cargar_datos())  # Actualiza los datos en el archivo
        print(f"Depósito de ${monto:.2f} realizado con éxito.")
        consultar_saldo(cuenta)
    else:
        print("El monto a depositar debe ser mayor que cero.")


def retirar(cuenta, monto):
    if monto > 0:
        if cuenta['saldo'] >= monto:
            cuenta['saldo'] -= monto
            guardar_datos(cargar_datos())  # Actualiza los datos en el archivo
            print(f"Retiro de ${monto:.2f} realizado con éxito.")
            consultar_saldo(cuenta)
        else:
            print("Saldo insuficiente para realizar el retiro.")
    else:
        print("El monto a retirar debe ser mayor que cero.")