MIN_LENGTH = 10
password = input("Password: ")
while len(password) < MIN_LENGTH:
    print("Invalid length.")
    password = input("Password: ")
print("*" * len(password))
