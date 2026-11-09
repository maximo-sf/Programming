PASSWD = "Maxi"

user_input = input("Enter your password: ")

if user_input.lower() == PASSWD.lower():
    print("Access granted")
else:
    print("Wrong password")