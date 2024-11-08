class Coche:
    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad

    def arrancar(self):
        print(f"El coche de color {self.color} ha arrancado")

    def frenar(self):
        print("El coche ha frenado")


# Crear un objeto de la clase Coche
mi_coche = Coche("rojo", 120)
mi_coche.arrancar()
