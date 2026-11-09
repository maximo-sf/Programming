deposito = float(input("Introduce la cantidad depositada: "))

interes = 0.04

year1 = deposito * (1 + interes)
year2 = year1 * (1 + interes)
year3 = year2 * (1 + interes)

print(f"Balance tras el primer año: {year1:.2f}")
print(f"Balance tras el segundo año: {year2:.2f}")
print(f"Balance tras el tercer año: {year3:.2f}")