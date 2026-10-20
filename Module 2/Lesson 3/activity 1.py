text = "programming"

for character in text:
    count = 0
    for letter in text:
        if character == letter:
            count += 1
    print(f"{character} appears {count} times")