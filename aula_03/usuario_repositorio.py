from typing import Any
import sqlite3
from usuario import Usuario
from typing import List

class UsuarioRepositorio:
    """Repositório de usuários.
    
    Attributes:
        db_nome (str): Nome do banco de dados.
    """

    def __init__(self, db_nome: str):
        self.dbnome = db_nome

    # CRUD:
        # CREATE
        # READ
        # UPDATE
        # DELATE
    
    def __executar_query(self, query: str, *params: Any): # Usado mais pra criaçao de atualização de dados. Não usado pra obter dados (selects).
        """Executa uma query no banco de dados.
        
        Args:
            query (str): Query que será executada.
            params (Any): Parâmetros da query.
        """
        connection = sqlite3.connect(self.dbnome) # Abrir uma conexção com o sqlite
        cursor = connection.cursor() # através do cursos que consegue executar as consultas do banco de dados.
        cursor.execute(query, params) # Executar a query
        connection.commit() # Commitar as alterações feitas pela consulta
        connection.close() # Fecha a coneção com o banco de dados

    def inserir_usuario(self, usuario: Usuario):
        """ Insere um usuário no bando de dados. O objeto usuário é atualizado com o ID do banco.

        Args:
            usuario (Usuario): Usuário que será criado no banco de dados.      
        """
        query = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"
        self.__executar_query(query, usuario.nome, usuario.email)

        usuario.id = self.__get_ultimo_id_inserido()
        return usuario
    
    def obter_usuarios(self) -> List[Usuario]:
        """Obtém todos os usuários cadastrados no banco de dados."""
        query = "SELECT * FROM usuarios;"
        connection = sqlite3.connect(self.dbnome) # Abrir uma conexção com o sqlite
        cursor = connection.cursor() # através do cursos que consegue executar as consultas do banco de dados.
        cursor.execute(query) # Executar a query
        rows = cursor.fetchall()
        connection.close()
        # (1, "Gabriel, "gabriel@gmail.com")
        return [Usuario(row[1], row[2], row[0]) for row in rows] #utilizando "list comprehension" pra gerar a lista de usuarios

    def atualizar_usuario(self, usuario: Usuario):
        """Atualiza um usuário no banco de dados
        
        Args:
            usuario (Usuario): Usuário que será atualizado.
        """
        query = "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?"
        self.__executar_query(query, usuario.nome, usuario.email, usuario.id)


    def remover_usuario(self, usuario: Usuario):
        """Remove um usuário do banco de dados.
        
        Args:
            usuario (Usuarios): Usuário que será removido
        """
        query = "DELETE FROM usuarios WHERE id = ?"
        self.__executar_query(query, usuario.id)

    def __get_ultimo_id_inserido(self) -> int:
        """Retorna o ID do último registro inserido na tabela de usuários."""
        query = "SELECT id FROM usuarios ORDER BY id DESC LIMIT 1"
        connection = sqlite3.connect(self.dbnome) # Abrir uma conexção com o sqlite
        cursor = connection.cursor() # através do cursos que consegue executar as consultas do banco de dados.
        cursor.execute(query) # Executar a query
        row = cursor.fetchone()
        connection.close()
        return row[0]