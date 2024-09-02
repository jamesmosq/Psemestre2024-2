#Ejercicio 2: Convertidor de unidades
def convertir_unidad(valor, unidad_origen, unidad_destino):
    match (unidad_origen, unidad_destino):
        case ("km", "mi"):
            return valor * 0.621371
        case ("mi", "km"):
            return valor * 1.60934
        case ("kg", "lb"):
            return valor * 2.20462
        case ("lb", "kg"):
            return valor / 2.20462
        case ("c", "f"):
            return (valor * 9 / 5) + 32
        case ("f", "c"):
            return (valor - 32) * 5 / 9
        case _:
            return "Conversión no soportada"


def convertidor():
    print("Convertidor de unidades")
    print("Conversiones soportadas: km<->mi, kg<->lb, c<->f")

    while True:
        entrada = input("Ingresa la conversión (ejemplo: 10 km mi) o 'q' para salir: ")
        if entrada.lower() == 'q':
            break

        try:
            valor, unidad_origen, unidad_destino = entrada.split()
            valor = float(valor)
            resultado = convertir_unidad(valor, unidad_origen.lower(), unidad_destino.lower())

            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"{valor} {unidad_origen} = {resultado:.2f} {unidad_destino}")
        except ValueError:
            print("Entrada no válida. Usa el formato: valor unidad_origen unidad_destino")


convertidor()