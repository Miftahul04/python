rows = 5

for i in range(1,rows+1):
    for space in range(rows-i):
        print(" ", end = "")
    for col in range(1,2*i):
        print(col , end = "")
    print()