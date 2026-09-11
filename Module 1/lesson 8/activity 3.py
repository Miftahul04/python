score = 0

q1 = input("Q1: What is the capital of France? -> ").lower()
if q1 == "paris":
    score += 1
q2 = input("Q2: What is 5+7? -> ").lower()
if q2 == "12":
    score += 1
q3 = input("Q3: Which programming language are we using now? -> ").lower()
if q3 == "python":
    score +=1
print(f"Your total score {score}/3")
