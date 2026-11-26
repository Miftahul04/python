rows = int(input("Enter the number of rows:"))
for i in range(rows):
    for j in range(5 - i):
        print(" ",end="")
        for k in range(i):
            print("*",end="")

    print()
for l in range(rows - 1,0,-1):
    for m in range(l):
        print("*", end="")

    print()