total = 0
count = 0
for i in range(1,51):
    if i % 5 == 0:
        count += 1
        total += i
print("Count:", count)
print("Total:", total)