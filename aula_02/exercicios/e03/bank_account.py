from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint

class BankAccount(ABC):
    """BacnkAccount representa uma conta bancária
    
    Attributes:
        holder (str): Nome do titular
    """

    def __init__(self, holder: str) -> None:
        self.__registration = randint(1, 100_000)
        self.__balance = 0
        self.holder = holder

    @property
    def registration(self):
        """(int): Número da conta."""
        return self.__registration
    
    @property
    def balance(self):
        """(float): Saldo da conta."""
        return self.__balance
    
    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Saldo não pode ser negativo")
        self.__balance = value

    def withdraw(self, amount: float) -> bool:
        """Saca um valor da conta.
        
        Args:
            amount (float): Valor que será sacado

        Returns:
            True caso o saque tenha sido realizado com sucesso, false caso contrário
        """
        if self.__balance >= amount:
            self.__balance -=amount
            return True
        return False
    
    def deposit(self, amount: float):
        """Deposita um valor na conta.
        
        Args:
            amount (float): Valor que será depositado na conta.
        """
        tax = self.get_deposit_tax()
        self.__balance += amount * (1 - tax)

    def transfer(self, amount: float, target_account: BankAccount):
        """Transfere um valor para outra conta
        
        Args
            amount (float): Valor que será transferido.
            target_account (BankAccount): Conta de destino da transferência
        """
        if(self.withdraw(amount)):
            target_account.deposit(amount)
        else:
            print("Não foi possível realizar a transferência: Saldo indisponível.")

    @abstractmethod
    def get_deposit_tax(self) -> float:
        """Retorna a taxa de depósito."""