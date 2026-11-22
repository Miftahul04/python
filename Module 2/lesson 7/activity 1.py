correct_password = "python123"
attempts = int(input("How many attempts do you want? ->"))
for attempt in range(1,attempts+1):
    password = input("Enter the password")
    if password == correct_password:
        print("Access granted")
        break
    print("Incorrect password. Try again")

print("Program finished")