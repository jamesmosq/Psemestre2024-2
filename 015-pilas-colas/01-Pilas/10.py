#6 VERIFICACIONES DE PILA:
def verificar_balance(expresion):
    pila = Pila()
    apertura = "({["
    cierre = ")}]"
    pares = dict(zip(cierre, apertura))

    for char in expresion:
        if char in apertura:
            pila.push(char)
        elif char in cierre:
            if pila.is_empty():
                return False
            if pila.pop() != pares[char]:
                return False

    return pila.is_empty()


# Ejemplo de uso
print(verificar_balance("{[()]}"))  # True
print(verificar_balance("{[(])}"))  # False