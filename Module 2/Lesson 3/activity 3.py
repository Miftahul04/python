start = 2
end = 10

for number in range(start,end+1):
    print("Factors of ",number)
    for divisor in range(1,number+2):
        if number%divisor == 0:
            print(divisor,end=" ")
    print()