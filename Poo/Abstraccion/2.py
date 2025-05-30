from abc import ABC, abstractmethod


class Humano(ABC):
    """Clase abstracta que define la interfaz para un humano"""

    @abstractmethod
    def hablar(self):
        """Método abstracto que debe ser implementado por las subclases"""
        pass

    @abstractmethod
    def caminar(self):
        """Método abstracto que debe ser implementado por las subclases"""
        pass

    def mostrar_info(self):
        """Método concreto que puede ser usado por todas las subclases"""
        print(f"Humano: {self.__class__.__name__}")
        self.hablar()
        self.caminar()


class Estudiante(Humano):
    def hablar(self):
        print("Hola, soy un estudiante y estoy aprendiendo.")

    def caminar(self):
        print("Camino hacia la clase.")


Estudiante().mostrar_info()
