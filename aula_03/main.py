from inicializador_bd import InicializadorBD
from usuario_repositorio import UsuarioRepositorio
from usuario import Usuario

DB_NOME = "exemplo.db"
InicializadorBD.criar_tabelas(DB_NOME)

usuario_repositorio = UsuarioRepositorio(DB_NOME)

usuario1 = Usuario("Gabriel Linhares", "gabriel@gmail.com")
usuario2 = Usuario("Amanda Varela", "amanda@gmail.com")

try:
    # Código que pode dar erro
    usuario_repositorio.inserir_usuario(usuario1) # Comentada pois os usuários já foram criados
except:
    # O que fazer caso aconteça um erro
    print("E-mail já cadastrado.")
# usuario_repositorio.inserir_usuario(usuario2)

usuarios = usuario_repositorio.obter_usuarios()
# print(usuarios)
# usuario_alterado = usuarios[0]
# usuario_alterado.nome = "Outro nome"
# usuario_alterado.email = "teste@gmail.com"

# usuario_repositorio.atualizar_usuario(usuario_alterado)
# usuario_removido = usuarios[0]
# usuario_repositorio.remover_usuario(usuario_removido)
