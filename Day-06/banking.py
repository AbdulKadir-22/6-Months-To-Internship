
def withdraw(balance):
    withdraw = float(input("How much you want to withdraw: "))
    balance = balance- withdraw
    print(f"NOw your balance is {balance:.2f}$")
    return balance

def deposit(balance):
    deposit = float(input("How much you want to add: "))
    balance += deposit
    print(f"NOw your balance is {balance:.2f}$")
    return balance

def showBalance(balance):
    print(f"Your balance is {balance:.2f}$")



def main():
    balance = 0
    isRunning = True
    while isRunning:
        print("Enter 1 to check the balance")
        print("Enter 2  to deposit money")
        print("Enter 3 to withdraw money")
        print("Enter 4 to exit")
        choice = input("Enter (1-4): ")

        if choice == "1":
            showBalance(balance)

        elif choice == "2":
            balance += deposit(balance)

        elif choice == "3":
            balance -= withdraw(balance)

        elif choice == "4":
            isRunning = False
        
        else:
            print("Enter a valid choice")
        

if __name__ == '__main__':
    main()