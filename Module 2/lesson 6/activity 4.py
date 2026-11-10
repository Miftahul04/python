for number in range(20,50):
    divisor_count = 0
    for divisor in range(1,number+1):
        if number % divisor == 0:
            divisor_count += 1
    if divisor_count == 2:
        print(number)