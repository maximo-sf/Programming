# act02_menu.py

print("1) Disk  2) Users  3) Ping  q) Quit")
option = input("> ").strip().lower()

match option:
    case "1":
        used = int(input("Used %: "))
        if used > 90:
            print("CRITICAL: Disk usage is over 90%")
        elif used > 80:
            print("WARNING: Disk usage is over 80%")
        else:
            print("OK: Disk usage is normal")

    case "2":
        print("Active users: admin, user1, guest")

    case "3":
        ip = input("Enter IP: ").strip()
        parts = ip.split(".")
        if len(parts) == 4:
            print(f"Pinging {ip}... Success!")
        else:
            print("Error: Invalid IP address. It must have 4 parts.")

    case "q":
        print("Goodbye!")

    case _:
        print("Unknown option")

# act02_menu_if.py

print("1) Disk  2) Users  3) Ping  q) Quit")
option = input("> ").strip().lower()

if option == "1":
    used = int(input("Used %: "))
    if used > 90:
        print("CRITICAL: Disk usage is over 90%")
    elif used > 80:
        print("WARNING: Disk usage is over 80%")
    else:
        print("OK: Disk usage is normal")

elif option == "2":
    print("Active users: admin, user1, guest")

elif option == "3":
    ip = input("Enter IP: ").strip()
    parts = ip.split(".")
    if len(parts) == 4:
        print(f"Pinging {ip}... Success!")
    else:
        print("Error: Invalid IP address. It must have 4 parts.")

elif option == "q":
    print("Goodbye!")

else:
    print("Unknown option")