#Fução para gerar html com log do pyteste
# pytest --cov=. --cov-report=html:coverage


import pytest

from e02 import Aluno, InvalidRegistration, InvalidNameError

def test_criacao_aluno():
    aluno = Aluno("12312312", "gabriel linhares", [1, 5, 8])
    assert aluno.matricula == "12312312"
    assert aluno.nome == "Gabriel Linhares"
    assert aluno.notas == [1, 5, 8]

# sintaxe exclusiva para teste de exceções
def test_invalid_registration():
    with pytest.raises(InvalidRegistration):
        aluno = Aluno("123123", "gabriel linhares", [1, 5, 8])
        
# sintaxe exclusiva para teste de exceções
def test_invalid_name():
    with pytest.raises(InvalidNameError):
        aluno = Aluno("12312312", "gabrielinhares", [1, 5, 8])

def test_get_situacao():
    aluno1 = Aluno("12312312", "erg rgeg", [9, 8, 7])
    assert aluno1.get_situacao() == "Aprovado"
    aluno2 = Aluno("12312312", "erg rgeg", [2, 3, 1])
    assert aluno2.get_situacao() == "Reprovado"
    aluno3 = Aluno("12312312", "erg rgeg", [6, 5, 6])
    assert aluno3.get_situacao() == "Recuperação"