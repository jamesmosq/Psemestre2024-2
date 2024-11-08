class Plato:
    def __init__(self, nombre_plato, precio):
        self.nombre_plato = nombre_plato
        self.precio = precio

    def descripcion(self):
        return f"Plato: {self.nombre_plato}, Precio: ${self.precio:.2f}"


class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.platos = []

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def mostrar_pedido(self):
        print(f"Pedido Número: {self.numero_pedido}")
        for plato in self.platos:
            print(plato.descripcion())

    def total_pedido(self):
        total = sum(plato.precio for plato in self.platos)
        return total


# Ejemplo de uso

# Crear platos
plato1 = Plato("Ensalada César", 7.50)
plato2 = Plato("Pizza Margarita", 12.00)
plato3 = Plato("Sopa de Tomate", 5.25)

# Crear pedido
pedido1 = Pedido(101)

# Agregar platos al pedido
pedido1.agregar_plato(plato1)
pedido1.agregar_plato(plato2)
pedido1.agregar_plato(plato3)

# Mostrar pedido y total
pedido1.mostrar_pedido()
print(f"Total del pedido: ${pedido1.total_pedido():.2f}")
