start_number = int(input("Enter the starting number:"))
end_number = int(input("Enter the ending number:"))
even_count = 0
odd_count = 0
sum_of_digits = 0
multiples_of_3_5 = 0
even_multiple_5 = 0

for i in range(start_number,end_number+1):
    if i % 2 == 0:
        even_count+=1
    else:
        odd_count+=1
        while i > 0:
            digit = i % 10
            sum_of_digits + digit
            i = i // 10
            if sum_of_digits % 3 == 0 and digit == 0 or 5:
                multiples_of_3_5+=1
            elif i % 2 == 0 and i % 5 == 0:
                even_multiple_5 +=1

print("Even count:", even_count)
print("Odd count:",odd_count)
print("Sum of the digits:", sum_of_digits)
print("Multiples of 3 and 5:",multiples_of_3_5)
print("Even multiples of 5:",even_multiple_5)