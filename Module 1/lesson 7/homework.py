count = int(input("How many items did you buy? ->"))

for items in range(count):
    price = float(input("Enter the price of this item ->"))

if price >= 50:
    total_price = price*0.9

print("Total bill is", total_price)