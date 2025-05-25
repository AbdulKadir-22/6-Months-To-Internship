import random

low = 0
high =100
Tries = 5

number = random.randint(low,high)

while True:
    guess = int(input("Enter the number: "))
    if number == guess:
        print("You won")
        break
    elif number < guess:
        print("You have to guess lower")
        Tries -=1
        print(f"You have {Tries}left")
        if Tries == 0:
            print("You lost")
            break
    elif number > guess:
        print("You have to guess higher")
        Tries -=1
        print(f"You have {Tries}left")
        if Tries == 0:
            print("You lost")
            break

