#3.OPERACIONES ADICIONALES:
class PilaAvanzada(Pila):
    # 7. DUPLICAR el último elemento
    def duplicate_top(self):
        if not self.is_empty():
            self.push(self.peek())

    # 8. INTERCAMBIAR los dos últimos elementos
    def swap(self):
        if self.size() >= 2:
            item1 = self.pop()
            item2 = self.pop()
            self.push(item1)
            self.push(item2)

    # 9. ROTAR elementos (n posiciones)
    def rotate(self, n):
        if self.size() > 1 and n > 0:
            temp = self.items[-n:] + self.items[:-n]
            self.items = temp

    # 10. BUSCAR un elemento
    def search(self, item):
        return item in self.items

    # 11. CONTAR ocurrencias de un elemento
    def count(self, item):
        return self.items.count(item)