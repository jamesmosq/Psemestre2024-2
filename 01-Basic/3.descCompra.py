precio_original = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

descuento_cantidad = precio_original * (descuento / 100)
precio_final = precio_original - descuento_cantidad

print("El descuento es de:", descuento_cantidad)
print("El precio final es:", precio_final)