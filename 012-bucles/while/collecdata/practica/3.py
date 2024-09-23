# Ejemplo: Buscar un elemento en una tupla
colores = ('rojo', 'verde', 'azul', 'amarillo')
buscar = 'azul'
indice = 0

while indice < len(colores):
    if colores[indice] == buscar:
        print(f"Encontrado '{buscar}' en el índice {indice}")
        break
    indice += 1
else:
    print(f"'{buscar}' no encontrado en la tupla")