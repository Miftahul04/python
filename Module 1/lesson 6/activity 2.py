weather = input("Is it sunny,rainy or cold ?")
temp = int(input("Enter the temperature"))
if weather == "sunny" and temp > 25:
    print("Wear sunscreen!")
elif weather == "rainy" or temp < 10:
    print("Bring an umbrella")
else:
    print("Enjoy the day")
