from __future__ import annotations
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    """SavingsAccount representa uma conta bancária."""

    interet_percentage = 0.58

    def __init__ (self, holder: str, initial_balance: float):
        super().__init__(holder)
        self.initial_balance = initial_balance
        self.deposit(initial_balance)

    def generate_interest(self):
        """Gera o juros mensal da conta."""
        self.balance += self.balance * (SavingsAccount.interet_percentage / 100)
    
    def get_deposit_tax(self) -> float:
        """Retorna a taxa de depósito."""
        return 0.005
    
if __name__ == "__main__":
    savings_account = SavingsAccount("Gabriel", 1000)

    savings_account.deposit(500)
    print(savings_account.balance)