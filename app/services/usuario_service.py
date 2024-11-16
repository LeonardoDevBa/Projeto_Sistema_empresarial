from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime

class UsuarioService:
    def __init__(self,repository:UsuarioRepository):
        self.repository = repository
    
    def criando_usuario(self,cpf:str, nome: str,sobrenome:str ,idade:int, email:str, senha:str, admissao:datetime, altura:float, peso:float):
        try:
            usuario = Usuario(cpf=cpf,nome=nome,sobrenome=sobrenome,idade=idade,email=email,senha=senha,admissao=admissao,altura=altura,peso=peso)

            usuario_cadastrado = self.repository.pesquisar_usuario(usuario.cpf)

            if usuario_cadastrado:
                print("Usuário já cadastrado!")
                return
            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
        
    def listar_usuarios(self):
        return self.repository.lista_usuarios()