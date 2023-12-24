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

    def __str__(self) -> str:
        return f"ID: {self.id} | name: {self.name} | type: {self.type} | power = {self.power} | cooldown = {self.cooldown} | current cooldown = {self.current_cooldown}\n" 

    def __repr__(self) -> str:
        return f"ID: {self.id} | name: {self.name} | type: {self.type} | power = {self.power} | cooldown = {self.cooldown} | current cooldown = {self.current_cooldown}\n" 
    

    def attacks_definition(db_name):

        attacks = AttackRepository(db_name).get_attacks()
        for attack in attacks:
            Attack.attacks_list.append(Attack(*attack))

    def your_attack(pokemon1, pokemon2):
        attacks = pokemon1.attacks
        for num, attack in enumerate(attacks):
            print(f"{num + 1}\t{attack.name}")
        try:
            chosen_attack = int(input("Choose you attack: "))
        except:
            chosen_attack = 0
        while not (0 < chosen_attack <= len(attacks)):
            try:
                chosen_attack = int(input("Choose your attack according the list above!: "))
            except:
                chosen_attack = 0
        attack_raw_damage = attacks[chosen_attack -1].power
        input(f"(You): {pokemon1.name}, use {attacks[chosen_attack -1].name}!\n")
        pokemon2.recieve_damage(attack_raw_damage)

    def opponent_atack(pokemon1, pokemon2):
        attacks = pokemon2.attacks
        attack_amount = len(attacks)
        chosen_attack = randint(0, attack_amount -1)
        attack_raw_damage = attacks[chosen_attack].power
        input(f"(Opponent): {pokemon2.name}, use {attacks[chosen_attack].name}!\n")
        pokemon1.recieve_damage(attack_raw_damage)

    
