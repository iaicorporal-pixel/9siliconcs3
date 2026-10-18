# bankaccount class: stores an account number and balance, rejecting negative balances
class BankAccount:
    # constructor: sets up the account and validates the starting balance
    def __init__(self, account_number, balance):
        # private account number
        self.__account_number = account_number
        # start at 0.0 so the balance is always defined
        self.__balance = 0.0
        # route through the setter to apply the negative-value check
        self.set_balance(balance)

    # setter for the account number; converts the input to an int
    def set_account_number(self, account_number):
        self.__account_number = int(account_number)

    # setter for the balance; rejects negatives, otherwise stores the value as a float
    def set_balance(self, balance):
        # print an error and leave the current balance unchanged if negative
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = float(balance)

    # read-only access to the account number (a.account_number)
    @property
    def account_number(self):
        return self.__account_number

    # read-only access to the balance (a.balance)
    @property
    def balance(self):
        return self.__balance


# create an account with number 12345 and a starting balance of 1000
a1 = BankAccount(12345, 1000)
print("Account 1")
# show the account number and balance, with the balance shown to two decimal places
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

# try to set a negative balance; the setter rejects it, so the balance stays at 1000
print("\nUpdate balance to -100")
a1.set_balance(-100)
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")