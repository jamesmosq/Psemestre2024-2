class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
class Impresora:
    def __init__(self):
        self.cola_impresion = Cola()

    def agregar_documento(self, documento):
        self.cola_impresion.enqueue(documento)
        print(f"Documento '{documento}' agregado a la cola")

    def imprimir(self):
        if not self.cola_impresion.is_empty():
            doc = self.cola_impresion.dequeue()
            print(f"Imprimiendo: {doc}")
        else:
            print("No hay documentos en cola")


# Uso
impresora = Impresora()
impresora.agregar_documento("Tesis.pdf")
impresora.agregar_documento("CV.doc")
impresora.imprimir()  # Imprime: Tesis.pdf
impresora.imprimir()  # Imprime: CV.doc