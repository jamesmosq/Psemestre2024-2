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
        print(f"\nEstudiantes en el curso {self.nombre_curso} ({self.codigo_curso}):")
        for estudiante in self.estudiantes:
            estudiante.mostrar_info()


# Crear estudiantes
estudiante1 = Estudiante("Ana", 20, "A001")
estudiante2 = Estudiante("Luis", 22, "A002")
estudiante3 = Estudiante("María", 19, "A003")

estudiante4 = Estudiante("Juana", 20, "A004")
estudiante5 = Estudiante("Luisa", 22, "A005")
estudiante6 = Estudiante("Mariana", 19, "A006")

estudiante7 = Estudiante("Juan", 21, "A007")
estudiante8 = Estudiante("Luisa M", 23, "A008")
estudiante9 = Estudiante("Mariana Luisa", 18, "A009")


# Crear cursos
curso_python = Curso("Python Básico", "PY101")
curso_db = Curso("Bases de datos Básico", "DB102")
curso_web = Curso("Diseño web Básico", "WB102")

# Agregar estudiantes al curso de Python
curso_python.agregar_estudiante(estudiante1)
curso_python.agregar_estudiante(estudiante2)
curso_python.agregar_estudiante(estudiante3)

# Agregar estudiantes al curso de Bases de datos
curso_db.agregar_estudiante(estudiante4)
curso_db.agregar_estudiante(estudiante5)
curso_db.agregar_estudiante(estudiante6)

# Agregar estudiantes al curso de Diseño web
curso_web.agregar_estudiante(estudiante7)
curso_web.agregar_estudiante(estudiante8)
curso_web.agregar_estudiante(estudiante9)

# Mostrar estudiantes de cada curso
print("INFORMACIÓN DE TODOS LOS CURSOS")
curso_python.mostrar_estudiantes()
curso_db.mostrar_estudiantes()
curso_web.mostrar_estudiantes()