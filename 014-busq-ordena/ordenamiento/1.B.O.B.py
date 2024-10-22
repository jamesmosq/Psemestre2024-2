def bubble_sort(lista):
    n = len(lista)  # Obtener la longitud de la lista

    # Bucle que controla el número de pasadas
    for i in range(n):
        # Bandera para detectar si hubo algún intercambio en esta pasada
        intercambio = False

        # Bucle interno que realiza las comparaciones de pares adyacentes
        # Recorre la lista hasta la posición (n - i - 1) porque los últimos i elementos ya estarán ordenados
        for j in range(n - i - 1):
            # Comparar elementos adyacentes
            if lista[j] > lista[j + 1]:
                # Si están en el orden incorrecto, se intercambian
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # Cambiar la bandera para indicar que hubo un intercambio
                intercambio = True

        # Si no hubo intercambios en esta pasada, la lista ya está ordenada y se puede detener el algoritmo
        if not intercambio:
            break


# Lista de ejemplo para ordenar
lista = [64, 34, 25, 12, 22, 11, 90,8]

# Llamar a la función bubble_sort
bubble_sort(lista)

# Mostrar la lista ordenada
print("Lista ordenada:", lista)
