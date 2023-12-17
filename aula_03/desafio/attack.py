from pokemon import Pokemon
from random import randint
class Attack:

    def your_attack(pokemon1: Pokemon, pokemon2: Pokemon):
        attacks = pokemon1.attacks
        for attack in attacks:
            print(f"{attack[0]}\t{attack[1]}")
        pass
        chosen_attack = int(input("Choose you attack (by ID): "))
        for attack in attacks:
            if attack[0] == chosen_attack:
                attack_raw_damage = attack[3]
                input(f"(You): {pokemon1.name}, use {attack[1]}!\n")
                break
        pokemon2.recieve_damage(attack_raw_damage)

    def opponent_atack(pokemon1: Pokemon, pokemon2: Pokemon):
        attacks = pokemon2.attacks
        attack_amount = len(attacks)
        chosen_attack = randint(0, attack_amount -1)
        attack_raw_damage = attacks[chosen_attack][3]
        input(f"(Opponent): {pokemon2.name}, use {attacks[chosen_attack][1]}!\n")
        pokemon1.recieve_damage(attack_raw_damage)
