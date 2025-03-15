from accounts.bank_account import BankAccount


class SavingsAccount(BankAccount):
    _interest_rate: float = 0.5

    def apply_interest(self)-> float:
        self._balance *= (1 + self._interest_rate)
        return self._balance
