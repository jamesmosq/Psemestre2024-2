"""
Evalúa si al menos una de estas condiciones es verdadera:
'a' es igual a 'b', 'c' es igual a 'd', o 'a' más 'd' es igual a
'b' más 'c':"""
a, b, c, d = 4, 5, 9, 7
resultado = (a == b) or (c == d) and (a + d == b + c)
print(resultado)  # False