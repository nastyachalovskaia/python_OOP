from dataclasses import dataclass


@dataclass
class BankAccount:
    owner: str
    _balance: float = 0.0

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            raise ValueError("Сумма не может быть отрицательной, попробуйте снова.")

    def withdraw(self, amount: float) -> float:
        if self._balance >= amount:
            self._balance -= amount
            return self._balance
        else:
            raise ValueError("Баланс меньше введённой суммы, попробуйте уменьшить значение.")

    @property
    def balance(self) -> float:
        return self._balance
