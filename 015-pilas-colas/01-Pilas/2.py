"""
Deshacer y Rehacer Operaciones
Muchas aplicaciones, como procesadores de texto o editores de imágenes,
utilizan pilas para implementar las funcionalidades de "Deshacer" y "Rehacer".
"""
class Editor:
    def __init__(self):
        self.texto = ""
        self.historial_undo = []
        self.historial_redo = []

    def escribir(self, texto):
        self.historial_undo.append(self.texto)
        self.texto += texto

    def deshacer(self):
        if self.historial_undo:
            self.historial_redo.append(self.texto)
            self.texto = self.historial_undo.pop()

    def rehacer(self):
        if self.historial_redo:
            self.historial_undo.append(self.texto)
            self.texto = self.historial_redo.pop()

# Paso a paso
editor = Editor()
editor.escribir("Hola ")
editor.escribir("mundo")
editor.escribir(" Caminando")

print(editor.texto)  # Salida: "Hola mundo"
editor.deshacer()

print(editor.texto)  # Salida: "Hola "
editor.rehacer()

print(editor.texto)  # Salida: "Hola mundo"
editor.deshacer()
