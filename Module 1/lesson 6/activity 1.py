age = int(input("Enter your age"))
is_student = input("Are you a student (yes/no)").lower()
if age < 5:
    price = 0 #free ticket
elif is_student== "yes" or age <= 12:
  price = 8
else :
   price = 12
print(f"Your ticket price is {price}BDT")


