try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("That is not a valid number")
