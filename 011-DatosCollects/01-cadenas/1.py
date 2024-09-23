lista = (1,78,6,6,89)
lista1 = (1,78,6,6,89)
"""for l in lista:
 print(l)"""

print(sum(lista+lista1))

tupla = (1,78,6,6,89)
tupla =list(tupla)
tupla.append(90900000)
print(tupla)

conj1 = {3, 4, 5, 6}
conj2 = {6, 7, 8, 9,11,3}
print(conj1.intersection(conj2))
n=conj2.difference(conj1)

"""for i in n:
    print(i)"""

diccionario = {"nombre": "Juan", "edad": 30}
print(diccionario["nombre"])