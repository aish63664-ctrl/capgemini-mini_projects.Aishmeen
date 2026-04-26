import utils
def deposit():
    amount = int(input("Enter amount to deposit: "))
    if amount <= 0:
        print("enter positive amount")
        return
    utils.balance += amount
    utils.transactions.append("Deposited " + str(amount))
    print("Amount deposited")

