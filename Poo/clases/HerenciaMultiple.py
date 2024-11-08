class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class Volador:
    def volar(self):
        print(f"{self.nombre} está volando")

class Nadador:
    def nadar(self):
        print(f"{self.nombre} está nadando")

class Pato(Animal, Volador, Nadador):
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, especie, edad)

# Ejemplo de uso
pato = Pato("Lucas", "Pato común", 2)
pato.volar()  # Esto imprimirá: Lucas está volando
pato.nadar()  # Esto imprimirá: Lucas está nadando
