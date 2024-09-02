"""
Comparación de valores simples:
Cuando necesitas comparar una variable
con varios valores posibles.
"""
def dia_semana(dia):
    match dia:
        case 1:
            return "Lunes"
        case 2:
            return "Martes"
        case 3:
            return "Miércoles"
        case 4:
            return "Jueves"
        case 5:
            return "Viernes"
        case 6:
            return "Sábado"
        case 7:
            return "Domingo"
        case _:
            return "Día inválido"

# Pedir al usuario que ingrese un número
numero_dia = int(input("Ingresa un número del 1 al 7: "))

# Llamar a la función y mostrar el resultado (aqui aplica lo de el scope de las variables, se explciaron en clases previas)
resultado = dia_semana(numero_dia)
print(f"El día correspondiente es: {resultado}")