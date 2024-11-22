from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from config.database import Session
from cryptography.fernet import Fernet

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    return chave

def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    return chave

def criptografia_senha():
    senha = input("Senha: ")
    senha_criptografada = cipher.encrypt(senha.encode("utf-8"))
    return senha_criptografada

def descriptografia_senha(senha):
    if senha is None:
        raise ValueError("Senha não pode ser None!")
    
    if isinstance(senha, str):
        senha = senha.encode("utf-8")

    try:

        senha_descriptografada = cipher.decrypt(senha).decode("utf-8")
        return senha_descriptografada
    except cryptography.fernet.InvalidToken:
        raise ValueError("Erro: O token criptografado é inválido ou foi corrompido.")
    except Exception as e:
        raise ValueError(f"Erro na descriptografia: {e}")

def descriptografia_senha(senha):
    if senha is None:
        raise ValueError("Senha não pode ser None!")
    if isinstance(senha, str):
        senha = senha.encode("utf-8")
    try:
        return cipher.decrypt(senha).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Erro na descriptografia: {e}")
    
def menu_principal ():
    menu="""
========| MENU PRINCIPAL |========

1 - CADASTRAR FUNCIONARIO
2 - CHECAR CADASTRO DE FUNCIONARIO
3 - EDITAR CADASTRO DE FUNCIONARIO
4 - DEMISSAO DE FUNCIONARIO
5 - SAIR
"""  
    return menu

def cadastrando_funcionario():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")
    senha = criptografia_senha()
    admissao = datetime.now()
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    service.criando_usuario(cpf, nome,sobrenome, idade, email, senha, admissao, altura, peso)

def verificando_cadastro():
    funcionario1 = int(input("Informe o CPF do funcionario: "))
    funcionario = repository.pesquisar_usuario(funcionario1)
    print(f"Nome:{funcionario.nome} {funcionario.sobrenome} ")
    print(f"Email:{funcionario.email}")
    print(f"Idade: {funcionario.idade}")
    print(f"Admissão: {funcionario.admissao}")

def editando_dados():
    cpf = input("Informe o CPF do funcionário que deseja editar: ")
    funcionario = repository.pesquisar_usuario(cpf)

    if funcionario:
        print("=== Dados Atuais ===")
        print(f"Nome: {funcionario.nome}")
        print(f"Sobrenome: {funcionario.sobrenome}")
        print(f"Idade: {funcionario.idade}")
        print(f"Email: {funcionario.email}")
        print(f"Altura: {funcionario.altura}")
        print(f"Peso: {funcionario.peso}")
        print("\n=== Insira os novos dados (ou pressione Enter para manter o atual) ===")
        nome = input("Novo Nome: ") or funcionario.nome
        sobrenome = input("Novo Sobrenome: ") or funcionario.sobrenome
        idade = input("Nova Idade: ")
        idade = int(idade) if idade else funcionario.idade
        email = input("Novo Email: ") or funcionario.email
        altura = input("Nova Altura: ")
        altura = float(altura) if altura else funcionario.altura
        peso = input("Novo Peso: ")
        peso = float(peso) if peso else funcionario.peso
        funcionario.nome = nome
        funcionario.sobrenome = sobrenome
        funcionario.idade = idade
        funcionario.email = email
        funcionario.altura = altura
        funcionario.peso = peso
        repository.atualizar_cadastro(funcionario)
        print("\n=== Dados atualizados com sucesso! ===")
    else:
        print("Funcionário não encontrado!")
    
def desligamento():
    funcionario1 = int(input("Informe o CPF do funcionario: "))
    funcionario = repository.pesquisar_usuario(funcionario1)
    repository.excluir_usuario(funcionario)
    print("===Demissão efetuada com sucesso===")
    
def senha ():
    cpf = input("informe seu CPF: ")
    funcionario = repository.pesquisar_usuario(cpf)
    senha = funcionario.senha
    senha_descrip = descriptografia_senha(senha)
    return senha_descrip
    
chave = carregar_chave()  
cipher = Fernet(chave)
