from numpy import mean
from typing import List
class InvalidNameError(Exception):
    """Exceção para nome inválido"""
    pass

class InvalidRegistration(Exception):
    """Exceção para matrícula inválida"""
    pass

class InvalidNote(Exception):
    """Exceção para nota inválida (não numérica)"""

class Aluno:
    """Aluno representa um aluno cadastrado
    
    Attributes:
        # Na verdade não precisava colocar a Matrícula, porque é um atributo privado.
        matricula (str): Matrícula do aluno.
        nome (str): Nome do aluno.
        notas (list): Notas do aluno

    """
    # def __init__(self, matricula: str, nome: str, notas: list):
    def __init__(self, matricula: str, nome: str, notas: List[float]): # declarado "List[float]" com o uso do import no início do código"
        
        if not matricula.isdigit() or len(matricula) != 8:
            raise InvalidRegistration()

        
        if len(nome.strip().split()) == 1:
            raise InvalidNameError()
        
        for nota in notas:
            if not isinstance(nota, (int, float)) or not 0 <= nota <= 10:
                raise InvalidNote()

        # Matrícula definida com __ aqui por não tem o seter pra definir que vai ser
        self.__matricula = matricula
        self.nome = nome
        self.notas = notas
    
    # Criado o property para poder acessar um atributo privado de fora da classe
    @property
    def matricula(self):
        return self.__matricula
    
    # Matrícula não precisa do setter pois a matricula não deve ser modificada.
    # @matricula.setter
    # def matricula(self, matricula: str):
    #     self.__matricula = matricula
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.title()

    @property
    def notas(self):
        return self.__notas
    
    @notas.setter
    def notas(self, notas: list):
        self.__notas = notas
    

    def get_media(self):
        return mean(self.notas)
    
    def get_situacao(self):
        if self.get_media() < 4.75:
            return "Reprovado"
        if self.get_media() >= 6.75:
            return "Aprovado"
        return "Recuperação"

if __name__ == "__main__":

    gabriel = Aluno("14203765", "gabriel linhares", [10, 9, 8])
    print(gabriel.get_media())
    print(gabriel.get_situacao())
