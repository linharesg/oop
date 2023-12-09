#Fução para gerar html com log do pyteste
# pytest --cov=. --cov-report=html:coverage

import pytest

from e04 import Ponto2D, InvalidXInput, InvalidYInput

def test_ponto_x():
    novo_ponto2d = Ponto2D(12, -16.5)

    assert novo_ponto2d.x == 12
    assert novo_ponto2d.y == -16.5

def test_eixo_comum():
    ponto1 = Ponto2D(-8, 15)
    ponto2 = Ponto2D(-8, 6)

    # assert Ponto2D.tem_eixo_comum(10, 10) == True
    assert Ponto2D.tem_eixo_comum(ponto1.x, ponto2.x) == True


