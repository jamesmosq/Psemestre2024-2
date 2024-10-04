import json
import os

# Configuración del archivo de datos
RUTA_DATOS = 'libros.json'


def cargar_datos():
    """Carga los datos de los libros desde el archivo JSON."""
    if os.path.exists(RUTA_DATOS):
        with open(RUTA_DATOS, 'r') as archivo:
            return json.load(archivo)
    return []


def guardar_datos(libros):
    """Guarda los datos de los libros en el archivo JSON."""
    with open(RUTA_DATOS, 'w') as archivo:
        json.dump(libros, archivo, indent=2)


def inicializar_archivo_json():
    """Inicializa el archivo JSON si no existe."""
    if not os.path.exists(RUTA_DATOS):
        guardar_datos([])
        print(f"Archivo {RUTA_DATOS} creado e inicializado con una lista vacía.")
    else:
        print(f"El archivo {RUTA_DATOS} ya existe.")


def agregar_libro(titulo, autor, año):
    """Agrega un nuevo libro a la biblioteca."""
    libros = cargar_datos()
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "prestado": False
    }
    libros.append(nuevo_libro)
    guardar_datos(libros)
    print(f"Libro agregado: {titulo} por {autor}")


def prestar_libro(titulo):
    """Marca un libro como prestado."""
    libros = cargar_datos()
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower() and not libro["prestado"]:
            libro["prestado"] = True
            guardar_datos(libros)
            print(f"Libro prestado: {libro['titulo']}")
            return
    print("Libro no disponible o no encontrado.")


def devolver_libro(titulo):
    """Marca un libro como devuelto."""
    libros = cargar_datos()
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower() and libro["prestado"]:
            libro["prestado"] = False
            guardar_datos(libros)
            print(f"Libro devuelto: {libro['titulo']}")
            return
    print("No se puede devolver este libro.")


def listar_libros():
    """Muestra todos los libros en la biblioteca."""
    libros = cargar_datos()
    if not libros:
        print("La biblioteca está vacía.")
    else:
        print("Libros en la biblioteca:")
        for libro in libros:
            estado = "Prestado" if libro["prestado"] else "Disponible"
            print(f"- {libro['titulo']} por {libro['autor']} ({libro['año']}) | Estado: {estado}")


def buscar_por_autor(autor):
    """Busca y muestra los libros de un autor específico."""
    libros = cargar_datos()
    libros_autor = [libro for libro in libros if libro["autor"].lower() == autor.lower()]
    if libros_autor:
        print(f"Libros de {autor}:")
        for libro in libros_autor:
            print(f"- {libro['titulo']} ({libro['año']})")
    else:
        print(f"No se encontraron libros de {autor}.")


def menu():
    print("--- Menú de la Biblioteca ---")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar por autor")
    print("6. Salir")
    return input("Seleccione una opción: ")


def main():
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