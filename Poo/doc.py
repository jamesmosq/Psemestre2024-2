# Clase base

class Electrodomestico:

    def __init__(self, marca, modelo):
        self.marca = marca

        self.modelo = modelo

    def encender(self):
        print(f"{self.marca} {self.modelo} está encendido")


# Clase derivada

class Lavadora(Electrodomestico):

    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)

        self.capacidad = capacidad

    def lavar(self):
        print(f"La lavadora {self.marca} {self.modelo} de {self.capacidad} kg está lavando")


# Prueba

lavadora = Lavadora("LG", "TurboWash", 8)

lavadora.encender()

lavadora.lavar()