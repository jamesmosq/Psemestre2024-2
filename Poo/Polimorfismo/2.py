# ===========================================
# 1. POLIMORFISMO DE SUBTIPO (HERENCIA)
# ===========================================

class Vehiculo:
    def arrancar(self):
        return "El vehículo arranca"


class Coche(Vehiculo):
    def arrancar(self):
        return "El coche arranca con llave"


class Moto(Vehiculo):
    def arrancar(self):
        return "La moto arranca con botón"


# Uso polimórfico
vehiculos = [Coche(), Moto()]
for vehiculo in vehiculos:
    print(vehiculo.arrancar())

print("+" * 50) # no me preginte para qye es


# ===========================================
# 2. POLIMORFISMO AD-HOC (SOBRECARGA)
# ===========================================

# A) Sobrecarga de operadores
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __add__(self, otro):
        # Sumar precios
        return self.precio + otro.precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"


producto1 = Producto("Laptop", 1000)
producto2 = Producto("Mouse", 50)

print(f"Total: ${producto1 + producto2}")  # Usa __add__
print(producto1)  # Usa __str__

print("-" * 50)


# B) Sobrecarga de métodos (simulada)
class Calculadora:
    def sumar(self, *args):
        if len(args) == 2:
            return f"Suma de 2 números: {args[0] + args[1]}"
        elif len(args) == 3:
            return f"Suma de 3 números: {sum(args)}"
        else:
            return f"Suma de {len(args)} números: {sum(args)}"


calc = Calculadora()
print(calc.sumar(5, 3))
print(calc.sumar(5, 3, 2))
print(calc.sumar(1, 2, 3, 4, 5))

print("-" * 50)

# ===========================================
# 3. POLIMORFISMO PARAMÉTRICO (GENERICS)
# ===========================================

from typing import TypeVar, Generic, List

T = TypeVar('T')


class Almacen(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def agregar(self, item: T):
        self.items.append(item)
        print(f"Agregado: {item}")

    def obtener_todos(self) -> List[T]:
        return self.items


# Uso con diferentes tipos
almacen_numeros = Almacen[int]()
almacen_numeros.agregar(10)
almacen_numeros.agregar(20)

almacen_nombres = Almacen[str]()
almacen_nombres.agregar("Juan")
almacen_nombres.agregar("María")

print(f"Números: {almacen_numeros.obtener_todos()}")
print(f"Nombres: {almacen_nombres.obtener_todos()}")

print("-" * 50)


# ===========================================
# 4. DUCK TYPING
# ===========================================

class Pato:
    def caminar(self):
        return "El pato camina balanceándose"

    def nadar(self):
        return "El pato nada en el agua"


class Persona:
    def caminar(self):
        return "La persona camina erguida"

    def nadar(self):
        return "La persona nada estilo libre"


class Robot:
    def caminar(self):
        return "El robot camina mecánicamente"

    def nadar(self):
        return "El robot no puede nadar"


# Función que acepta cualquier objeto que pueda "caminar" y "nadar"
def actividades_acuaticas(ser):
    print(ser.caminar())
    print(ser.nadar())
    print()


# Todos funcionan sin herencia común
seres = [Pato(), Persona(), Robot()]
for ser in seres:
    actividades_acuaticas(ser)

print("-" * 50)


# ===========================================
#  PRÁCTICANDO 🫡 COMBINADO
# ===========================================

# Sistema de notificaciones usando duck typing
class EmailNotificador:
    def enviar(self, mensaje):
        return f"📧 Email: {mensaje}"


class SMSNotificador:
    def enviar(self, mensaje):
        return f"📱 SMS: {mensaje}"


class PushNotificador:
    def enviar(self, mensaje):
        return f"🔔 Push: {mensaje}"


class SistemaNotificaciones:
    def __init__(self):
        self.notificadores = []

    def agregar_notificador(self, notificador):
        # Duck typing: solo necesita tener método 'enviar'
        self.notificadores.append(notificador)

    def notificar_todos(self, mensaje):
        for notificador in self.notificadores:
            print(notificador.enviar(mensaje))


sistema = SistemaNotificaciones()
sistema.agregar_notificador(EmailNotificador())
sistema.agregar_notificador(SMSNotificador())
sistema.agregar_notificador(PushNotificador())

sistema.notificar_todos("¡Nueva actualización disponible!")
# para agregar emojis a los mensajes en windows: usa la teclca de windows + punto (.) y selecciona el emoji que quieras
# Para agregar emojis a los mensajes en linux: esos no me los sé ☹️