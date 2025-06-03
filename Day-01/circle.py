import math
radius = float(input("Enter the radius: "))

#Area of a circle
Area = math.pi * pow(radius,2)
print(f"Area of the circle is: {round(Area,2)}")

#CIrcumference of the Circle
Circumference = 2 * math.pi * radius
print(f"Circumference of the circle is: {round(Circumference,2)}")