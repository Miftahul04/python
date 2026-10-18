PIN = "1234"
attempts = 3
pin = ""
while pin != PIN:
    pin = input("Enter the PIN")
    attempts == attempts - 1
    print("Incorrect PIN. Try again")

while attempts == 0:
     print("Acess denied")
print("Acess granted") 