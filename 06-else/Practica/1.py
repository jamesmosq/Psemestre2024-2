#Verificador de contraseña
contrasena = input("Crea una contraseña: ")

if len(contrasena) < 8:
    print("La contraseña es demasiado corta")
elif not any(char.isdigit() for char in contrasena):
    print("La contraseña debe contener al menos un número")
elif not any(char.isupper() for char in contrasena):
    print("La contraseña debe contener al menos una letra mayúscula")
else:
    print("Contraseña válida")

