# 1. Dispositivo Multifuncional (Impresora/Scanner/Fax)
class Impresora:
    def imprimir(self):
        return "Imprimiendo documento..."

class Scanner:
    def escanear(self):
        return "Escaneando documento..."

class Fax:
    def enviar_fax(self):
        return "Enviando fax..."

class DispositivoMultifuncional(Impresora, Scanner, Fax):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def estado(self):
        return f"Dispositivo {self.marca} {self.modelo} listo"

# 2. Estudiante Deportista
class Estudiante:
    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado
    
    def estudiar(self):
        return "Estudiando..."

class Deportista:
    def __init__(self, deporte):
        self.deporte = deporte
    
    def entrenar(self):
        return "Entrenando..."

class EstudianteDeportista(Estudiante, Deportista):
    def __init__(self, nombre, grado, deporte):
        Estudiante.__init__(self, nombre, grado)
        Deportista.__init__(self, deporte)
    
    def rutina_diaria(self):
        return f"Estudiando {self.grado} y entrenando {self.deporte}"

# 3. Vehículo Anfibio
class VehiculoTerrestre:
    def conducir(self):
        return "Conduciendo en tierra"
    
    def frenar(self):
        return "Frenando"

class VehiculoAcuatico:
    def navegar(self):
        return "Navegando en agua"
    
    def anclar(self):
        return "Anclando"

class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    def cambiar_modo(self, modo):
        return f"Cambiando a modo {modo}"

# 4. Robot Trabajador
class Robot:
    def __init__(self, id):
        self.id = id
    
    def cargar_bateria(self):
        return "Cargando batería..."

class Trabajador:
    def trabajar(self):
        return "Trabajando..."

class Guardia:
    def vigilar(self):
        return "Vigilando..."

class RobotGuardiaTrabajador(Robot, Trabajador, Guardia):
    def estado(self):
        return f"Robot {self.id} operativo"

# 5. Ave Mascota
class Ave:
    def volar(self):
        return "Volando..."
    
    def cantar(self):
        return "Cantando..."

class Mascota:
    def __init__(self, nombre, dueño):
        self.nombre = nombre
        self.dueño = dueño
    
    def jugar(self):
        return "Jugando..."

class Loro(Ave, Mascota):
    def hablar(self):
        return "Repitiendo palabras..."

# 6. Empleado Remoto
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def trabajar(self):
        return "Trabajando..."

class TrabajadorRemoto:
    def conectar(self):
        return "Conectado al servidor remoto"
    
    def desconectar(self):
        return "Desconectado del servidor remoto"

class ConsultorIT(Empleado, TrabajadorRemoto):
    def reunion_virtual(self):
        return "En reunión virtual"

# 7. Producto Digital Descargable
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def obtener_info(self):
        return f"{self.nombre}: ${self.precio}"

class Descargable:
    def descargar(self):
        return "Descargando..."
    
    def verificar_integridad(self):
        return "Verificando archivo..."

class Software(Producto, Descargable):
    def instalar(self):
        return "Instalando software..."

# 8. Personaje de Juego
class Guerrero:
    def atacar(self):
        return "Atacando con espada"
    
    def defender(self):
        return "Defendiendo con escudo"

class Mago:
    def lanzar_hechizo(self):
        return "Lanzando hechizo"
    
    def meditar(self):
        return "Meditando para recuperar maná"

class GuerreroMago(Guerrero, Mago):
    def ataque_magico(self):
        return "Atacando con espada mágica"

# 9. Documento Digital
class Documento:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar(self):
        return f"Mostrando {self.titulo}"

class Encriptable:
    def encriptar(self):
        return "Encriptando documento..."
    
    def desencriptar(self):
        return "Desencriptando documento..."

class DocumentoSeguro(Documento, Encriptable):
    def guardar_seguro(self):
        self.encriptar()
        return "Documento guardado de forma segura"

# 10. Animal Doméstico Entrenado
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer(self):
        return "Comiendo..."

class Domestico:
    def vivir_en_casa(self):
        return "Viviendo en casa"

class Entrenado:
    def realizar_truco(self):
        return "Realizando truco"

class PerroEntrenado(Animal, Domestico, Entrenado):
    def __init__(self, nombre, edad, trucos):
        super().__init__(nombre, edad)
        self.trucos = trucos
    
    def mostrar_trucos(self):
        return f"Trucos conocidos: {', '.join(self.trucos)}"
