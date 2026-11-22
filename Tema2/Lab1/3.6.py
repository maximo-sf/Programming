cpu_usage = float(input("Enter CPU usage percentage (0-100): "))

if not (0 <= cpu_usage <= 100):
    raise ValueError("CPU usage percentage must be between 0 and 100.")

print(f"CPU usage recorded: {cpu_usage}%")
