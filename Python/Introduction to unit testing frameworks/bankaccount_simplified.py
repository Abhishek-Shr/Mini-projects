class BankAccount():
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def get_name(self):
        return self._name

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            return False
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 0:
            return False
        self._balance -= amount
