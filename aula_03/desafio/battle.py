from pokemon import Pokemon
from random import randint
from datetime import datetime
from pokemon_repository import PokemonRepository
from battle_repository import BattleRepository
from damage_calculator import DamageCalculator
from attack import Attack
class Battle():

    
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.your_attacks = 0
        self.opponent_attacks = 0
        self.winner = "battle still running"
        self.start_time = datetime.now()

    def __str__(self):
        return f"pokemon1: {self.pokemon1} | pokemon2: {self.pokemon2} | your atk: {self.your_attacks} | opp atk: {self.opponent_attacks} | total round: {self.opponent_attacks + self.your_attacks} | winner : {self.winner}"
    
    def start_battle(db_name: str):

        pokemon1 = Battle.choose_pokemon_1(db_name)
        pokemon2 = Battle.choose_pokemon_2(db_name)
        current_battle = Battle(pokemon1, pokemon2)

        if not current_battle.opponent_attacks and not current_battle.your_attacks:
            if randint(0,1) == 0:
                input("You Start the battle! Press enter to continue.\n")
                Battle.your_turn(current_battle)
            else:
                input("Your opponent start the battle. Press enter to continue.\n")
                Battle.opponent_turn(current_battle)

        BattleRepository(db_name).load_battle_results(current_battle)
    def your_turn(self):

        # Check if pokemon1 is defeated
        if self.pokemon1.is_pokemon_defeated():
            input(f"Oh no! Unfortunately your {self.pokemon1.name} was defeated! Keep practicing to improve your battle skills!")
            self.winner = "Opponent"
            return
        self.your_attacks += 1
        input(f"Your {self.pokemon1.name} is current with {self.pokemon1.hp} healh points.")
        print("Choose your attack!")
        Battle.your_attack(self)
        self.opponent_turn()

    def opponent_turn(self):
        
        # Check if pokemon2 is defeated.
        if self.pokemon2.is_pokemon_defeated():
            input(f"Your {self.pokemon1.name} did great, you won the battle. Congratulations!")
            self.winner = "You"
            return
        self.opponent_attacks += 1
        print(f"Opponent's {self.pokemon2.name} is current with {self.pokemon2.hp} health points.")
        input("Be ready for your opponent's attack! Press enter to continue.")
        Battle.opponent_atack(self)
        self.your_turn()

    def choose_pokemon_1(db_name):
        Pokemon.show_pokemon_list(db_name)
        input_pokemon1 = input("Your Pokemon (by ID): ")
        pokemon1 = Pokemon(*Pokemon.pokemon_definition(db_name, input_pokemon1))
        pokemon1.attacks = Pokemon.set_pokemon_attacks(db_name, input_pokemon1)
        print(f"Well done! Your pokemon is {pokemon1.name}.")
        return pokemon1
    
    def choose_pokemon_2(db_name):
        pokemon_amount = PokemonRepository(db_name).get_pokemon_amount()
        random_pokemon2 = str(randint(1, pokemon_amount))
        pokemon2 = Pokemon(*Pokemon.pokemon_definition(db_name, random_pokemon2))
        pokemon2.attacks = Pokemon.set_pokemon_attacks(db_name, random_pokemon2)
        input("Press any key to randomly choose your opponent.\n")
        print(f"Be ready, your opponent is a {pokemon2.name}!")
        return pokemon2
    
    def your_attack(self):
        Battle.decrease_cooldown(self.pokemon1.attacks)
        avaliable_attacks = {}
        for num, attack in enumerate(self.pokemon1.attacks):
            if attack.current_cooldown == 0:
                avaliable_attacks[num + 1] = attack
            print(f"{num + 1}\t{attack.name}\t\t cooldown: {attack.current_cooldown}/{attack.cooldown}")
        
        if not len(avaliable_attacks):
            input("Your pokemon is exhausted of attacking! Wait until the next round to a new attack without cooldown.")
            return

        try:
            chosen_attack = int(input("Choose you attack: "))
        except:
            chosen_attack = 0
        while not (chosen_attack in avaliable_attacks.keys()):
            try:
                chosen_attack = int(input("Choose an attack without cooldown according the list above!: "))
            except:
                chosen_attack = 0
                
        Battle.increase_cooldown(self.pokemon1.attacks[chosen_attack -1])
    
        attack_raw_damage = self.pokemon1.attacks[chosen_attack -1].power
        input(f"(You): {self.pokemon1.name}, use {self.pokemon1.attacks[chosen_attack -1].name}!\n")
        final_damage = DamageCalculator.calculate_damage(self.pokemon2.type, self.pokemon1.attacks[chosen_attack -1].type, attack_raw_damage)
        self.pokemon2.recieve_damage(final_damage)

    def opponent_atack(self):
        
        Battle.decrease_cooldown(self.pokemon2.attacks)
        avaliable_attacks = []

        for attack in self.pokemon2.attacks:
            if attack.current_cooldown == 0:
                # print(f"{attack.id}\t{attack.name}\t\t cooldown: {attack.current_cooldown} | C: {attack.cooldown} | {attack}")
                avaliable_attacks.append(attack.id)
            # else:
                # print(f"{attack.id}\t{attack.name}\t\t cooldown: {attack.current_cooldown} | C: {attack.cooldown} | {attack}")

        attack_amount = len(avaliable_attacks)

        if not attack_amount:
            input("Opponent's pokemon is exhausted of attacking!")
            return            

        random_index = randint(0, attack_amount -1)
        chosen_attack_id = avaliable_attacks[random_index]

        for attack in self.pokemon2.attacks:
            if chosen_attack_id == attack.id:
                chosen_attack = attack
                break
        Battle.increase_cooldown(chosen_attack)

        attack_raw_damage = chosen_attack.power
        input(f"(Opponent): {self.pokemon2.name}, use {chosen_attack.name}!\n")
        final_damage = DamageCalculator.calculate_damage(self.pokemon1.type, chosen_attack.type, attack_raw_damage)
        self.pokemon1.recieve_damage(final_damage)

    def increase_cooldown(attack: Attack):
        attack.current_cooldown = attack.cooldown + 1

    def decrease_cooldown(attacks: Attack):
        for attack in attacks:
            if attack.current_cooldown > 0:
                attack.current_cooldown -= 1


