def busqueda_lineal_palabras(lista_palabras, palabra_objetivo):
    # Recorre la lista de palabras
    for i in range(len(lista_palabras)):
        # Si encuentra la palabra objetivo, retorna el índice
        if lista_palabras[i] == palabra_objetivo:
            return i
    # Si no se encuentra la palabra objetivo, retorna -1
    return -1

# Lista de palabras de ejemplo
lista_palabras = ['manzana', 'banano', 'pera', 'naranja', 'uva','piña','sal','banano']

# Palabra que queremos buscar
palabra_objetivo = 'banano'

# Llamar a la función de búsqueda lineal
resultado = busqueda_lineal_palabras(lista_palabras, palabra_objetivo)

# Mostrar el resultado
if resultado != -1:
    print(f"La palabra '{palabra_objetivo}' se encuentra en la posición {resultado}.")
else:
    print(f"La palabra '{palabra_objetivo}' no se encuentra en la lista.")
