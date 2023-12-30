from random import randint
from attack_repository import AttackRepository

class Attack:
    """Represent the pokemon's attacks.

    Attributes:
        id (int): Attack's ID.
        name (str): Attack's name.
        type (str): Attack's type.
        power (int): Power of the attack (raw damage, independent of type).
        cooldown (int): Number of rounds that must wait until use the same attack again in a battle.
        current_cooldown (int): Number of round that's already gone since the last use of the attack.    
    """
    # Stores all the attacks on the database as objects in a list.
    attacks_list = []

    def __init__ (self,id: int, name: str, type: str, power: int, cooldown: int):
        self.id = id
        self.name = name
        self.type = type
        self.power = power
        self.cooldown = cooldown
        self.current_cooldown = 0

    def __str__(self) -> str:
        return f"ID: {self.id} | name: {self.name} | type: {self.type} | power = {self.power} | cooldown = {self.cooldown} | current cooldown = {self.current_cooldown}\n" 

    def __repr__(self) -> str:
        return f"ID: {self.id} | name: {self.name} | type: {self.type} | power = {self.power} | cooldown = {self.cooldown} | current cooldown = {self.current_cooldown}\n" 
    

    def attacks_definition(db_name: str) -> None:
        """Stores all the attacks of the database in a list
        
        Args: 
            db_name (str): name of the database.
        """
        attacks = AttackRepository(db_name).get_attacks()
        for attack in attacks:
            Attack.attacks_list.append(Attack(*attack))



    
