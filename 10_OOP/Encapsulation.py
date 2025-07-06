# ✅ 4. Encapsulation (Private Variables)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"💸 Deposited: {amount}")

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
print("🏦 Current Balance:", acc.get_balance())
