import json
import os


def inicializar_archivo_json():
    ruta_datos = os.path.join(os.path.dirname(__file__), 'datos', 'cuentas.json')
    os.makedirs(os.path.dirname(ruta_datos), exist_ok=True)

    if not os.path.exists(ruta_datos):
        cuentas_iniciales = [
            {"numero": "1234", "pin": "1234", "saldo": 1000},
            {"numero": "5678", "pin": "5678", "saldo": 2000}
        ]
        with open(ruta_datos, 'w') as archivo:
            json.dump(cuentas_iniciales, archivo, indent=2)
        print(f"Archivo {ruta_datos} creado e inicializado con cuentas de ejemplo.")
    else:
        print(f"El archivo {ruta_datos} ya existe.")


if __name__ == "__main__":
    inicializar_archivo_json()