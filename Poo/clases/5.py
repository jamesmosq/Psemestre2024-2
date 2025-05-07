class Habitacion:
    def __init__(self, numero, tipo, precio, capacidad):
        self.numero = numero
        self.tipo = tipo  # "individual", "doble", "suite"
        self.precio = precio
        self.capacidad = capacidad
        self.ocupada = False
        self.cliente = None
        self.dias_reserva = 0

    def reservar(self, cliente, dias):
        if self.ocupada:
            return f"La habitación {self.numero} ya está ocupada."

        self.ocupada = True
        self.cliente = cliente
        self.dias_reserva = dias
        return f"Habitación {self.numero} reservada para {cliente} por {dias} días."

    def liberar(self):
        if not self.ocupada:
            return f"La habitación {self.numero} ya está libre."

        monto = self.precio * self.dias_reserva
        cliente_anterior = self.cliente

        # Resetear valores
        self.ocupada = False
        self.cliente = None
        self.dias_reserva = 0

        return f"Habitación {self.numero} liberada. Cobrar ${monto} a {cliente_anterior}."

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        return f"Precio de habitación {self.numero} actualizado a ${nuevo_precio}."


class Hotel:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        return f"Habitación {habitacion.numero} agregada al hotel {self.nombre}."

    def buscar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return habitacion
        return None

    def habitaciones_disponibles(self):
        disponibles = [h for h in self.habitaciones if not h.ocupada]
        return disponibles

    def reservar_habitacion(self, numero, cliente, dias):
        habitacion = self.buscar_habitacion(numero)
        if habitacion:
            return habitacion.reservar(cliente, dias)
        return f"No se encontró la habitación {numero}."


# Uso del sistema
hotel_mar = Hotel("Hotel Mar Azul", "Av. Costanera 123")

# Agregar habitaciones
h101 = Habitacion(101, "individual", 80, 1)
h102 = Habitacion(102, "doble", 120, 2)
h103 = Habitacion(103, "suite", 200, 4)

hotel_mar.agregar_habitacion(h101)
hotel_mar.agregar_habitacion(h102)
hotel_mar.agregar_habitacion(h103)

# Hacer reservas
print(hotel_mar.reservar_habitacion(101, "Carlos Rodríguez", 3))
print(hotel_mar.reservar_habitacion(103, "Familia Martínez", 5))

# Verificar disponibilidad
disponibles = hotel_mar.habitaciones_disponibles()
print(f"Habitaciones disponibles: {[h.numero for h in disponibles]}")

# Liberar habitación
h101 = hotel_mar.buscar_habitacion(101)
print(h101.liberar())