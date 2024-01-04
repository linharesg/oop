# from battle import Battle

class DamageCalculator:
    "DamageCalculator is used to calculate the final damage, based on the attack and pokemon types."

    multipliers = {
        'Bug': {'Grass': 1.5, 'Psychic': 1.2, 'Dark': 1.2, 'Fire': 0.8},
        'Dark': {'Psychic': 1.5, 'Ghost': 0.8},
        'Dragon': {'Dragon': 1.5},
        'Electric': {'Water': 1.7, 'Flying': 1.5},
        'Fairy': {'Fighting': 1.4, 'Dragon': 0.9, 'Dark': 1.2},
        'Fighting': {'Normal': 1.5, 'Ice': 1.2, 'Rock': 0.9},
        'Fire': {'Grass': 1.7, 'Bug': 1.4, 'Ice': 1.2, 'Water': 0.8},
        'Flying': {'Grass': 1.3, 'Fighting': 1.2, 'Bug': 1.4},
        'Ghost': {'Psychic': 2, 'Ghost': 1.5},
        'Grass': {'Water': 1.6, 'Rock': 1.3, 'Ground': 1.1, 'Fire': 0.7},
        'Ground': {'Fire': 1.7, 'Electric': 0, 'Poison': 2},
        'Ice': {'Grass': 1.6, 'Ground': 1.5, 'Flying': 1.2},
        'Normal': {'Rock': 0.8, 'Ghost': 0, 'Steel': 0.8, 'Electric': 0.8},
        'Poison': {'Grass': 1.5, 'Fairy': 0.9},
        'Psychic': {'Fighting': 1.5, 'Poison': 1.3, 'Dark': 0.7},
        'Rock': {'Fire': 1.6, 'Ice': 1.5, 'Flying': 1.3},
        'Steel': {'Ice': 1.5, 'Rock': 1.5, 'Fairy': 1.2},
        'Water': {'Fire': 1.8, 'Rock': 1.5, 'Ground': 1.2, 'Normal': 1.1},
    }

    @staticmethod
    def calculate_damage(pokemon_type: str, attack_type: str, attack_raw_damage: int) -> int:
        """Calculates the final damage based on the pokemon and attacks type
        
        Args:
            pokemon_type (str): Type of the pokemon who is receiving the damage.
            attack_type (str): Type of the attack wich is dealing the damage.
            attack_raw_damage (int): The raw damage caused by the attack.
        """
        try:
            multiplier = DamageCalculator.multipliers[attack_type][pokemon_type]
        except:
            multiplier = 1

        DamageCalculator.print_damage_effectiveness(multiplier)

        return int(round(attack_raw_damage * multiplier, 0))
    
    def print_damage_effectiveness(multiplier: float) -> None:
        """Print a message according the effectiveness od the attack
        
        Args:
            multiplier (float): Multiplier apllied to the damage according the types (attack and pokemon)
        """
        
        if 1 < multiplier <= 1.2:
            print("The attack was quite effective!")
        elif 1.2 < multiplier < 1.7:
            print("A powerful hit! The attack was highly effective.")
        elif multiplier >= 1.7:
            print("Unbelievable! This attack was overwhelmingly effective, dealing massive damage!")
        elif multiplier < 1:
            print("Not very effective. The attack didn't have much impact.")
        
        return
