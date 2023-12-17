from pokemon import Pokemon
from random import randint
class Battle():

    
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.your_attacks = 0
        self.opponent_attacks = 0
        self.winner = "battle still running"
    
    def start_battle(self):
        print(f"It just started an epic battle between a {self.pokemon1.name} and a {self.pokemon2.name}")
        # Choose the first player to attack
        
        if not self.opponent_attacks and not self.your_attacks:
            if randint(0,1) == 0:
            # if False == 0:
                print("You Start")
                Battle.your_turn(self)
            else:
                print("PC Starts")
                Battle.opponent_turn(self)

    def new_turn(self):
        pass

    def your_turn(self):
        
        print(f"Your {self.pokemon1.name} is current with {self.pokemon1.hp} healh points.")
        print("Choose your attack!")
        attacks = self.pokemon1.attacks
        for attack in attacks:
            print(f"{attack[0]}\t{attack[1]}")
        pass
        chosen_attack = int(input("Choose you attack (by ID): "))
        for attack in attacks:
            if attack[0] == chosen_attack:
                attack_raw_damage = attack[3]
                print(f"{self.pokemon1.name}, use {attack[1]}!")
                break
        self.pokemon2.hp -= attack_raw_damage
        self.opponent_turn()

    def opponent_turn(self):
        if self.pokemon2.hp <= 0:
            print(f"Your {self.pokemon1.name} did great, you won the Battle. Congratulaitons!")
            self.winner = "You"
            return
        print(f"Opponent's {self.pokemon2.name} is current with {self.pokemon2.hp}")
        pass

