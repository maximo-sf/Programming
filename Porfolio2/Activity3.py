n = int(input("Introduce un número: "))

while n >= 0:
    print(n, end=", ")
    n = n - 1
print()

# ----------------------------------------------------------------------

suma = 0
contador = 0
num = float(input("Introduce un número (0 para terminar): "))

while num != 0:
    suma = suma + num
    contador = contador + 1
    num = float(input("Introduce otro número (0 para terminar): "))

if contador > 0:
    media = suma / contador
    print("Suma:", suma)
    print("Media:", media)
else:
    print("No has introducido ningún número.")

# ----------------------------------------------------------------------

n = int(input("Introduce un número para su tabla: "))

for i in range(1, 11):
    resultado = n * i
    print(n, "x", i, "=", resultado)

# ----------------------------------------------------------------------

puerto = int(input("Introduce un puerto (1 a 65535): "))

while puerto < 1 or puerto > 65535:
    print("Error: Puerto no válido.")
    puerto = int(input("Prueba de nuevo (1 a 65535): "))

print("¡Puerto correcto! Has elegido:", puerto)