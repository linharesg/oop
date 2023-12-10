from e01 import Pessoa

def MaxContact(Exception):
    """Exceção para limite de contatos na agenda"""
    pass


class Agenda:
    """Agenda de contatos com até 10 pessoas"""
    contatos = {}
    
    def __str__(self):
        return f"\n".join(str(contato) for contato in Agenda.contatos.values())

    def __init__(self):
        # self.contatos = {}
        #self.contatos = contatos
        pass

    @staticmethod
    def adicionar_pessoa(nome, telefone):
        if len(Agenda.contatos) > 1:
            raise MaxContact("Agenda atingiu o limite de 10 contatos")
        
        contato_id = "contato_" + str(len(Agenda.contatos) + 1)
        Agenda.contatos[contato_id] = Pessoa(nome, telefone)
    
    @staticmethod
    def listar_pessoas():
         print(Agenda())

    @staticmethod
    def buscar_pessoa(nome_da_pessoa):
        for i in Agenda.contatos:
            if Agenda.contatos[i]["nome"] == nome_da_pessoa:
                print(Agenda.contatos)

Agenda.adicionar_pessoa("algue silva", "321123")
Agenda.adicionar_pessoa("algue silva1", "321123")

Agenda.listar_pessoas()
print("OI")
Agenda.buscar_pessoa("contato_2")