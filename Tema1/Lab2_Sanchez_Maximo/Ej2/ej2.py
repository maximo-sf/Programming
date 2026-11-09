GROWTH = 0.06

uso = float(input("Current usage (GB): "))

uso_m1 = uso * (1 + GROWTH)
uso_m2 = uso_m1 * (1 + GROWTH)
uso_m3 = uso_m2 * (1 + GROWTH)

print(f"Month 1: {uso_m1:.2f} GB")
print(f"Month 2: {uso_m2:.2f} GB")
print(f"Month 3: {uso_m3:.2f} GB")