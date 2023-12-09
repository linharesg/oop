class Carro:
    """Carro representa um carro
    
    Attributes:
        marca (str): Marca do carro
        modelo (str): Modelo do carro
        ano (int): Ano do carro
    """

    def __init__(self, marca_carro, modelo_carro, ano_carro):

        self.__marca = marca_carro
        self.modelo = modelo_carro
        self.ano = ano_carro
        self.velocidade = 0
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} | Modelo: {self.modelo} | ano: {self.ano} | velocidade: {self.velocidade}"

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, qualquer_string):
        self.__marca = qualquer_string

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade == 0:
            print("O carro já está parado, não tem como frear.")
            return
        self.velocidade -= 5
