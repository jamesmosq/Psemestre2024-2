#Ejercicio 3: Analizador de comandos de un juego
def ejecutar_comando(comando):
    partes = comando.split()
    accion = partes[0].lower()

    match accion:
        case "mover":
            if len(partes) != 2:
                return "Uso: mover [norte|sur|este|oeste]"
            direccion = partes[1].lower()
            match direccion:
                case "norte" | "sur" | "este" | "oeste":
                    return f"Te has movido hacia el {direccion}"
                case _:
                    return "Dirección no válida"
        case "atacar":
            if len(partes) != 2:
                return "Uso: atacar [enemigo]"
            enemigo = partes[1]
            return f"Has atacado a {enemigo}"
        case "tomar":
            if len(partes) != 2:
                return "Uso: tomar [item]"
            item = partes[1]
            return f"Has tomado {item}"
        case "inventario":
            return "Mostrando inventario..."
        case "salir":
            return "Saliendo del juego..."
        case _:
            return "Comando no reconocido"


def juego():
    print("Bienvenido al juego de aventura por texto")
    print("Comandos disponibles: mover, atacar, tomar, inventario, salir")

    while True:
        comando = input("Ingresa un comando: ")
        resultado = ejecutar_comando(comando)
        print(resultado)
        if resultado == "Saliendo del juego...":
            break


juego()