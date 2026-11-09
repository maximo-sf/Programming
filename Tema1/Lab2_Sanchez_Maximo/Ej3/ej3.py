n = int(input("n: "))

# Suma de 1 a n y suma de cuadrados (división entera con //)
suma = n * (n + 1) // 2
suma_cuadrados = n * (n + 1) * (2 * n + 1) // 6

print(f"Sum: {suma}")
print(f"Sum of squares: {suma_cuadrados}")

peso = float(input("Weight (kg): "))
altura = float(input("Height (m): "))

bmi = peso / (altura**2)

print(f"Your Body Mass Index is {bmi:.2f}")