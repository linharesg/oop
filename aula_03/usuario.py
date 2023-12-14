"""Modelo de usuário."""

class Usuario:
    """Classe para representar um usuário.
    
    Attributes:
        id (int): ID do usuário.
        nome (str): Nome do usuário.
        email (str): E-mail do usuário.
    """
    def __init__(self, nome: str, email: str, id: int = None) -> None:
        self.nome = nome
        self.email = email
        self.id = id

    def __str__(self) -> str:
        return f"ID: {self.id} Usuário: {self.nome} | E-mail: {self.email}"
    
    def __repr__(self) -> str:
        return f"ID: {self.id} Usuário: {self.nome} | E-mail: {self.email}"