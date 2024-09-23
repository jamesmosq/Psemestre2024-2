def es_calificacion_valida(calificacion):
    try:
        calificacion = float(calificacion)
        return 0 <= calificacion <= 10
    except ValueError:
        return False


calificaciones = []
continuar = True

print("Bienvenido al sistema de entrada de calificaciones.")
print("Ingrese las calificaciones de los estudiantes (0-10).")
print("Para terminar, ingrese 'fin'.")

while continuar:
    entrada = input("Ingrese la calificación del estudiante: ")

    if entrada.lower() == 'fin':
        continuar = False
    elif es_calificacion_valida(entrada):
        calificaciones.append(float(entrada))
        print(f"Calificación {entrada} añadida.")
    else:
        print("Entrada inválida. Por favor, ingrese un número entre 0 y 10.")

print("\nResumen de calificaciones ingresadas:")
print(f"Número de calificaciones: {len(calificaciones)}")
if calificaciones:
    print(f"Calificación promedio: {sum(calificaciones) / len(calificaciones):.2f}")
    print(f"Calificación más alta: {max(calificaciones)}")
    print(f"Calificación más baja: {min(calificaciones)}")
else:
    print("No se ingresaron calificaciones.")

print("\nLista de todas las calificaciones:")
for i, calificacion in enumerate(calificaciones, 1):
    print(f"Estudiante {i}: {calificacion}")