# Clase base 1
class Deportista:
    def __init__(self, deporte):
        self.deporte = deporte

    def entrenar(self):
        print(f"Entrenando en {self.deporte}.")

# Clase base 2
class Artista:
    def __init__(self, arte):
        self.arte = arte

    def practicar(self):
        print(f"Practicando {self.arte}.")

# Clase derivada
class PersonaTalentoMixto(Deportista, Artista):
    def __init__(self, deporte, arte):
        Deportista.__init__(self, deporte)
        Artista.__init__(self, arte)

    def mostrar_habilidades(self):
        print(f"Tengo habilidades deportivas en {self.deporte} y habilidades artísticas en {self.arte}.")

# Crear un objeto de PersonaTalentoMixto
persona = PersonaTalentoMixto("fútbol", "pintura")

# Llamar a los métodos
persona.entrenar()
persona.practicar()
persona.mostrar_habilidades()
