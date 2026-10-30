age = int(input("Enter your age ->"))

if age >= 18:
    destination = input("Where do you want to travel? ->")
    passport = input("Do you have a valid passport? (yes/no)")
else:
    print("You are too young for this trip.")

if passport == "yes":
    visa = input("Do you have a valid visa for your destination country? (yes/no)")
else:
    print("Your trip can't be conducted because you don't have a valid passport.")

if visa == "yes":
    estimated_budget = int(input("What is the estimated budget? ->"))
    total_budget = int(input("What is your total budget? ->"))
else:
    print("You do not have a valid visa.")

if total_budget >= estimated_budget:
    print("You are ready for the trip.")
else:
    print("Your budget is lower than the estimated budget.")