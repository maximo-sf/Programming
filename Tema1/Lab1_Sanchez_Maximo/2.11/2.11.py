nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

total = precio * cantidad

print(f"{nombre}: Precio = {precio:09.2f}, Cantidad = {cantidad:03d}, Total = {total:011.2f}")