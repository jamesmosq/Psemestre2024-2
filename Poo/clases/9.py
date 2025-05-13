class Person:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def saludar(self):
        """Imprime un saludo con el nombre de la persona."""
        print(f"Hola, mi nombre es {self.name}.")

    def tiene_telefono(self):
        """Devuelve True si la persona tiene un número de teléfono, False en caso contrario."""
        return bool(self.phone)

    def enviar_correo(self, mensaje):
        """Simula enviar un correo electrónico a la persona."""
        print(f"Enviando correo a {self.email} con el mensaje: '{mensaje}'")

    def cumplir_anios(self):
        """Incrementa la edad de la persona en 1."""
        self.age += 1
        print(f"¡Feliz cumpleaños, {self.name}! . años.")
    

# Crear instancias de la clase Person
p1 = Person("John", 36, "John@example.com", "")
p2 = Person("Ana", 10, "Ana@example.com", "965476514")
p3 = Person("Juana", 10, "juana@gmail.com", 4567890)
p4 = Person("JamesM", 10, "james@gmail.com", 4567812)
p5 = Person("James", 10, "james@gmail.com","65789876789")

# Usar los métodos de los objetos
p1.saludar()
p2.saludar()
p5.saludar()
if p1.tiene_telefono():
    print(f"{p1.name} tiene un número de teléfono.")
else:
    print(f"{p1.name} no tiene un número de teléfono registrado.")

if p2.tiene_telefono():
    print(f"{p2.name} tiene un número de teléfono.")
else:
    print(f"{p2.name} no tiene un número de teléfono registrado.")

p3.enviar_correo("¿Vamos por un helado?")

p2.cumplir_anios()
print(f"La nueva edad de {p2.name} es: {p2.age}")

p1.cumplir_anios()
p1.cumplir_anios()
print(f"La nueva edad de {p1.name} es: {p1.age}")

p4.cumplir_anios()
print(f"La nueva edad de {p4.name} es: {p4.age}")
