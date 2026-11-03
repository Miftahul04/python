rows = int(input("Enter the number of rows:"))
for rows in range(1,rows+1):
    for star in range(rows):
        print("*", end = "")
    print()