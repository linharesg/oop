"""Implementação da conta."""
from __future__ import annotations # Precisa disso porque dentro da classe Conta, existe um atributo usando a própria classe Conta.

class Conta:
    """Conta representa uma conta bancária.
    
    Attributes:
        numero (str): Número identificador da conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo da conta.
        limite (float): Limite da conta.
    """

    quantidade_contas = 0 # Atributo estático - > pertence à classe, e não ao objeto.
    # Atributos normais estão associados a um objeto específico. Atributo estático está relacionado à classe.

    def __init__(self, numero: str, titular: str):
        # Realizando a validação do número da conta.
        if len(numero) != 9:
            raise AttributeError("Número da conta deve possuir 9 dígitos.")
        
        # Encapsulamento
        self.__numero = numero
        self.titular = titular # Está usando o @titular.setter para definir o valor
        self.__limite = 100
        self.__saldo = 0

        Conta.quantidade_contas += 1

    # Formata a visualização (print) do objeto
    def __str__(self):
        return f"TItular: {self.titular} | Saldo: {self.saldo} | Limite: {self.__limite}"

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular: str):
        self.__titular = novo_titular.title()

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite: float):
        self.__limite = novo_limite

    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor: float) -> None:
        """Deposita um valor no saldo da conta.
        
        Args:
            valor (float): Valor do depósito.
        """
        self.__saldo += valor

    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta se o saldo + limite for maior ou igual ao valor do saque
        
        Args:
            valor (float): Valor do saque.

        Returns:
            True se for bem-sucedido, False caso contrário.
        """
        if (self.__saldo + self.__limite) < valor:
            print("Saldo indisponível para realizar a operação.")
            return False

        if self.__saldo < valor:
            self.__limite -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor
        
        return True

    def transferir(self, valor: float, conta_destino: Conta) -> None:
        """Transfere o valor de uma conta para outra se o saldo + limite for igual ao valor do saque.
        
        Args:
            valor (float): Valor da transferência.
            conta_destino (Conta): Conta de destino da transferência.
        """
        if (self.sacar(valor)):
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")

    #Método estática é chamado pela Classe. A diferença é que um método normal é chamado pelo objeto
    @staticmethod
    def verifica_numero_conta(numero: str) -> bool:
        """Verificar se o número da conta é válido.
        
        Args:
            numero (str): Número da conta.
        Returns
            True caso o número da conta seja válido, Flase caso contrário.
        """
        return len(numero) == 9


if __name__ == "__main__":
    conta_william = Conta("123123123", "william cirico")

    print(conta_william.titular)

    print(f"Nome do titular quando foi criado: {conta_william.titular}")

    conta_william.titular = "william cirico"

    print(f"Nome do titular após modificação: {conta_william.titular}")

    print(f"Valor antes do depósito: {conta_william.saldo}")
    conta_william.depositar(100_000_000)
    print(f"Valor após o depósito: {conta_william.saldo}")
    conta_william.sacar(100_000)
    print(f"Valor após o saque: {conta_william.saldo} | Limite: {conta_william.limite}")
    print(conta_william)

    conta_marcos = Conta("123456789", "marcos da silva")

    print(conta_marcos)

    conta_william.transferir(20, conta_marcos)
    print(conta_william)
    print(conta_marcos)

    print(Conta.quantidade_contas)

    if Conta.verifica_numero_conta("123456446"):
        print("Número da conta é válido!")
    else:
        print("Número da conta é inválido!")