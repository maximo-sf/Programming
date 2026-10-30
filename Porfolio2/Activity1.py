# act01_selection.py 
# Tareas 1 y 2: Mark Calculator

try:
    mark = float(input("Enter a mark (0-10): "))

    if mark < 0 or mark > 10:
        print("Error: Mark must be between 0 and 10.")
    elif mark < 5:
        print("Grade: Fail")
    elif mark < 7:
        print("Grade: Pass")
    elif mark < 9:
        print("Grade: Remarkable")
    elif mark < 10:
        print("Grade: Outstanding")
    else: 
        print("Grade: Excellent with honors")

except ValueError:
    print("Error: Please enter a valid number.")

# Tareas 3 y 4: Leap Year

year = int(input("Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")