#Iterar sobre un diccionario mientras cumple una condición
inventario = {'manzanas': 5, 'bananas': 2, 'naranjas': 8, 'peras': 3}
frutas_a_vender = []

while inventario and max(inventario.values()) > 3:
    fruta = max(inventario, key=inventario.get)
    frutas_a_vender.append(fruta)
    del inventario[fruta]

print("Frutas a vender:", frutas_a_vender)
print("Inventario restante:", inventario)

