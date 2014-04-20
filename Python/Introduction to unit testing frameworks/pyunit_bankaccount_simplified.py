# Unit tests for bankaccount_simplified.py using PyUnit


# IMPORTS
from bankaccount_simplified import BankAccount
import unittest


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.ba = BankAccount("George", 1000)

    def test_get_name(self):
        self.assertEqual("George", self.ba.get_name())

    def test_get_balance(self):
        self.assertEqual(1000, self.ba.get_balance())

    def test_deposit_negative_amount(self):
        self.assertFalse(self.ba.deposit(-500))

    def test_deposit_positive_amount(self):
        self.ba.deposit(500)
        self.assertEqual(1500, self.ba.get_balance())

    def test_withdraw_more_than_balance(self):
        self.assertFalse(self.ba.withdraw(2500))

    def test_withdraw_amount_less_than_balance(self):
        self.ba.withdraw(600)
            self.assertEqual(400, self.ba.get_balance())


# TESTS RUN
if __name__ == '__main__':
    unittest.main()
