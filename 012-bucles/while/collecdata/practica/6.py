#Buscar un valor en un diccionario
precios = {'manzana': 0.5, 'banana': 0.3, 'naranja': 0.4, 'pera': 0.6}
busc_precio = 9.0
encontrado = False

items = list(precios.items())
i = 0

while i < len(items) and not encontrado:
    fruta, precio = items[i]
    if precio == busc_precio:
        print(f"Encontrado: {fruta} cuesta: $ {precio}")
        encontrado = True
    i += 1

if not encontrado:
    print(f"No se encontró ninguna fruta que cueste: $ {busc_precio}")