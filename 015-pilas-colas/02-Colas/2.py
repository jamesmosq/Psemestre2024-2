class Cola:
    def __init__(self):
        """Inicializa una cola vacía"""
        self.items = []

    def enqueue(self, item):
        """
        Añade un elemento al final de la cola
        Args:
            item: Elemento a añadir
        """
        self.items.append(item)

    def dequeue(self):
        """
        Elimina y retorna el elemento del frente de la cola
        Returns:
            El elemento eliminado
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.is_empty():
            raise IndexError("No se puede hacer dequeue de una cola vacía")
        return self.items.pop(0)

    def front(self):
        """
        Muestra el elemento del frente sin eliminarlo
        Returns:
            El elemento del frente
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items[0]

    def rear(self):
        """
        Muestra el último elemento sin eliminarlo
        Returns:
            El último elemento
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items[-1]

    def is_empty(self):
        """
        Verifica si la cola está vacía
        Returns:
            True si está vacía, False si no
        """
        return len(self.items) == 0

    def size(self):
        """
        Retorna el número de elementos en la cola
        Returns:
            int: Número de elementos
        """
        return len(self.items)

    def clear(self):
        """Elimina todos los elementos de la cola"""
        self.items = []


# Ejemplo de uso
def main():
    # Crear cola
    cola = Cola()

    # Enqueue - Añadir elementos
    cola.enqueue("Primero")
    cola.enqueue("Segundo")
    cola.enqueue("Tercero")
    print("Cola después de enqueue:", cola.items)  # ['Primero', 'Segundo', 'Tercero']

    # Dequeue - Eliminar primer elemento
    elemento = cola.dequeue()
    print("Elemento eliminado:", elemento)  # Primero
    print("Cola después de dequeue:", cola.items)  # ['Segundo', 'Tercero']

    # Front - Ver primer elemento
    primero = cola.front()
    print("Primer elemento:", primero)  # Segundo

    # Rear - Ver último elemento
    ultimo = cola.rear()
    print("Último elemento:", ultimo)  # Tercero

    # Verificar si está vacía
    print("¿Está vacía?", cola.is_empty())  # False

    # Tamaño de la cola
    print("Tamaño:", cola.size())  # 2

    # Limpiar cola
    cola.clear()
    print("Cola después de clear:", cola.items)  # []

    # Manejo de errores
    try:
        cola.dequeue()
    except IndexError as e:
        print("Error:", e)  # Error: No se puede hacer dequeue de una cola vacía


if __name__ == "__main__":
    main()
