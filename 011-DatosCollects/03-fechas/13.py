from datetime import datetime
import locale
# Cambiar el idioma a español
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

# Obtener la fecha y hora actual
fecha = datetime.now()

# Obtener el nombre del día
nombre_dia = fecha.strftime("%A")

# Mostrar el nombre del día
print("Nombre del día:", nombre_dia)
