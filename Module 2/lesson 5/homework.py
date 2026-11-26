rows = int(input("Enter the number of shelves:"))
coloumns = int(input("Ënter the number of sections:"))
print("LIBRARY SHELF ORGANISER")
print("-----------------------")
for i in range(1,rows+1):
    for j in range(1,coloumns+1):
        print(f"Shelf{i}: Section {j}")
    print()