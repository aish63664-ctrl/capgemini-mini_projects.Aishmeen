import utils
def withdraw():
    amount = int(input("Enter amount to withdraw: "))

    if amount > utils.balance:
        print("insufficient balance")
    else:
        utils.balance -= amount
        utils.transactions.append("Withdrawn " + str(amount))
        print("Please collect your money")
