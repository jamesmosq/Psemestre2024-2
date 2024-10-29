def deci_a_bin(decimal):
    pila = []
    while decimal > 0:
        pila.append(decimal % 2)
        decimal //= 2

    binario = ""
    while pila:
        binario += str(pila.pop())
    return binario

print(deci_a_bin(90))
