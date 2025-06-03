principle = 0
time =0
rate = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be 0 or negative")

while time <= 0:
    time = int(input("Enter the time: "))
    if principle <= 0:
        print("Time cannot be 0 or negative")

while rate <= 0:
    rate = float(input("Enter the Interest rate: "))
    if rate <= 0:
        print("Interest cannot be 0 or negative")

total = principle * pow((1 + rate/100),time)

print(f"Your total will be {total} after {time}years")