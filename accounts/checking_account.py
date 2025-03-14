from accounts.bank_account import BankAccount
from dataclasses import dataclass


@dataclass
class CheckingAccount(BankAccount):

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance