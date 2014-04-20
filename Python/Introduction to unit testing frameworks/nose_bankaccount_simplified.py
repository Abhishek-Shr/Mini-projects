# Unit tests for bankaccount_simplified.py using Nose


# IMPORTS
from bankaccount_simplified import BankAccount
from nose.tools import eq_


class TestBankAccount():
    def setup(self):
        self.ba = BankAccount("George", 1000)

    def test_get_name(self):
        eq_("George", self.ba.get_name())

    def test_get_balance(self):
        eq_(1000, self.ba.get_balance())

    def test_deposit_negative_amount(self):
        eq_(False, self.ba.deposit(-500))

    def test_deposit_positive_amount(self):
        self.ba.deposit(500)
        eq_(1500, self.ba.get_balance())

    def test_withdraw_more_than_balance(self):
        eq_(False, self.ba.withdraw(2500))

    def test_withdraw_amount_less_than_balance(self):
        self.ba.withdraw(600)
        eq_(400, self.ba.get_balance())
