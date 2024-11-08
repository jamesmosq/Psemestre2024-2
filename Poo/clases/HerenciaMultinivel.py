class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")


class Deportivo(Coche):
    def __init__(self, marca, modelo, año, puertas, caballos_de_fuerza):
        super().__init__(marca, modelo, año, puertas)
        self.caballos_de_fuerza = caballos_de_fuerza

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Caballos de fuerza: {self.caballos_de_fuerza}")

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando con {self.caballos_de_fuerza} caballos de fuerza.")


# Ejemplo de uso
deportivo = Deportivo("Ferrari", "F8", 2020, 2, 710)
deportivo.mostrar_info()  # Muestra toda la información del deportivo
deportivo.acelerar()  # Simula la aceleración del coche deportivo
