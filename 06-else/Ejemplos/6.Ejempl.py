#Ejemplo práctico: Verificación de contraseña

contrasena_correcta = "python123"
intento = input("Ingresa la contraseña: ")

if intento == contrasena_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")