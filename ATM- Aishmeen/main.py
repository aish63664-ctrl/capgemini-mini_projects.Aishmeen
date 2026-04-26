import show_balance
import deposit
import withdraw
import statement
import menu
def atm():
    while True:
        menu.menu()
        choice = int(input("Enter Your Choice: "))
    
        if choice == 1:
            show_balance.show_balance()
        elif choice == 2:
            deposit.deposit()
        elif choice == 3:
            withdraw.withdraw()
        elif choice == 4:
            statement.statement()
        elif choice == 5:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

atm()