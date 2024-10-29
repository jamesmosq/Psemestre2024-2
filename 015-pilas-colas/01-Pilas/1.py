class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Ejemplo
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(5)
pila.push(1)

print(pila.pop())  # Imprime: el ultimo en hacerle pop