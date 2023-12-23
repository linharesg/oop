from pokemon import Pokemon
from random import randint
class Attack:

    def __init__ (self,id: int, name: str, type: str, power: int, cooldown: int):
        self.id = id
        self.name = name
        self.type = type
        self.power = power
        self.cooldown = cooldown
        self.current_cooldown = 0

    def __str__(self) -> str:
        return f"ID: {self.id} | name: {self.name} | type: {self.type} | power = {self.power} | cooldown = {self.cooldown} | current cooldown = {self.current_cooldown}" 

    def __repr__(self) -> str:
        return f"ID: {self.id} | name: {self.name} | type: {self.type} | power = {self.power} | cooldown = {self.cooldown} | current cooldown = {self.current_cooldown}" 
        

    def your_attack(pokemon1: Pokemon, pokemon2: Pokemon):
        attacks = pokemon1.attacks
        for num, attack in enumerate(attacks):
            print(f"{num + 1}\t{attack[1]}")
        try:
            chosen_attack = int(input("Choose you attack: "))
        except:
            chosen_attack = 0
        while not (0 < chosen_attack <= len(attacks)):
            try:
                chosen_attack = int(input("Choose your attack according the list above!: "))
            except:
                chosen_attack = 0
        attack_raw_damage = attacks[chosen_attack -1][3]
        input(f"(You): {pokemon1.name}, use {attacks[chosen_attack -1][1]}!\n")
        pokemon2.recieve_damage(attack_raw_damage)

    def opponent_atack(pokemon1: Pokemon, pokemon2: Pokemon):
        attacks = pokemon2.attacks
        attack_amount = len(attacks)
        chosen_attack = randint(0, attack_amount -1)
        attack_raw_damage = attacks[chosen_attack][3]
        input(f"(Opponent): {pokemon2.name}, use {attacks[chosen_attack][1]}!\n")
        pokemon1.recieve_damage(attack_raw_damage)
