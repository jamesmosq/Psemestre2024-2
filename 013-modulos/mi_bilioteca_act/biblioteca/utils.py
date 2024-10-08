import json
import os

RUTA_DATOS = os.path.join(os.path.dirname(__file__), '..', 'datos', 'libros.json')

def cargar_datos():
    """Carga los datos de los libros desde el archivo JSON."""
    if os.path.exists(RUTA_DATOS):
        with open(RUTA_DATOS, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_datos(libros):
    """Guarda los datos de los libros en el archivo JSON."""
    os.makedirs(os.path.dirname(RUTA_DATOS), exist_ok=True)
    with open(RUTA_DATOS, 'w') as archivo:
        json.dump(libros, archivo, indent=2)