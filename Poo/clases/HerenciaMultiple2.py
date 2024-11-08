class Vehiculo:
    """Clase base para representar vehículos."""

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def describirse(self):
        print(f"Soy un vehículo {self.marca} {self.modelo} de color {self.color}.")


class Terrestre(Vehiculo):
    """Clase que representa vehículos terrestres."""

    def __init__(self, marca, modelo, color, num_ruedas):
        Vehiculo.__init__(self, marca, modelo, color)
        self.num_ruedas = num_ruedas

    def conducir(self):
        print(f"Conduciendo el {self.marca} {self.modelo} por tierra.")


class Acuatico(Vehiculo):
    """Clase que representa vehículos acuáticos."""

    def __init__(self, marca, modelo, color, velocidad_acuatica):
        Vehiculo.__init__(self, marca, modelo, color)
        self.velocidad_acuatica = velocidad_acuatica

    def navegar(self):
        print(f"Navegando el {self.marca} {self.modelo} por el agua a {self.velocidad_acuatica} km/h.")


class Anfibio(Terrestre, Acuatico):
    """Clase que representa vehículos anfibios."""

    def __init__(self, marca, modelo, color, num_ruedas, velocidad_acuatica):
        Terrestre.__init__(self, marca, modelo, color, num_ruedas)
        Acuatico.__init__(self, marca, modelo, color, velocidad_acuatica)

    def describirse(self):
        print(f"Soy un vehículo anfibio {self.marca} {self.modelo} de color {self.color}.")


# Creamos instancias de las clases
carro = Terrestre("Toyota", "Hilux", "gris", 4)
bote = Acuatico("Yamaha", "Waverunner", "azul", 80)
anfibio = Anfibio("Jetcar", "Amphistar", "amarillo", 4, 50)

# Llamamos a los métodos de las instancias
carro.describirse()
carro.conducir()

bote.describirse()
bote.navegar()

anfibio.describirse()
anfibio.conducir()
anfibio.navegar()
