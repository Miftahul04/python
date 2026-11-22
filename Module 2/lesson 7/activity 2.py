start_number = int(input("Enter the starting number:"))
end_number = int(input("Enter the ending number:"))

for i in range(start_number,end_number + 1):
    if i < 0:
        continue
    print(i)
