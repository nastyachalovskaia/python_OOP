from dataclasses import dataclass
from accounts.bank_account import BankAccount


@dataclass
class SavingsAccount(BankAccount):
    interest_rate: float = 0.5

    def apply_interest(self):
        self._balance *= (1 + self.interest_rate)
        return self._balance
