def request_pin():
    pin = ""

    while pin != "1234":
        pin = input("Please enter your pin: ")

        if pin == "1234":
            print("authetnicated")
        else:
            print("not authenticated\n")

def withdraw():
    pass

def deposit():
    pass

def exit():
    pass

print("Welcome to the atm.")

request_pin()