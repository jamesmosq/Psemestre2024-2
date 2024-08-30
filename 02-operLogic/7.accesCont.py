edad = int(input("Ingrese su edad: "))
tiene_identificacion = input("¿Tiene identificación? (sí/no): ").lower() == "sí"
if edad >= 18 and tiene_identificacion:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")