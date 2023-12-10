from e01 import Pessoa

def MaxContact(Exception):
    """Exceção para limite de contatos na agenda"""
    pass


class Agenda:
    """Agenda de contatos com até 10 pessoas"""
    contatos = {}
    
    def __str__(self):
        return f"{Agenda.contatos}"

    def __init__(self):
        pass

    @staticmethod
    def adicionar_pessoa(nome, telefone):
        if len(Agenda.contatos) == 10:
            raise MaxContact("Agenda atingiu o limite de 10 contatos")
        
        contato_novo = Pessoa(nome, telefone)
        Agenda.contatos[contato_novo.nome] = contato_novo.telefone
        
    
    @staticmethod
    def listar_pessoas():
         for nome in Agenda.contatos:
             print(f"Nome: {nome} | Telefone: {Agenda.contatos[nome]}")

    @staticmethod
    def buscar_pessoa(nome_da_pessoa):
        print(f"Nome: {nome_da_pessoa} | Telefone: {Agenda.contatos[nome_da_pessoa]}")

    @staticmethod
    def remover_pessoa(nome_da_pessoa):
        Agenda.contatos.pop(nome_da_pessoa)
        



Agenda.adicionar_pessoa("gabriel socreppa", "123")
Agenda.adicionar_pessoa("amanda varela", "321")

Agenda.listar_pessoas()

Agenda.buscar_pessoa("Gabriel Socreppa")

Agenda.remover_pessoa("Gabriel Socreppa")

Agenda.listar_pessoas()