from pokemon import Pokemon

class PokemonPlayer(Pokemon):

    def __init__(self, id: int,  name: str, type: str, hp: int):
        
        super().__init__(id,  name, type, hp)
        self.current_hp = self.hp
        self.level = 0
        self.attacks = []

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp} | current hp: {self.current_hp} | level: {self.level} \n Attacks : {self.attacks}"
    
    def __repr__(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp} | current hp: {self.current_hp} | level: {self.level}"