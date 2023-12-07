class Pessoa:
    """
    Pessoa representa uma pessoa que possui um nome e um telefone.

    Attributes:
        nome (str): Nome da pessoa.
        telefone (str): Telefone da pessoa.
    """

    def __init__(self, nome: str, telefone: str):
        # Validando que seja o nome completo
        if " " not in nome.strip():
            raise AttributeError("Deve informar o nome completo.")
        
        self.nome = nome
        self.__telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome} | Telefone: {self.__telefone}"
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome.title()
    
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone
    
if __name__ == "__main__":

    pessoa_gabriel = Pessoa("gabriel linhares", "999790581")
    pessoa_amanda = Pessoa("amanda varela", "40028922")

    print(pessoa_gabriel)
    print(pessoa_amanda)