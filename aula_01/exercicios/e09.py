class Pessoas:
    """Representa o cadastro de pessoas.
    
    Attributes:
        nome (str): Nome da pessoa
        Idade (int): Idade da pessoa
    """

    # Total de pessoas instanciadas pela classe
    __total_pessoas = 0

    def __init__(self, nome, idade) -> None:
        
        self.__nome = nome
        self.__idade = idade

        Pessoas.__total_pessoas += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    # Não é necessário getter pois, ao ser chamado pelo setter, mostra apenas o espaço de alocação na memória
    # @property
    # def total_pessoas():
    #     return Pessoas.__total_pessoas

    # Não necessita de setter pois não será atribuído nenhum valor. Cálculo automático definido no __init__   
    # @total_pessoas.setter
    # def total_pessoas(valor):
    #     __total_pessoas = Pessoas.total_pessoas

    # def get_total_pessoas():
    #     return Pessoas.total_pessoas

    @staticmethod
    def get_total_pessoas():
        return Pessoas.__total_pessoas


pessoa1 = Pessoas("Gabriel", 27)
pessoa2 = Pessoas("Amanda", 26)

print(f"Total de pessoas instanciadas: {Pessoas.get_total_pessoas()}")    