class Universidade:
    """Representa uma universidade"""

    total_estudantes = 0
    total_professores = 0

    # Sem necessidade de inicialização pois não tem nenhum atributo de objeto?
    def __init__ (self):
        pass
    
    def __str__(self) -> str:
        return f"Estudantes: {self.total_estudantes} | Professores: {self.total_professores} | Total pessoas: {self.obter_total_pessoas()}"

    @staticmethod
    def matricular_estudante():
        Universidade.total_estudantes += 1

    @staticmethod
    def matricular_professor():
        Universidade.total_professores += 1

    @staticmethod
    def obter_total_pessoas():
        return Universidade.total_estudantes + Universidade.total_professores
    
if __name__ == "__main__":

    Universidade.matricular_estudante()
    Universidade.matricular_professor()
    Universidade.matricular_professor()
    Universidade.matricular_professor()
    Universidade.matricular_estudante()
    Universidade.matricular_professor()

    print(Universidade())