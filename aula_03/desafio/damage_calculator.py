from damage_repository import DamageRepository
from abc import ABC
class DamageCalculator(ABC):
    "DamageCalculator is used to calculate the final damage, based on the attack and pokemon types."

    multipliers = DamageRepository.get_type_effectiveness()
    
    @staticmethod
    def calculate_damage(pokemon_type: str, attack_type: str, attack_raw_damage: int) -> int:
        """Calculates the final damage based on the pokemon and attacks type
        
        Args:
            pokemon_type (str): Type of the pokemon who is receiving the damage.
            attack_type (str): Type of the attack wich is dealing the damage.
            attack_raw_damage (int): The raw damage caused by the attack.
        """

        multiplier = DamageCalculator.multipliers.get(attack_type, 1).get(pokemon_type, 1)

        DamageCalculator.print_damage_effectiveness(multiplier)

        return int(round(attack_raw_damage * multiplier, 0))
    
    @staticmethod
    def print_damage_effectiveness(multiplier: float) -> None:
        """Print a message according the effectiveness od the attack
        
        Args:
            multiplier (float): Multiplier apllied to the damage according the types (attack and pokemon)
        """
        
        if multiplier == 0:
            print("It seems like this attack didn't have any effect!.")
        elif multiplier == 2:
            print("Unbelievable! This attack was overwhelmingly effective, dealing massive damage!")
        elif multiplier == 0.5:
            print("Not very effective. The attack didn't have much impact.")

        return
