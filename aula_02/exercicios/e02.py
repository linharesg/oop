from abc import ABC
from math import pi

class FormaGeometrica(ABC):

    def calcular_area():
        pass

    def calcular_perimetro():
        pass

class Circulo(FormaGeometrica):
    """Cria um círculo com o raio informado
    
    Attributes:
        raio (float): Raio de círculo (em mm)
    """

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = round(pi * self.raio ** 2, 2)
        print(f"Área: {area}mm²")

    def calcular_perimetro(self):
        perimetro = round(2 * pi * self.raio, 2)
        print(f"Perîmetro: {perimetro}mm")

class Retangulo(FormaGeometrica):
    """Cria um retângulo com os lados informados
    
    Attributes:
        base (float): Base do retângulo (em mm)
        altura (float): Altura do retângulo (em mm)
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = round(self.base * self.altura)
        print(f"Área: {area}mm²")

    def calcular_perimetro(self):
        perimetro = round(2 * (self.base + self.altura))
        print(f"Perîmetro: {perimetro}mm")

class Retangulo(FormaGeometrica):
    """Cria um triângulo coma altura e base informados
    
    Attributes:
        base (float): Base do retângulo (em mm)
        altura (float): Altura do retângulo (em mm)
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
        
panqueca = Circulo(180)
panqueca.calcular_area()
panqueca.calcular_perimetro()

porta = Retangulo(800, 2100)
porta.calcular_area()
