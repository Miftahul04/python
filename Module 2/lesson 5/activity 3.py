days_in_month = 30
start_day= 1 # 1 = monday 7 = sunday
print("Mon Tue Wed Thu Fri Sat Sun")

# print spaces for the first week
for i in range(1, start_day):
    print("    ", end = "")

#print each day
for day in range(1, days_in_month + 1):
    print(f"{day:2}", end = "  ")
    if (day + start_day - 1) %7 == 0:
        print()