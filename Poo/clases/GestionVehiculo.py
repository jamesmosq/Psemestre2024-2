class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"{self.anio} {self.marca} {self.modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, numero_puertas):
        super().__init__(marca, modelo, anio)
        self.numero_puertas = numero_puertas

    def descripcion(self):
        return f"{super().descripcion()}, {self.numero_puertas} puertas"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo

    def descripcion(self):
        return f"{super().descripcion()}, tipo: {self.tipo}"


# Ejemplo de uso

# Crear instancias de Coche
coche1 = Coche("Toyota", "Corolla", 2020, 4)
coche2 = Coche("Honda", "Civic", 2018, 2)

# Crear instancias de Moto
moto1 = Moto("Yamaha", "MT-07", 2019, "Deportiva")
moto2 = Moto("Harley-Davidson", "Street 750", 2021, "Cruiser")

# Mostrar descripciones de los vehículos
print(coche1.descripcion())  # Salida: 2020 Toyota Corolla, 4 puertas
print(coche2.descripcion())  # Salida: 2018 Honda Civic, 2 puertas
print(moto1.descripcion())   # Salida: 2019 Yamaha MT-07, tipo: Deportiva
print(moto2.descripcion())   # Salida: 2021 Harley-Davidson Street 750, tipo: Cruiser
