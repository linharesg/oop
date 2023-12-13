from abc import ABC, abstractmethod
from math import pi
from math import sqrt

class GeometricForm(ABC):
    """GeometricForm representa uma forma geométrica"""

    @abstractmethod
    def get_area(self) -> float:
        pass
    
    @abstractmethod
    def get_perimeter(self) -> float:
        pass

class Rectangle(GeometricForm):
    """"""

    def __init__(self, side_a: float, side_b: float) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b
    
    def get_perimeter(self):
        return 2 * (self.side_a * self.side_b)

class Circle(GeometricForm):
    """Circle representa um círculo"""

    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def get_area(self) -> float:
        return pi * self.radius ** 2
    
    def get_perimeter(self) -> float:
        return 2 * pi * self.radius

class Triangle(GeometricForm):
    """"""

    def __init__ (self, side_a: float, side_b: float, side_c: float):
        if not self.__is_triangle(side_a, side_b, side_c):
            raise AttributeError("Triângulo não é válido")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def __is_triangle(self, side_a: float, side_b: float, side_c: float) ->bool:
        """Verifica se o triângulo é válido"""
        return (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a)
    
    def get_area(self) ->float:
        """Retorna a área do triângulo utilizando a fórmula de Heron."""
        semiperimeter = (self.side_a + self.side_b + self.side_c) / 2

        return sqrt(semiperimeter * (semiperimeter - self.side_a) * (semiperimeter - self.side_b) * (semiperimeter - self.side_c))
    
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

tia = Triangle(10, 11, 11)
print(tia.get_area())
print(tia.get_perimeter())