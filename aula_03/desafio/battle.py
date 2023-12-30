from pokemon import Pokemon
from random import randint
from datetime import datetime
from pokemon_repository import PokemonRepository
from battle_repository import BattleRepository
from damage_calculator import DamageCalculator
from attack import Attack
from typing import List
class Battle():
    """Represents a battle between two pokemons, controling the rounds, attacks and results.

    Attributes:
        pokemon1 (Pokemon): User's pokemon (referred as 'your pokemon' as well).
        pokemon2 (Pokemon): PC's pokemon (referred as 'opponent's pokemon' as well).
        your_attacks (int): number of attacks done by the user.
        opponents_attacks (int): number of attacks done by the PC.
        winner (str): Who won the battle after finishing it.
        start_time (str): Time when the battle was started.
    
    """
    
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.your_attacks = 0
        self.opponent_attacks = 0
        self.winner = "battle still running"
        self.start_time = datetime.now()

    def __str__(self):
        return f"pokemon1: {self.pokemon1} | pokemon2: {self.pokemon2} | your atk: {self.your_attacks} | opp atk: {self.opponent_attacks} | total round: {self.opponent_attacks + self.your_attacks} | winner : {self.winner}"
    
    @staticmethod
    def start_battle(db_name: str):
        """Starts a battle between 2 pokemons (user and PC).
        
        Args:
            db_name (str): database's name.
        """

        # Define the pokemons and creates an object Battle
        pokemon1 = Battle.choose_pokemon_1(db_name)
        pokemon2 = Battle.choose_pokemon_2(db_name)
        current_battle = Battle(pokemon1, pokemon2)

        # Selects randomly who starts the battle
        if not current_battle.opponent_attacks and not current_battle.your_attacks:
            if randint(0,1):
                input("You Start the battle! Press enter to continue.\n")
                Battle.your_turn(current_battle)
            else:
                input("Your opponent start the battle. Press enter to continue.\n")
                Battle.opponent_turn(current_battle)

        # Call a function to store de battle results, finishing it.
        BattleRepository(db_name).load_battle_results(current_battle)

    def your_turn(self):
        "Controls the sequence of commands in user's round."

        # Check if pokemon1 is defeated
        if self.pokemon1.is_pokemon_defeated():
            input(f"Oh no! Unfortunately your {self.pokemon1.name} was defeated! Keep practicing to improve your battle skills!")
            self.winner = "Opponent"
            return
        
        # Increase the user's rounds by one.
        self.your_attacks += 1

        # Prints the current hp
        input(f"Your {self.pokemon1.name} is current with {self.pokemon1.hp} healh points.")

        # Call a method to choose the attack
        Battle.your_attack(self)

        # Go to oppponent's round.
        self.opponent_turn()

    def opponent_turn(self):
        
        # Check if pokemon2 is defeated.
        if self.pokemon2.is_pokemon_defeated():
            input(f"Your {self.pokemon1.name} did great, you won the battle. Congratulations!")
            self.winner = "You"
            return
        
        # Increase the opponent's rounds by one.
        self.opponent_attacks += 1

        # Prints current status of the opponent's pokemon
        print(f"Opponent's {self.pokemon2.name} is current with {self.pokemon2.hp} health points.")
        
        # Call a method to choose the attack
        Battle.opponent_atack(self)

        # Go to user's round.
        self.your_turn()

    @staticmethod
    def choose_pokemon_1(db_name):
        """Choose the user's pokemon.
        
        Args:
            db_name (str): database's name.
        """    
        
        # Show the list of the available pokemons and ask for a input.
        Pokemon.show_pokemon_list(db_name)
        input_pokemon1 = input("Your Pokemon (by ID): ")

        # Instantiate the user's pokemon and attacks.
        pokemon1 = Pokemon(*Pokemon.pokemon_definition(db_name, input_pokemon1))
        pokemon1.attacks = Pokemon.set_pokemon_attacks(db_name, input_pokemon1)
        print(f"Well done! Your pokemon is {pokemon1.name}.")
        return pokemon1
    
    def choose_pokemon_2(db_name):
        """Choose the opponent's pokemon.
        
        Args:
            db_name (str): database's name.
        """
        # Get the amount of available pokemons, and choose a random.
        pokemon_amount = PokemonRepository(db_name).get_pokemon_amount()
        random_pokemon2 = str(randint(1, pokemon_amount))

        # Instantiate the opponent's pokemon and attacks.
        pokemon2 = Pokemon(*Pokemon.pokemon_definition(db_name, random_pokemon2))
        pokemon2.attacks = Pokemon.set_pokemon_attacks(db_name, random_pokemon2)
        input("Press any key to randomly choose your opponent.\n")
        print(f"Be ready, your opponent is a {pokemon2.name}!")
        return pokemon2
    
    def your_attack(self):
        "Use an avaliable attack aaccording to the available ones, controling its cooldown"

        # Decrease the cooldown of the pokemon attacks.
        Battle.decrease_cooldown(self.pokemon1.attacks)

        # Create an empty dictionary to stores the pokemon's available attacks (without cooldown).
        avaliable_attacks = {}

        print("Choose your attack!")

        # Print the attacks with its cooldown status.
        for num, attack in enumerate(self.pokemon1.attacks):
            if attack.current_cooldown == 0:
                avaliable_attacks[num + 1] = attack
            print(f"{num + 1}\t{attack.name}\t\t cooldown: {attack.current_cooldown}/{attack.cooldown}")
        
        # Ends the attack if all the attacks is  current with a colldown > 0.
        if not len(avaliable_attacks):
            input("Your pokemon is exhausted of attacking! Wait until the next round to a new attack without cooldown.")
            return

        # Input the user's attack, accepting only available attacks.
        try:
            chosen_attack = int(input("Choose you attack: "))
        except:
            chosen_attack = 0
        while not (chosen_attack in avaliable_attacks.keys()):
            try:
                chosen_attack = int(input("Choose an attack without cooldown according the list above!: "))
            except:
                chosen_attack = 0
        
        # Increase the chosen attack by one.
        self.pokemon1.attacks[chosen_attack -1].increase_cooldown()

        # Calculate the raw damage and final damage based on the pokemon and attack type.
        attack_raw_damage = self.pokemon1.attacks[chosen_attack -1].power
        input(f"(You): {self.pokemon1.name}, use {self.pokemon1.attacks[chosen_attack -1].name}!\n")
        final_damage = DamageCalculator.calculate_damage(self.pokemon2.type, self.pokemon1.attacks[chosen_attack -1].type, attack_raw_damage)
        
        # Decrease the opponent's pokemon hp by the final calculated damage.
        self.pokemon2.recieve_damage(final_damage)

    def opponent_atack(self):
        "Choose randomly the opponent's attack according to the availables, controlling the cooldown."

        input("Be ready for your opponent's attack! Press enter to continue.")
        
        # Decreases the attacks cooldown.
        Battle.decrease_cooldown(self.pokemon2.attacks)

        # Creates a empty list do store the available attacks (without cooldown).
        avaliable_attacks = []

        # Stores the available attacks.
        for attack in self.pokemon2.attacks:
            if attack.current_cooldown == 0:
                avaliable_attacks.append(attack.id)

        attack_amount = len(avaliable_attacks)

        # Check if there is not and available attack, ending the opponent's round.
        if not attack_amount:
            input("Opponent's pokemon is exhausted of attacking!")
            return            

        # Choose a random attack only by its id.
        random_index = randint(0, attack_amount -1)
        chosen_attack_id = avaliable_attacks[random_index]

        # Define the attack by its id.
        for attack in self.pokemon2.attacks:
            if chosen_attack_id == attack.id:
                chosen_attack = attack
                break

        # Increase the attack's colldown.
        chosen_attack.increase_cooldown()

        # Calculate the raw and final damage based on the pokemon and attack type.
        attack_raw_damage = chosen_attack.power
        input(f"(Opponent): {self.pokemon2.name}, use {chosen_attack.name}!\n")
        final_damage = DamageCalculator.calculate_damage(self.pokemon1.type, chosen_attack.type, attack_raw_damage)
        self.pokemon1.recieve_damage(final_damage)
    
    def decrease_cooldown(attacks: List[Attack]):
        """Decreases the attack's cooldown if it is not 0.
        
        Args:
            Attacks (List[Attack]): List of the pokemons attacks
        """
        for attack in attacks:
            if attack.current_cooldown > 0:
                attack.current_cooldown -= 1


