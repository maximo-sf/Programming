telefono = input("Introduce el número de teléfono (+34-123456789):")

partes = telefono.split("-")
numero = partes[1]

print(f"El número es: {numero}")