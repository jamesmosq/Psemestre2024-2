#Crear un diccionario usando enumerate
letras = ['a', 'b', 'c', 'd']
dicc_letras = {indice: letra for indice, letra in enumerate(letras)}
print(dicc_letras)  # {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

