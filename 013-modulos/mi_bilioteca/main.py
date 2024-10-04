from biblioteca import agregar_libro, listar_libros, prestar_libro, devolver_libro, buscar_por_autor
from inicializar_datos import inicializar_archivo_json


def menu():
    print("\n--- Menú de la Biblioteca ---")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar por autor")
    print("6. Salir")
    return input("Seleccione una opción: ")


def main():
    # Inicializar el archivo de datos
    inicializar_archivo_json()

    while True:
        opcion = menu()
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año = input("Ingrese el año de publicación: ")
            agregar_libro(titulo, autor, año)
        elif opcion == '2':
            listar_libros()
        elif opcion == '3':
            titulo = input("Ingrese el título del libro a prestar: ")
            prestar_libro(titulo)
        elif opcion == '4':
            titulo = input("Ingrese el título del libro a devolver: ")
            devolver_libro(titulo)
        elif opcion == '5':
            autor = input("Ingrese el nombre del autor: ")
            buscar_por_autor(autor)
        elif opcion == '6':
            print("¡Gracias por usar la biblioteca!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()