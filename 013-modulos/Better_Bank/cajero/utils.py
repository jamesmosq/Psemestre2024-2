import json
import os

RUTA_DATOS = os.path.join(os.path.dirname(__file__), '..', 'datos', 'cuentas.json')

def cargar_datos():
    """Carga los datos de las cuentas desde el archivo JSON."""
    if os.path.exists(RUTA_DATOS):
        with open(RUTA_DATOS, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_datos(cuentas):
    """Guarda los datos de las cuentas en el archivo JSON."""
    os.makedirs(os.path.dirname(RUTA_DATOS), exist_ok=True)
    with open(RUTA_DATOS, 'w') as archivo:
        json.dump(cuentas, archivo, indent=2)