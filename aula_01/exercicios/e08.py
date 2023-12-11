from datetime import date

class Veiculo:
    """Define veículos
    
    Attributes:
        marca (str): Marca do veículo.
        ano (int): Ano de fabricação do veículo.
        valor_base (float): Valor base do veículo.
    """

    def __init__ (self, marca: str, ano: int, valor_base: float):

        self.__marca = marca
        self.__ano = ano
        self.__valor_base = valor_base

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def valor_base(self):
        return self.__valor_base
    
    @valor_base.setter
    def valor_base(self, valor):
        self.__valor_base = valor

    @staticmethod
    def get_current_year():
        return date.today().year

    def get_depreciacao(self):
        return self.__valor_base * (Veiculo.get_current_year() - self.ano) * 0.05
    
    def calcular_imposto(self):
        return Veiculo.get_depreciacao(self) * 0.02
        

veiculo1 = Veiculo("ford", 2010, 50000)

print(veiculo1.get_depreciacao())
print(veiculo1.calcular_imposto())
