from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os 
from time import sleep
from datetime import datetime

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)


while True:
    os.system("cls||clear")
    print("===Menu Principal===")
    print(repository.menu_principal())
    opcao = input(":")
    match opcao:
        case '1':
            while True:
                for i in range (1):
                    os.system("cls||clear")
                    print("===Cadastro de funcionario===")
                    cpf = input("CPF: ")
                    nome = input("Nome: ")
                    sobrenome = input("Sobrenome: ")
                    idade = int(input("Idade: "))
                    email = input("E-mail: ")
                    senha = input("Senha: ")
                    admissao = datetime.now()
                    altura = float(input("Altura: "))
                    peso = float(input("Peso: "))

                    service.criando_usuario(cpf, nome,sobrenome, idade, email, senha, admissao, altura, peso)

                    print("\n===Listando usuarios Cadastrados===")

        case '2':
            lista_funcionarios = service.listar_usuarios()
            for usuario in lista_funcionarios:
                print(f"Nome:{usuario.nome} {usuario.sobrenome} 0\nEmail:{usuario.email}\nAdmissão: {usuario.admissao}") 
                sleep(5)
        case '3':
            funcionario = int(input("Informe o CPF do funcionario: "))
            repository.excluir_usuario(repository.pesquisar_usuario(funcionario))
            print("===Demissão efetuada com sucesso===")

        




