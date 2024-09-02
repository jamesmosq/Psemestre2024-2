#Clasificador de edades

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad no válida")
elif edad < 13:
    print("Eres un niño")
elif edad < 20:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")