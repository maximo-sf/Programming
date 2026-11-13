# 1. Right triangle of asterisks
height = int(input("Height: "))

for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()

print()

# 2. Upside-down right triangle
for i in range(height, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()

# 3. Full multiplication table 1-10 aligned with f-strings
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

print()

# 4. Extension: Hollow square of side n
n = int(input("Square side n: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()