try:
    archivo = open('archivo.txt', 'r')
    # Procesar el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado.")
finally:
    archivo.close()
