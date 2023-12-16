"""Pokemon model"""
from abc import ABC

class Pokemon(ABC):
    """This class represents a Pokemon
    
    Attributes:
        id (int): Pokemon's ID.
        name (str): Pokemon's name.
        type (str): Pokemon's type.
        hp (int): Pokemon's initial health points
    """
    def __init__(self, id: int,  name: str, type: str, hp: int) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.hp = hp
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp}"
    
    def __repr__(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp}"
    
    def attack():
        pass

    