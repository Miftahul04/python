total_bill = float(input("Enter your total bill"))
if total_bill > 500:
    discount = total_bill*0.20
elif total_bill > 300:
    discount = total_bill * 0.10
else:
    discount = 0
final_bill = total_bill - discount
print(f"Original Bill {total_bill}")
print(f"Discount Applied {discount}")
print(f"Final Bill {final_bill}") 