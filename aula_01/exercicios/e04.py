class InvalidXInput(Exception):
    pass

class InvalidYInput(Exception):
    pass

class Ponto2D:
    """Representa a posição de um ponto em um plano cartesiano de 2 dimensões.
    
    Attributes:
        x (float): Repsenta a opsição no eixo X.
        Y (float): Repsenta a opsição no eixo Y.
    """
    
    def __str__(self):
        return f"Ponto X: {self.x} | Ponto Y: {self.y}"
    
    def __init__(self, ponto_x, ponto_y):
        
        # Validação de input numérico em X
        if not isinstance(ponto_x, float):
            raise InvalidXInput("Deve ser um número")

        # Validação de input numérico em Y
        if not isinstance(ponto_y, float):
            raise InvalidYInput("Deve ser um número")
        
        self.__x = ponto_x
        self.__y = ponto_y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, ponto_x: float):
        self.__x = ponto_x

    @property
    def y(self):
        return self.__y
    
    @x.setter
    def y(self, ponto_y: float):
        self.__y = ponto_y

    @staticmethod
    def tem_eixo_comm(ponto_a, ponto_b):
        return ponto_a == ponto_b
    
