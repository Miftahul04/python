age = int(input("Enter your age ->"))
birth_year = 2026 - age

hobby = str(input("Enter your hobby ->")).upper()

name = str(input("Enter your name ->"))
print(f"The year you were born {birth_year}.")

print("Your hobby is ", hobby)

print(name[::-1])