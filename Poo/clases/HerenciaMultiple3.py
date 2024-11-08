# Definición de la primera clase base
class Mamifero:
    def __init__(self, nombre):
        self.nombre = nombre

    def amamantar(self):
        return f"{self.nombre} está amamantando a sus crías."

# Definición de la segunda clase base
class Volador:
    def __init__(self):
        self.altura_vuelo = 0

    def volar(self, altura):
        self.altura_vuelo = altura
        return f"Volando a una altura de {self.altura_vuelo} metros."

# Definición de la clase derivada que hereda de Mamifero y Volador
class Murcielago(Mamifero, Volador):
    def __init__(self, nombre):
        # Llamada al constructor de Mamifero
        Mamifero.__init__(self, nombre)
        # Llamada al constructor de Volador
        Volador.__init__(self)

    def hacer_sonido(self):
        return "El murciélago hace un sonido agudo."

# Crear una instancia de la clase Murcielago
murcielago = Murcielago("Batty")

# Usar los métodos de las clases base y de la clase derivada
print(murcielago.amamantar())       # Output: Batty está amamantando a sus crías.
print(murcielago.volar(10))         # Output: Volando a una altura de 10 metros.
print(murcielago.hacer_sonido())    # Output: El murciélago hace un sonido agudo.
