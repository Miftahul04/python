even_count = 0
odd_count = 0

for i in range(1,11):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)

for number in range(1,31):
    if number % 3 == 0:
        print("Divisible by 3", number)
    elif number % 5 == 0:
        print("Divisible by 5:", number)