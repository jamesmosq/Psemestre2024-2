class Estudiante:
    def __init__(self, nombre, edad, identificacion):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, ID: {self.identificacion}")


class Curso:
    def __init__(self, nombre_curso, codigo_curso):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Estudiantes en el curso {self.nombre_curso}:")
        for estudiante in self.estudiantes:
            estudiante.mostrar_info()


# Ejemplo

# Crear estudiantes
estudiante1 = Estudiante("Ana", 20, "A001")
estudiante2 = Estudiante("Luis", 22, "A002")
estudiante3 = Estudiante("María", 19, "A003")

# Crear curso
curso_python = Curso("Python Básico", "PY101")

# Agregar estudiantes al curso
curso_python.agregar_estudiante(estudiante1)
curso_python.agregar_estudiante(estudiante2)
curso_python.agregar_estudiante(estudiante3)

# Mostrar estudiantes del curso
curso_python.mostrar_estudiantes()
