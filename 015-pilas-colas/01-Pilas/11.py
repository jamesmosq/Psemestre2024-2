class Pila:
    def __init__(self):
        """Inicializa una pila vacía"""
        self.items = []

    def push(self, item):
        """
        Añade un elemento a la pila
        Args:
            item: Elemento a añadir
        """
        self.items.append(item)

    def pop(self):
        """
        Elimina y retorna el elemento superior de la pila
        Returns:
            El elemento eliminado
        Raises:
            IndexError: Si la pila está vacía
        """
        if self.is_empty():
            raise IndexError("No se puede hacer pop de una pila vacía")
        return self.items.pop()

    def peek(self):
        """
        Muestra el elemento superior sin eliminarlo
        Returns:
            El elemento superior
        Raises:
            IndexError: Si la pila está vacía
        """
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.items[-1]

    def is_empty(self):
        """
        Verifica si la pila está vacía
        Returns:
            True si está vacía, False si no
        """
        return len(self.items) == 0

    def size(self):
        """
        Retorna el número de elementos en la pila
        Returns:
            int: Número de elementos
        """
        return len(self.items)

    def clear(self):
        """Elimina todos los elementos de la pila"""
        self.items = []


# Ejemplo de uso
def main():
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

    # Manejo de errores
    try:
        pila.pop()
    except IndexError as e:
        print("Error:", e)  # Error: No se puede hacer pop de una pila vacía


if __name__ == "__main__":
    main()