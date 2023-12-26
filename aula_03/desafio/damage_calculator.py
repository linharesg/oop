# from battle import Battle

class DamageCalculator:
    """DamageCalculator is used to calculate the final damage, based on the attack and pokemon types
    
    Attributes:

    Returns:
    
    """

    multipliers = {
        'Bug': {'Grass': 1.5, 'Psychic': 1.2, 'Dark': 1.2},
        'Dark': {'Psychic': 1.5, 'Ghost': 0.8},
        'Dragon': {'Dragon': 1.5},
        'Electric': {'Water': 1.7, 'Flying': 1.5},
        'Fairy': {'Fighting': 1.4, 'Dragon': 0.9, 'Dark': 1.2},
        'Fighting': {'Normal': 1.5, 'Ice': 1.2, 'Rock': 0.9},
        'Fire': {'Grass': 1.7, 'Bug': 1.4, 'Ice': 1.2, 'Water': 0.8},
        'Flying': {'Grass': 1.3, 'Fighting': 1.2, 'Bug': 1.4},
        'Ghost': {'Psychic': 2, 'Ghost': 1.5},
        'Grass': {'Water': 1.6, 'Rock': 1.3, 'Ground': 1.1},
        'Ground': {'Fire': 1.7, 'Electric': 0, 'Poison': 2},
        'Ice': {'Grass': 1.6, 'Ground': 1.5, 'Flying': 1.2},
        'Normal': {'Rock': 0.8, 'Ghost': 0, 'Steel': 0.8},
        'Poison': {'Grass': 1.5, 'Fairy': 0.9},
        'Psychic': {'Fighting': 1.5, 'Poison': 1.3, 'Dark': 0.7},
        'Rock': {'Fire': 1.6, 'Ice': 1.5, 'Flying': 1.3},
        'Steel': {'Ice': 1.5, 'Rock': 1.5, 'Fairy': 1.2},
        'Water': {'Fire': 1.8, 'Rock': 1.5, 'Ground': 1.2},
    }


    def calculate_damage(pokemon_type: str, attack_type: str, attack_raw_damage: int):
        
        try:
            multiplier = DamageCalculator.multipliers[attack_type][pokemon_type]
        except:
            multiplier = 1
        # print(f"multiplicador consta?: {pokemon_type in DamageCalculator.multipliers[attack_type].keys()}")
        # print(f"multiplicador: {multiplier}")
        # print(f"pokemon type: {pokemon_type}")
        # print(f"atk type: {attack_type}")

        return attack_raw_damage * multiplier