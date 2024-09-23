#Ejercicio 11: Menú interactivo con while True
while True:
    print("\nMenú:")
    print("1. Saludar")
    print("2. Mostrar número favorito")
    print("3. Salir")

    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        print("¡Hola! ¿Cómo estás?")
    elif opcion == "2":
        numero_favorito = 7
        print("Mi número favorito es:", numero_favorito)
    elif opcion == "3":
        print("Saliendo del programa...")
        break  # Rompe el ciclo infinito y termina el programa
    else:
        print("Opción no válida. Intenta de nuevo.")
