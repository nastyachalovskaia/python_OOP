from accounts.checking_account import CheckingAccount
from accounts.savings_account import SavingsAccount


savings_account = SavingsAccount("Alice")
savings_account.deposit(500)
print(f"Баланс после взноса: {savings_account.balance} руб.")

savings_account.withdraw(100)
print(f"Баланс после выдачи: {savings_account.balance} руб.")

savings_account.apply_interest()
print(f"Баланс после начисления процентов: {savings_account.balance} руб.")

checking_account = CheckingAccount(owner="Макар")
print(f"Сняли деньги: {checking_account.withdraw(1850.0)} руб.") # сняли без ограничений
print(f"Баланс: {checking_account.balance} руб.")

def test_sum():
    assert savings_account.balance > 0
