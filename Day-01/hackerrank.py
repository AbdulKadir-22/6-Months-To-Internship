# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

n = float(input("Enter the number(1-100): "))

if n % 2 == 0:
    even = n
    if 2<= even and even <= 5:
        print(f"Not Weird")
    elif 6<= even and even <=20 :
        print(f"Weird")
    elif 20 < even :
        print(f"Not Weird")
else:
    odd = n
    print("Weird")


# n = int(input())

# if n % 2 != 0:
#     print("Weird")
# else:
#     if 2 <= n <= 5:
#         print("Not Weird")
#     elif 6 <= n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")
