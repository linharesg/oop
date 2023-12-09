class Calculadora:
    """Define os métodos estáticas de operação de uma calculadora
    
    Attributes:
        value_1 (float): Primeiro valor da operação
        value_2 (float): Segundo valor da operação
    """

    # É necessário fazer o init, já que será usado só método estático?
    # Pois método estático é direcionado à classe e não ao objeto
    # def __init__(self, value_01: float, value_02: float) -> None:
    #     pass
        

    @staticmethod
    def sum(value_1: float, value_2: float) -> float:
        """Função de somar da calculadora
        
        Args:
            value_1 (float): Valor 1 da operação
            value_2 (float): Valor 2 da operação
        Returns:
            Soma dos valores
        """
        return value_1 + value_2
    
    @staticmethod
    def subtraction(value_1: float, value_2: float) -> float:
        """Função de subtrair da calculadora
        
        Args:
            value_1 (float): Valor 1 da operação
            value_2 (float): Valor 2 da operação
        Returns:
            Subtrai dos valores
        """
        return value_1 - value_2
    
    @staticmethod
    def multiplication(value_1: float, value_2: float) -> float:
        """Função de multiplicar da calculadora
        
        Args:
            value_1 (float): Valor 1 da operação
            value_2 (float): Valor 2 da operação
        Returns:
            Multiplica dos valores
        """
        return value_1 * value_2
    
    @staticmethod
    def division(value_1: float, value_2: float) -> float:
        """Função de dividir da calculadora
        
        Args:
            value_1 (float): Valor 1 da operação
            value_2 (float): Valor 2 da operação
        Returns:
            Divide dos valores
        """
        return value_1 / value_2
    