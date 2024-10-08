import json
import os
from datetime import datetime, timedelta

# Rutas de los archivos de datos
RUTA_LIBROS = 'datos/libros.json'
RUTA_USUARIOS = 'datos/usuarios.json'
RUTA_PRESTAMOS = 'datos/prestamos.json'


# Funciones de utilidad para manejo de archivos
def cargar_datos(ruta):
    """Carga datos desde un archivo JSON."""
    with open(ruta, 'r') as archivo:
        return json.load(archivo)


def guardar_datos(datos, ruta):
    """Guarda datos en un archivo JSON."""
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=2)


# Funciones de gestión de usuarios y administradores
def login_admin(username, password):
    """Verifica las credenciales del administrador."""
    usuarios = cargar_datos(RUTA_USUARIOS)
    for usuario in usuarios:
        if (usuario['username'] == username and
                usuario['password'] == password and
                usuario['es_admin']):
            return usuario
    return None


def registrar_admin(username, password, nombre):
    """Registra un nuevo administrador."""
    usuarios = cargar_datos(RUTA_USUARIOS)
    nuevo_admin = {
        "username": username,
        "password": password,
        "nombre": nombre,
        "es_admin": True
    }
    usuarios.append(nuevo_admin)
    guardar_datos(usuarios, RUTA_USUARIOS)
    print(f"Administrador {username} registrado exitosamente.")


def registrar_usuario(nombre, telefono, ref_nombre, ref_telefono):
    """Registra un nuevo usuario con contacto de referencia."""
    usuarios = cargar_datos(RUTA_USUARIOS)
    nuevo_usuario = {
        "nombre": nombre,
        "telefono": telefono,
        "referencia": {
            "nombre": ref_nombre,
            "telefono": ref_telefono
        },
        "es_admin": False
    }
    usuarios.append(nuevo_usuario)
    guardar_datos(usuarios, RUTA_USUARIOS)
    print(f"Usuario {nombre} registrado exitosamente.")


# Funciones de gestión de biblioteca
def agregar_libro(titulo, autor, año):
    """Agrega un nuevo libro a la biblioteca."""
    libros = cargar_datos(RUTA_LIBROS)
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "prestado": False
    }
    libros.append(nuevo_libro)
    guardar_datos(libros, RUTA_LIBROS)
    print(f"Libro agregado: {titulo} por {autor}")


def prestar_libro(titulo, nombre_usuario):
    """Registra el préstamo de un libro."""
    libros = cargar_datos(RUTA_LIBROS)
    usuarios = cargar_datos(RUTA_USUARIOS)
    prestamos = cargar_datos(RUTA_PRESTAMOS)

    # Verificar si el usuario existe
    usuario = next((u for u in usuarios if u['nombre'] == nombre_usuario and not u['es_admin']), None)
    if not usuario:
        print("Usuario no encontrado.")
        return

    # Buscar el libro
    libro = next((l for l in libros if l['titulo'].lower() == titulo.lower() and not l['prestado']), None)
    if not libro:
        print("Libro no disponible.")
        return

    # Registrar el préstamo
    fecha_prestamo = datetime.now()
    fecha_devolucion = fecha_prestamo + timedelta(days=5)

    nuevo_prestamo = {
        "titulo_libro": libro['titulo'],
        "usuario": nombre_usuario,
        "fecha_prestamo": fecha_prestamo.isoformat(),
        "fecha_devolucion_esperada": fecha_devolucion.isoformat(),
        "devuelto": False
    }

    prestamos.append(nuevo_prestamo)
    guardar_datos(prestamos, RUTA_PRESTAMOS)

    # Actualizar estado del libro
    for l in libros:
        if l['titulo'] == libro['titulo']:
            l['prestado'] = True
    guardar_datos(libros, RUTA_LIBROS)

    print(f"Libro prestado a {nombre_usuario}. Fecha de devolución: {fecha_devolucion.strftime('%Y-%m-%d')}")


def devolver_libro(titulo):
    """Registra la devolución de un libro y calcula multas si aplica."""
    libros = cargar_datos(RUTA_LIBROS)
    prestamos = cargar_datos(RUTA_PRESTAMOS)

    # Buscar el préstamo activo para este libro
    prestamo = next((p for p in prestamos
                     if p['titulo_libro'].lower() == titulo.lower()
                     and not p['devuelto']), None)

    if not prestamo:
        print("No se encontró un préstamo activo para este libro.")
        return

    fecha_devolucion = datetime.now()
    fecha_esperada = datetime.fromisoformat(prestamo['fecha_devolucion_esperada'])

    # Calcular multa si aplica
    dias_retraso = (fecha_devolucion - fecha_esperada).days
    multa = max(0, dias_retraso - 3) * 1000  # $1000 por día después de 3 días de retraso

    # Actualizar el préstamo
    for p in prestamos:
        if p['titulo_libro'].lower() == titulo.lower() and not p['devuelto']:
            p['devuelto'] = True
            p['fecha_devolucion_real'] = fecha_devolucion.isoformat()
            if multa > 0:
                p['multa'] = multa

    # Actualizar el estado del libro
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            libro['prestado'] = False

    guardar_datos(prestamos, RUTA_PRESTAMOS)
    guardar_datos(libros, RUTA_LIBROS)

    print(f"Libro devuelto: {titulo}")
    if multa > 0:
        print(f"Se ha generado una multa de ${multa} por retraso en la devolución.")


def listar_libros():
    """Muestra todos los libros en la biblioteca."""
    libros = cargar_datos(RUTA_LIBROS)
    if not libros:
        print("La biblioteca está vacía.")
    else:
        print("Libros en la biblioteca:")
        for libro in libros:
            estado = "Prestado" if libro["prestado"] else "Disponible"
            print(f"- {libro['titulo']} por {libro['autor']} ({libro['año']}) | Estado: {estado}")


def buscar_por_autor(autor):
    """Busca y muestra los libros de un autor específico."""
    libros = cargar_datos(RUTA_LIBROS)
    libros_autor = [libro for libro in libros if libro["autor"].lower() == autor.lower()]
    if libros_autor:
        print(f"Libros de {autor}:")
        for libro in libros_autor:
            estado = "Prestado" if libro["prestado"] else "Disponible"
            print(f"- {libro['titulo']} ({libro['año']}) | Estado: {estado}")
    else:
        print(f"No se encontraron libros de {autor}.")


# Funciones de menú
def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Login Administrador")
    print("2. Registrar Administrador")
    print("3. Salir")
    return input("Seleccione una opción: ")


def menu_admin():
    print("\n--- Menú de Administrador ---")
    print("1. Registrar Usuario")
    print("2. Agregar Libro")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Listar Libros")
    print("6. Buscar por Autor")
    print("7. Cerrar Sesión")
    return input("Seleccione una opción: ")


# Función principal
def main():
    admin_actual = None

    while True:
        opcion = menu_principal()

        if opcion == '1':
            username = input("Usuario: ")
            password = input("Contraseña: ")
            admin_actual = login_admin(username, password)
            if admin_actual:
                print(f"Bienvenido, {username}!")
                while True:
                    opcion_admin = menu_admin()
                    if opcion_admin == '1':
                        nombre = input("Nombre del usuario: ")
                        telefono = input("Teléfono del usuario: ")
                        ref_nombre = input("Nombre de la referencia: ")
                        ref_telefono = input("Teléfono de la referencia: ")
                        registrar_usuario(nombre, telefono, ref_nombre, ref_telefono)
                    elif opcion_admin == '2':
                        titulo = input("Título del libro: ")
                        autor = input("Autor del libro: ")
                        año = input("Año de publicación: ")
                        agregar_libro(titulo, autor, año)
                    elif opcion_admin == '3':
                        titulo = input("Título del libro: ")
                        usuario = input("Nombre del usuario: ")
                        prestar_libro(titulo, usuario)
                    elif opcion_admin == '4':
                        titulo = input("Título del libro: ")
                        devolver_libro(titulo)
                    elif opcion_admin == '5':
                        listar_libros()
                    elif opcion_admin == '6':
                        autor = input("Nombre del autor: ")
                        buscar_por_autor(autor)
                    elif opcion_admin == '7':
                        admin_actual = None
                        print("Sesión cerrada.")
                        break
            else:
                print("Credenciales inválidas.")
        elif opcion == '2':
            username = input("Nuevo usuario admin: ")
            password = input("Contraseña: ")
            nombre = input("Nombre completo: ")
            registrar_admin(username, password, nombre)
        elif opcion == '3':
            print("¡Gracias por usar el sistema de biblioteca!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
    #https://claude.ai/chat/942e6788-08ff-4454-884e-7ac79be8752e