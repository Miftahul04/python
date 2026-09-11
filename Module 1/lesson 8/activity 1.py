student_marks = float(input("Enter your marks (out of 100)"))
if student_marks >= 90:
    grade = "A"
elif student_marks >= 75:
    grade = "B"
elif student_marks >= 50:
    grade = "C"
else: 
    grade = "F"

print(f"Grade: {grade}")