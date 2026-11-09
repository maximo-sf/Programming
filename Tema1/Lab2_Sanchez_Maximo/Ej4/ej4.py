nombre_completo = input("Full name: ")

# Limpiamos espacios iniciales/finales
nombre_clean = nombre_completo.strip()

# Convertimos a mayúsculas
nombre_mayus = nombre_clean.upper()

# Contamos letras eliminando los espacios
num_letras = len(nombre_clean.replace(" ", ""))

# Extraemos las palabras
partes = nombre_clean.split()
primer_nombre = partes[0]
primer_apellido = partes[1]

# Generamos el nombre de usuario
username = (primer_nombre[0] + primer_apellido).lower()

print(f"{nombre_mayus} has {num_letras} letters")
print(f"Username: {username}")