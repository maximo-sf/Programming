USER, PASSWORD = "admin", "asir2026"
MAX_TRIES = 3
tries = 0

while tries < MAX_TRIES:
    user = input("User: ")
    pwd = input("Password: ")

    if user == "" or pwd == "":
        print("Empty input ignored")
        continue

    tries += 1

    if user == USER and pwd == PASSWORD:
        print("Access granted")
        break
    else:
        print("Wrong credentials. Attempts left:", MAX_TRIES - tries)
else:
    print("Account locked")