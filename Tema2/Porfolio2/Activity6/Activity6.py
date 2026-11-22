import math

operations = 0

while True:
    op = input("Operation (+ - * / q): ").strip()

    if op == "q":
        print(f"Total operations completed: {operations}")
        break

    if op not in ("+", "-", "*", "/"):
        print(f"Unknown operation '{op}'. Please choose +, -, *, /, or q.")
        continue

    try:
        a = float(input("a: ").strip())
        b = float(input("b: ").strip())

        if math.isinf(a) or math.isinf(b):
            raise OverflowError("Number is too large (infinity).")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b

        if math.isinf(result) or math.isnan(result):
            raise OverflowError("Result overflowed or is undefined (NaN).")

    except ValueError:
        print("Invalid number input. Please enter numeric values (no letters or empty input).")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero divisor.")
    except OverflowError as e:
        print(f"Numeric limit exceeded: {e}")
    else:
        print(f"Result: {result}")
    finally:
        operations += 1
        print(f"Operations attempted so far: {operations}")
