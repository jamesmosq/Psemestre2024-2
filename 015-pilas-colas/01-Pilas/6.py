#2.EJEMPLOS DE USO:
# Crear pila
pila = Pila()

# Push - Añadir elementos
pila.push(1)
pila.push(2)
pila.push(3)
print("Pila después de push:", pila.items)  # [1, 2, 3]

# Pop - Eliminar último elemento
elemento = pila.pop()
print("Elemento eliminado:", elemento)  # 3
print("Pila después de pop:", pila.items)  # [1, 2]

# Peek - Ver último elemento
ultimo = pila.peek()
print("Último elemento:", ultimo)  # 2

# Verificar si está vacía
print("¿Está vacía?", pila.is_empty())  # False

# Tamaño de la pila
print("Tamaño:", pila.size())  # 2

# Limpiar pila
pila.clear()
print("Pila después de clear:", pila.items)  # []