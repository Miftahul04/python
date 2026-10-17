correct_password = "python123"
password= ""
attempts = 0
while password != correct_password:
    password = input("Enter the password:")
    attempts += 1
    if password != correct_password:
        print("Incorrect password! Keep trying")
print("Access granted")
print("Attempts:",attempts)