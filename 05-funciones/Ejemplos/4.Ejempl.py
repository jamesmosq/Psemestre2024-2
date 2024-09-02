#Función con valor por defecto:
def saludar_persona(nombre="Amigo"):
    print(f"Hola, {nombre}!")

saludar_persona()  # Imprime: Hola, Amigo!
saludar_persona("María")  # Imprime: Hola, María!
