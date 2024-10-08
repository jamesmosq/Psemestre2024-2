import json
from .utils import cargar_datos, guardar_datos

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

if __name__ == "__main__":
    # Código de prueba
    agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    agregar_libro("1984", "George Orwell", 1949)
    listar_libros()
    prestar_libro("1984")
    buscar_por_autor("Gabriel García Márquez")