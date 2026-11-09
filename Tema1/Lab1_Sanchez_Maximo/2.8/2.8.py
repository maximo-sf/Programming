precio = input("Introduce el precio del producto en euros (ej. 15.99): ")

euros, centimos = precio.split(".")

print(f"Euros: {euros}")
print(f"Céntimos: {centimos}")