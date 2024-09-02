#Función que devuelve múltiples valores:

def dividir_y_residuo(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo

resultado = dividir_y_residuo(17, 5)
print(resultado)  # Imprime: (3, 2)

# O puedes desempaquetar los valores
cociente, residuo = dividir_y_residuo(17, 5)
print(f"Cociente: {cociente}, Residuo: {residuo}")  # Imprime: Cociente: 3, Residuo: 2