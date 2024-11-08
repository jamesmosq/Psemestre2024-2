import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexión establecida correctamente.")
        except mysql.connector.Error as error:
            print("Error de conexión:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada correctamente.")

    def execute_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)

class Employee:
    def __init__(self, last_name, first_name, birth_date, photo, notes):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.photo = photo
        self.notes = notes

    def save_to_db(self, db_manager):
        insert_query = """INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes)
                          VALUES (%s, %s, %s, %s, %s)"""
        employee_data = (self.last_name, self.first_name, self.birth_date, self.photo, self.notes)
        db_manager.execute_query(insert_query, employee_data)
        print("Nuevo empleado insertado correctamente.")

# Configuración de la conexión
user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'

db_manager = DatabaseManager(host, user, password, database)

last_name = 'AMosquera'
first_name = 'APJmes'
birth_date = '1990-01-01'
photo = 'jaes-MR.jpg'
notes = 'New employee'

employee = Employee(last_name, first_name, birth_date, photo, notes)
try:
    db_manager.connect()

    employee.save_to_db(db_manager)

except Exception as e:
    print("Error inesperado:", e)
finally:
    db_manager.disconnect()
