from random import randint
from attack_repository import AttackRepository

class Attack:

    attacks_list = []

    def __init__ (self,id: int, name: str, type: str, power: int, cooldown: int):
        self.id = id
        self.name = name
        self.type = type
        self.power = power
        self.cooldown = cooldown
        self.current_cooldown = 0

    # def __str__(self) -> str:
    #     return f"ID: {self.id} | name: {self.name} | type: {self.type} | power = {self.power} | cooldown = {self.cooldown} | current cooldown = {self.current_cooldown}\n" 

    # def __repr__(self) -> str:
    #     return f"ID: {self.id} | name: {self.name} | type: {self.type} | power = {self.power} | cooldown = {self.cooldown} | current cooldown = {self.current_cooldown}\n" 
    

    def attacks_definition(db_name):

        attacks = AttackRepository(db_name).get_attacks()
        for attack in attacks:
            Attack.attacks_list.append(Attack(*attack))



    
