n = int(input("n: "))
while n >= 0:
    end = ", " if n > 0 else "\n"
    print(n, end=end)
    n -= 1

# ----------------------------------------------------------------------

suma = 0
contador = 0

while True:
    num = float(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"Suma: {suma}")
    print(f"Media: {media}")
else:
    print("No se introdujeron números para calcular la media.")

# ----------------------------------------------------------------------

n = int(input("Introduce un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# ------------------------------

puerto = int(input("Introduce un puerto (1-65535): "))

while puerto < 1 or puerto > 65535:
    print("Puerto inválido. Debe estar entre 1 y 65535.")
    puerto = int(input("Introduce un puerto (1-65535): "))

print(f"Puerto válido registrado: {puerto}")