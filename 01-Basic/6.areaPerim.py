figura = input("Ingrese la figura (cuadrado, círculo, triángulo): ")

if figura == "cuadrado":
    lado = float(input("Ingrese la longitud del lado: "))
    area = lado * lado
    perimetro = 4 * lado
elif figura == "circulo":
    radio = float(input("Ingrese el radio del círculo: "))
    import math
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
elif figura == "triangulo":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    # Para calcular el perímetro necesitaríamos los tres lados
    print("Para calcular el perímetro del triángulo se necesitan los tres lados.")
else:
    print("Figura no válida.")

print("Área:", area)
print("Perímetro:", perimetro)