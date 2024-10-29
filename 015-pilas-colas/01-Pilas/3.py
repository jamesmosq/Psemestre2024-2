"""
Navegación de Páginas Web (Historial de Navegación)
En navegadores web, el historial de páginas vistas se puede manejar
con una pila para la función de “Atrás” y otra para la función de “Adelante”.
"""
class Navegador:
    def __init__(self):
        self.historial_atras = []
        self.historial_adelante = []
        self.pagina_actual = None

    def visitar_pagina(self, url):
        if self.pagina_actual:
            self.historial_atras.append(self.pagina_actual)
        self.pagina_actual = url
        self.historial_adelante.clear()  # Limpiar el historial adelante cuando se visita una nueva página

    def ir_atras(self):
        if self.historial_atras:
            self.historial_adelante.append(self.pagina_actual)
            self.pagina_actual = self.historial_atras.pop()

    def ir_adelante(self):
        if self.historial_adelante:
            self.historial_atras.append(self.pagina_actual)
            self.pagina_actual = self.historial_adelante.pop()

# Paso a paso
navegador = Navegador()
navegador.visitar_pagina("google.com")
navegador.visitar_pagina("facebook.com")
navegador.visitar_pagina("python.org")

print(navegador.pagina_actual)  # Salida: "python.org"
navegador.ir_atras()

print(navegador.pagina_actual)  # Salida: "openai.com"
navegador.ir_adelante()
print(navegador.pagina_actual)  # Salida: "python.org"
