#Llenar una lista con números ingresados por el usuario:

numeros = []
while True:
    entrada = input("Ingrese un número (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")

print("Lista de números:", numeros)

#reto: Sumar los datos que sean ingresados al darle fin al ingreso de datos