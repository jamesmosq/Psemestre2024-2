calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

if promedio >= 5:
    print("Aprobaste con un promedio de:", promedio)
else:
    print("Reprobaste con un promedio de:", promedio)