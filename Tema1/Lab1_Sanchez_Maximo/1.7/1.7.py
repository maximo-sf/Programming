peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

bmi = peso / (altura ** 2)

print(f"Your Body Mass Index is {bmi:.2f}")