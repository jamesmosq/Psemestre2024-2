def bubble_sort_palabras(lista):
    n = len(lista)  # Obtener la longitud de la lista

    # Bucle que controla el número de pasadas
    for i in range(n):
        intercambio = False  # Bandera para detectar si hubo algún intercambio

        # Bucle interno que realiza las comparaciones de palabras adyacentes
        for j in range(n - i - 1):
            # Comparar palabras adyacentes alfabéticamente
            if lista[j] > lista[j + 1]:
                # Si están en el orden incorrecto, se intercambian
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True

        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambio:
            break


# Lista de palabras de ejemplo para ordenar
lista_palabras = ['yuca','zapote', 'banana', 'pera', 'naranja', 'uva','coco','durazno','sandia']

# Llamar a la función bubble_sort_palabras
bubble_sort_palabras(lista_palabras)

# Mostrar la lista ordenada
print("Lista de palabras ordenada:", lista_palabras)
