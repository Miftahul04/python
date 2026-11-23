secret_number = 78
attempts = 3
print("You have 3 attempts to guess the number.")

for attempt in range(attempts):
    number = int(input("Enter your guess:"))
    attempts-=1
    if number == secret_number:
        print("You have guessed the number correctly.")
        break
    else:
        print("It is incorrect. Try again ->")
    
    if attempts == 0:
        print("You are out of attempts.")
        break