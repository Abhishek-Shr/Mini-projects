# Unit tests for bankaccount_simplified.py using Pytest


# IMPORTS
from bankaccount_simplified import BankAccount


class TestBankAccount():
    def setup(self):
        self.ba = BankAccount("George", 1000)

    def test_get_name(self):
        assert "George" == self.ba.get_name()

    def test_get_balance(self):
        assert 1000 == self.ba.get_balance()

    def test_deposit_negative_amount(self):
        assert False == self.ba.deposit(-500)

    def test_deposit_positive_amount(self):
        self.ba.deposit(500)
        assert 1500 == self.ba.get_balance()

    def test_withdraw_more_than_balance(self):
        assert False == self.ba.withdraw(2500)

    def test_withdraw_amount_less_than_balance(self):
        self.ba.withdraw(600)
        assert 400  == self.ba.get_balance()
