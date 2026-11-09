fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

# Posición de las barras '/'
primera_barra = fecha.find('/')
segunda_barra = fecha.rfind('/')

# Extraer las partes usando slicing
dia = fecha[0:primera_barra]
mes = fecha[primera_barra + 1:segunda_barra]
anio = fecha[segunda_barra + 1:]

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")