last_score = float(input("Enter the last score ->"))
current_score = float(input("Enter the current score ->"))
perfect_attendance = input("Perfect attendance ? (yes/no)").lower()=="yes"

if current_score >= 90:
    grade = "A"
elif current_score >= 80:
    grade = "B"
elif current_score >= 70:
    grade = "C"
elif current_score >= 60:
    grade = "D"
else:
    grade = "F"

if current_score and perfect_attendance:
    print("Bonus 5% mark for perfect attendance.")
elif current_score > last_score:
    print("Improved! Keep it up.")

if current_score - last_score > 50 and last_score < 60:
    print("Warning! Unusual score jump. Review for cheating.")

print(f"Grade = {grade}")