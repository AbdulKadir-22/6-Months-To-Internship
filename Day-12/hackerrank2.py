# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money  earned.

from collections import Counter

X = int(input())

shoe_sizes = list(map(int, input().split()))
shoe_inventory = Counter(shoe_sizes)

N = int(input())
earnings = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoe_inventory[size] > 0:
        earnings += price            
        shoe_inventory[size] -= 1  

print(earnings)

