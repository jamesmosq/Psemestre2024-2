import json
import os

# Rutas de los archivos de datos
RUTA_LIBROS = 'datos/libros.json'
RUTA_USUARIOS = 'datos/usuarios.json'
RUTA_PRESTAMOS = 'datos/prestamos.json'


def inicializar_archivos():
    """Inicializa todos los archivos JSON necesarios."""
    for ruta in [RUTA_LIBROS, RUTA_USUARIOS, RUTA_PRESTAMOS]:
        # Asegurarse de que el directorio datos existe
        os.makedirs(os.path.dirname(ruta), exist_ok=True)

        if not os.path.exists(ruta):
            with open(ruta, 'w') as archivo:
                json.dump([], archivo)
            print(f"Archivo {ruta} creado e inicializado.")
        else:
            print(f"El archivo {ruta} ya existe.")


if __name__ == "__main__":
    inicializar_archivos()