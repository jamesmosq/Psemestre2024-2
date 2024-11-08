class Vehiculo:
  def __init__(self, marca, modelo, año, color, kilometraje):
    self.marca = marca
    self.modelo = modelo
    self.año = año
    self.color = color
    self.kilometraje = kilometraje

class Carro(Vehiculo):
  def __init__(self, marca, modelo, año, color, kilometraje, tipo_carroceria):
    super().__init__(marca, modelo, año, color, kilometraje)
    self.tipo_carroceria = tipo_carroceria

class Tractomula(Vehiculo):


  def __init__(self, marca, modelo, año, color, kilometraje, capacidad_carga):
    super().__init__(marca, modelo, año, color, kilometraje)
    self.capacidad_carga = capacidad_carga

class Tractor(Vehiculo):
  def __init__(self, marca, modelo, año, color, kilometraje, potencia):
    super().__init__(marca, modelo, año, color, kilometraje)
    self.potencia = potencia

class Terraneitor(Vehiculo):
  def __init__(self, marca, modelo, año, color, kilometraje, altura_libre):
    super().__init__(marca, modelo, año, color, kilometraje)
    self.altura_libre = altura_libre


carro1 = Carro("Toyota", "Corolla", 2020, "Rojo", 50000, "Sedan")
tracto1 = Tractomula("Kenworth", "T680", 2022, "Azul", 100000, 50000)
tractor1 = Tractor("John Deere", "9R", 2023, "Verde", 20000, 400)
terraneitor1 = Terraneitor("Hummer", "De Otro Mundo", 2021, "Negro", 350, "10cm")

"""
print(f"Carro: Marca: {carro1.marca} Modelo: {carro1.modelo} Año: {carro1.año} Color: {carro1.color} Kilometraje: {carro1.kilometraje} Tipo de Carrocería: {carro1.tipo_carroceria}")
print(f"Tractomula: Marca: {tracto1.marca} Modelo: {tracto1.modelo} Año: {tracto1.año} Color: {tracto1.color} Kilometraje: {tracto1.kilometraje} Capacidad de Carga: {tracto1.capacidad_carga}")
print(f"Tractor: Marca: {tractor1.marca} Modelo: {tractor1.modelo} Año: {tractor1.año} Color: {tractor1.color} Kilometraje: {tractor1.kilometraje} Potencia: {tractor1.potencia}")
print(f"Terraneitor: Marca: {terraneitor1.marca} Modelo: {terraneitor1.modelo} Año: {terraneitor1.año} Color: {terraneitor1.color} Kilometraje: {terraneitor1.kilometraje} Altura Libre: {terraneitor1.altura_libre}")
"""
