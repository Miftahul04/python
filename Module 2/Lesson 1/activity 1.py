subjects = int(input("How many subjects do you have ? ->"))
total_marks = 0

for number in range(subjects):
    marks = float(input(f"Enter marks for subject {number + 1}:"))
    total_marks = total_marks + marks

print("Total marks:", total_marks)