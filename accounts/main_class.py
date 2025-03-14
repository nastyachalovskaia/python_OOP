from accounts.savings_account import SavingsAccount

savings_account = SavingsAccount("Alice")
savings_account.deposit(500)
print(f"Баланс после взноса: {savings_account.get_balance} руб.")

savings_account.withdraw(100)
print(f"Баланс после выдачи: {savings_account.get_balance} руб.")

savings_account.apply_interest()
print(f"Баланс после начисления процентов: {savings_account.get_balance} руб.")

def test_sum():
    assert savings_account.get_balance > 0
