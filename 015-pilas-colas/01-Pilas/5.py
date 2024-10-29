#1.OPERACIONES BÁSICAS:

class Pila:
    def __init__(self):
        self.items = []

    # 1. PUSH - Añadir elemento
    def push(self, item):
        self.items.append(item)

    # 2. POP - Eliminar y retornar el último elemento
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    # 3. PEEK/TOP - Ver el último elemento sin eliminarlo
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # 4. IS_EMPTY - Verificar si está vacía
    def is_empty(self):
        return len(self.items) == 0

    # 5. SIZE - Obtener tamaño
    def size(self):
        return len(self.items)

    # 6. CLEAR - Limpiar la pila
    def clear(self):
        self.items = []