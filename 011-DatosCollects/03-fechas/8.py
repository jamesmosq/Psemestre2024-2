from datetime import datetime, date, time, timedelta

# Parsear una cadena a fecha
fecha_parseada = datetime.strptime("23/09/2023 14:30:00", "%d/%m/%Y %H:%M:%S")
print("Fecha parseada:", fecha_parseada)

