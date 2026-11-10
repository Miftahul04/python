numbers = [123,456,789,120]

for number in numbers:
    temp = number
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp = temp // 10
    print(f"{number} -> digit sum = {digit_sum}")