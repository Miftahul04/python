drink = input("Coffee or tea").lower()
if drink == "coffee":
    size = input("Size (S/M/L)").upper()
    if size == "S":
        print("You chose small size. Your total is 250 bdt.")
    elif size == "M":
        print("You chose medium size. Your total is 320 tk.")
    else:
        print("You chose large size. Your total is 400 tk.")
elif drink == "tea":
    sugar = int(input("Sugar level (0-2)"))
    if sugar == 0:
        print("You chose zero sugar for your tea.")
    elif sugar == 1:
        print("You chose level 1 sugar for your tea.")
    else:
        print("You chose level 2 sugar for your tea.")
else:
    print("Invalid input")