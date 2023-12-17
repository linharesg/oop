from pokemon import Pokemon
from random import randint
from attack import Attack
class Battle():

    
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.your_attacks = 0
        self.opponent_attacks = 0
        self.winner = "battle still running"
    
    def start_battle(self):
        # print(f"It just started an epic battle between a {self.pokemon1.name} and a {self.pokemon2.name}")
        # # Choose the first player to attack
        
        if not self.opponent_attacks and not self.your_attacks:
            if randint(0,1) == 0:
                input("You Start the battle! Press enter to continue.\n")
                Battle.your_turn(self)
            else:
                input("Your opponent start the battle. Press enter to continue.\n")
                Battle.opponent_turn(self)

    def new_turn(self):
        pass

    def your_turn(self):
        if self.pokemon1.is_pokemon_defeated():
            print(f"Oh no! Unfortunately your {self.pokemon1.name} was defeated! Keep practicing to improve your battle skills!")
            self.winner = "Opponent"
            return
        self.your_attacks += 1
        input(f"Your {self.pokemon1.name} is current with {self.pokemon1.hp} healh points.")
        print("Choose your attack!")
        Attack.your_attack(self.pokemon1, self.pokemon2)
        self.opponent_turn()

    def opponent_turn(self):
        
        # Check if pokemon2 is defeated.
        if self.pokemon2.is_pokemon_defeated():
            print(f"Your {self.pokemon1.name} did great, you won the battle. Congratulations!")
            self.winner = "You"
            return
        self.opponent_attacks += 1
        print(f"Opponent's {self.pokemon2.name} is current with {self.pokemon2.hp} health points.")
        input("Be ready for your opponent's attack! Press enter to continue.")
        Attack.opponent_atack(self.pokemon1, self.pokemon2)
        self.your_turn()
        pass
