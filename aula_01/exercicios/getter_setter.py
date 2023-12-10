# encapsulamento com __, getter e setter
# usar somente para entender o que ocorre por trás dos panos. se o atributo está encapsulado sem getter e setter, NÃO É PARA gettar/settar de fora da classe.

class Veiculo:

    def __init__ (self, marca_do_veiculo: str, ano_veiculo: int, valor_base_veiculo: float):

        # atributo 'marca' encapsulado pelo __ (acaba virando '_Veiculo__marca')    
        self.__marca = marca_do_veiculo # recebe o argumento do método construtor __init__

    @property
    def marcagetter123(self): # posso criar um "nome que eu quiser" para chamar esse atributo privado"
        return self.__marca
    
    @marcagetter123.setter # na definição do setter, eu chamo pelo "nome do getter" que eu criei
    def marcasetter456(self, valor): # posso usar o "nome que eu quiser" para atribuição do setter
        # self.__marca = valor -> funciona igual à linha abaixo
        self._Veiculo__marca = valor # o encapsulamento com "__" nada mais é do que trocar o nome do atirbuto de "__NomeDoAtributo" para "_Classe__NomeDoAtributo"


carro1 = Veiculo("ford", 220, 1212)
print(f"marca original: {carro1.marcagetter123}")

carro1.marcasetter456 = "bmw" # usando o setter criado
print(f"marca nova: {carro1.marcagetter123}") # usando o getter criado

carro1._Veiculo__marca = "mercedes" # atribuindo valor novo pelo "nome alterado pelo encapsulamento __"
print(f"chamando a marca pelo encapsulamento (marca nova nova): {carro1._Veiculo__marca}") # mesma coisa no getter

