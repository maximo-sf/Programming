# Manejo de fecha
fecha_input = input("Date: ")
partes_fecha = fecha_input.split("/")
dia = partes_fecha[0].zfill(2)
mes = partes_fecha[1].zfill(2)
anio = partes_fecha[2]

print(f"Date: {dia}/{mes}/{anio}")

# Datos del producto
producto = input("Product: ")
precio_unidad = float(input("Unit price: "))
cantidad = int(input("Quantity: "))

# Cálculo de euros y céntimos
euros = int(precio_unidad)
centimos = round((precio_unidad - euros) * 100)

total = precio_unidad * cantidad

print(f"Euros: {euros} Cents: {centimos}")
print(f"{producto}")

# Formato especificando ancho total (ej: 6 enteros + 1 punto + 2 decimales = 09.2f)
precio_fmt = f"{precio_unidad:09.2f}"
cant_fmt = f"{cantidad:03d}"
total_fmt = f"{total:011.2f}"

print(f"{precio_fmt} {cant_fmt} {total_fmt}")