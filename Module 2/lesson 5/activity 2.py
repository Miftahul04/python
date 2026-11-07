size = 5
for row in range(size):
    for col in range(size):
        if (row+col) %2 == 0:
            print("0", end = "") #black square
        else:
            print("X",end= "")
    print() #new line after each row