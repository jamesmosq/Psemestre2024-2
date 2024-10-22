def busqueda_lineal(lista, objetivo):
    # Recorre la lista elemento por elemento
    for i in range(len(lista)):
        # Si encuentra el objetivo, retorna el índice
        if lista[i] == objetivo:
            return i
    # Si no se encuentra el objetivo, retorna -1
    return -1

# Lista de ejemplo
lista = [3, 5, 2, 7, 9, 1]

# Valor que queremos buscar
objetivo = 19

# Llamar a la función de búsqueda lineal
resultado = busqueda_lineal(lista, objetivo)

# Mostrar el resultado
if resultado != -1:
    print(f"El número {objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El número {objetivo} no se encuentra en la lista.")
