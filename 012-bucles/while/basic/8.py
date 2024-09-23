#Ejercicio 8: Ciclo infinito con break
while True:
    comando = input("Escribe 'detener' para salir del ciclo: ")
    if comando.lower() == "detener":
        print("Ciclo terminado.")
        break
    print("Sigue corriendo el ciclo.")
