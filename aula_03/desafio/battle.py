from pokemon import Pokemon
from random import randint
class Battle():

    
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.your_attacks = 0
        self.opponent_attacks = 0
    
    def start_battle(self):
        print(f"It just started an epic battle between a {self.pokemon1.name} and a {self.pokemon2.name}")
        # Choose the first player to attack
        
        if not self.opponent_attacks and not self.your_attacks:
            if randint(0,1) == 0:
                print("You Start")
                Battle.your_turn(self)
            else:
                print("PC Starts")
                Battle.opponent_turn(self)

    def new_turn(self):
        pass

    def your_turn(self):
        print("Choose your attack!")
        pass

    def opponent_turn(self):
        pass

