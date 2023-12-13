from abc import ABC


class Animal(ABC):
    """Repressenta uma classe base para representar animais diversos"""

    def emitir_som(self):
        print(f"O aniimal está emitindo um som!")
    
    def mover(self):
        print(f"O aniimal está se movendo!")

class Cachorro(Animal):
    """Representa diversos cachorros
    
    Attributes:
        nome (str): Nome do cachorro
    """

    def __repr__(self) -> str:
        return f"{self.nome}"

    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print(f"O {self} está latindo!")

    def mover(self):
        print(f"O {self} está andando!")

class Gato(Animal):
    """Representa diversos gatos
    
    Attributes:
        nome (str): Nome do gato
    """

    def __repr__(self) -> str:
        return f"{self.nome}"

    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print(f"O gato {self} está miando!")

    def mover(self):
        print(f"O gato {self} está fugindo do dono que faz pspsps!")

class Passaro(Animal):
    """Representa diversos pássaros
    
    Attributes:
        nome (str): Nome do pássaro
    """

    def __repr__(self) -> str:
        return f"{self.nome}"

    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print(f"O pássaro {self} está miando!")

    def mover(self):
        print(f"O pássaro {self} está fugindo do dono que faz pspsps!")
    
cachorro_antenor = Cachorro("Antenor")
cachorro_antenor.emitir_som()

gato_bruno = Gato("Bruno")
gato_bruno.emitir_som()
gato_bruno.mover()