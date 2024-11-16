# 1. Vehículos
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        return "El vehículo está arrancando"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    
    def abrir_maletero(self):
        return "Maletero abierto"

# 2. Animales
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

# 3. Formas Geométricas
class Forma:
    def calcular_area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

# 4. Empleados
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def trabajar(self):
        return "Trabajando..."

class Programador(Empleado):
    def programar(self):
        return "Escribiendo código"

# 5. Dispositivos Electrónicos
class DispositivoElectronico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def encender(self):
        self.encendido = True

class Telefono(DispositivoElectronico):
    def hacer_llamada(self, numero):
        return f"Llamando a {numero}..."

# 6. Instrumentos Musicales
class InstrumentoMusical:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def tocar(self):
        pass

class Guitarra(InstrumentoMusical):
    def tocar(self):
        return "Tocando acordes"

# 7. Productos
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def obtener_info(self):
        return f"{self.nombre}: ${self.precio}"

class Libro(Producto):
    def __init__(self, nombre, precio, autor):
        super().__init__(nombre, precio)
        self.autor = autor

# 8. Cuentas Bancarias
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad

class CuentaAhorro(CuentaBancaria):
    def calcular_interes(self, tasa):
        return self.saldo * tasa

# 9. Bebidas
class Bebida:
    def __init__(self, nombre, temperatura):
        self.nombre = nombre
        self.temperatura = temperatura
    
    def servir(self):
        return f"Sirviendo {self.nombre}"

class Cafe(Bebida):
    def agregar_azucar(self):
        return "Añadiendo azúcar al café"

# 10. Usuarios
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def login(self):
        return "Iniciando sesión"

class Administrador(Usuario):
    def administrar_sistema(self):
        return "Administrando el sistema"
