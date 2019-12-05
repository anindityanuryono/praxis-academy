balance = 100000
import sys

def main():
    print("===========================================")
    print("\tWelcome to this simple ATM machine")
    print("===========================================")
    print()
    print("\tPlease select ATM Transactiions")
    print("\tPress [1] Deposit")
    print("\tPress [2] Withdraw");
    print("\tPress [3] Balance Inquiry");
    print("\tPress [4] Exit");
    print()
    option = int(input("\tWhat would you like to do"))

    while option > 4:
        print("\n\tEnter a right option ")
        option = int(input("\tWhat would you like to do"))

    if option == 1:
        print("\tBalance ", balance)
        Deposit = float(input("\tEnter the amount of money to deposit: "))
        if Deposit > 0:
            forewardbalance = (balance + Deposit)
            print("\tYou deposited the ammount of ", forewardbalance)
        else:
            print("\tNone deposit made")

    elif option == 2:
        print("\tBalance = ", balance)
        Withdraw = float(input("Enter withdraw amount = "))
        if Withdraw > 0:
            forewardbalance = (balance - Withdraw)
            print("\tForeward Balance  £ ", forewardbalance)
        elif Withdraw > balance:
            print("\tThe amount you withdraw is greater than to your balance")
            print("\tPlease check the amount you entered.")
        elif balance <= 50000:
            print("\tYou do not have sufficient money to withdraw")
            print("\tChecked your balance to see your money in the bank.")
        else:
            print("\tNone withdraw made")

    elif option == 3:
        if balance == 0:
            print("\tYour current balance is zero")
            print("\tYou cannot withdraw!")
            print("\tYou need to deposit money first.")
        print("\tBalance  £ ", balance)

    elif option == 4:
        sys.exit()

main()















