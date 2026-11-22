numbers = []

while True:
    user_input = input("Enter an integer (or 'end' to finish): ").strip()

    if user_input.lower() == "end":
        break

    try:
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        print("Warning: Invalid input. Please enter an integer or 'end'.")

if numbers:
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))
else:
    print("No valid integers were entered.")
