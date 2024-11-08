class Person:
    def __init__(self, name, age, email,phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

        def saludar(nombre):
            print("Hola, " + nombre)

        # Llamando a la función
        saludar("Juan")


p1 = Person("John", 36, "John@example.com", "6564541")
p2 = Person("Ana", 10, "Ana@example.com", "965476514")

print(p1.name, p1.age, p1.email, p1.phone)
print(p2.name, p2.age)
# print(p1.age)
