class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class Perro(Animal):
    def __init__(self, nombre, especie, edad, raza):
        super().__init__(nombre, especie, edad)  # Llama al constructor de la clase base
        self.raza = raza

    def ladrar(self):
        print(f"El perro {self.nombre} de raza {self.raza} está ladrando")

# Ejemplo de uso
mi_perro = Perro("Fido", "Canino", 3, "Labrador")
mi_perro.ladrar()  # Esto imprimirá: El perro Fido de raza Labrador está ladrando
