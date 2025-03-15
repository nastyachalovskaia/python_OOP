from accounts.bank_account import BankAccount


class CheckingAccount(BankAccount):

    def withdraw(self, amount: float) -> float:
        self._balance -= amount
        return self._balance
