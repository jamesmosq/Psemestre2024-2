#4 APLICACIONES PRÁCTICAS:
# 1. Invertir una cadena
def invertir_cadena(texto):
    pila = Pila()
    # Añadir cada carácter a la pila
    for char in texto:
        pila.push(char)

    # Reconstruir la cadena invertida
    texto_invertido = ""
    while not pila.is_empty():
        texto_invertido += pila.pop()

    return texto_invertido


# 2. Verificar palíndromos
def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == invertir_cadena(texto)


# 3. Convertir número decimal a cualquier base
def convertir_base(decimal, base):
    pila = Pila()
    digitos = "0123456789ABCDEF"

    while decimal > 0:
        pila.push(digitos[decimal % base])
        decimal //= base

    resultado = ""
    while not pila.is_empty():
        resultado += pila.pop()

    return resultado


# 4. Evaluar expresiones postfijas
def evaluar_postfija(expresion):
    pila = Pila()
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    for token in expresion.split():
        if token in operadores:
            b = float(pila.pop())
            a = float(pila.pop())
            resultado = operadores[token](a, b)
            pila.push(str(resultado))
        else:
            pila.push(token)

    return float(pila.pop())