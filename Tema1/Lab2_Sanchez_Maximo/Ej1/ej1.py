segundos_totales = int(input("Seconds: "))

# Calculamos días, horas, minutos y segundos restantes
dias = segundos_totales // (24 * 3600)
resto = segundos_totales % (24 * 3600)

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60

print(
    f"{segundos_totales} seconds are {dias} days, {horas} hours, {minutos} minutes and {segundos} seconds"
)