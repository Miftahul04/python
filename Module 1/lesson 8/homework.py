age = int(input("Enter your age -> "))
if age >= 18 > 21:
    print("You can vote but not drive yet")
elif age >= 21:
    print("You are eligible for both voting and driving.")
elif age >= 16 < 18:
    print("You can apply for a learner's license but can't vote")
else:
    print("Not eligible yet")
