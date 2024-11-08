class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def descripcion(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.anio_publicacion}"


class Biblioteca:
    def __init__(self, nombre_biblioteca):
        self.nombre_biblioteca = nombre_biblioteca
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"Libros en la {self.nombre_biblioteca}:")
        for libro in self.libros:
            print(libro.descripcion())

    def buscar_por_autor(self, autor):
        print(f"Buscando libros por {autor} en la {self.nombre_biblioteca}:")
        for libro in self.libros:
            if libro.autor == autor:
                print(libro.descripcion())


# Ejemplo de uso

# Crear libros
libro1 = Libro("1984", "George Orwell", 1949)
libro2 = Libro("To Kill a Mockingbird", "Harper Lee", 1960)
libro3 = Libro("Animal Farm", "George Orwell", 1945)

# Crear biblioteca
mi_biblioteca = Biblioteca("Biblioteca Central")

# Agregar libros a la biblioteca
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)
mi_biblioteca.agregar_libro(libro3)

# Mostrar todos los libros en la biblioteca
mi_biblioteca.mostrar_libros()

# Buscar libros por autor
mi_biblioteca.buscar_por_autor("George Orwell")
