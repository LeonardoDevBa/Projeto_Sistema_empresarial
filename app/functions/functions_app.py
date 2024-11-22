from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from config.database import Session
from cryptography.fernet import Fernet

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)

def senha ():
    senha = input("Senha: ")
    senha_seg = criptografia(senha)
    return senha_seg

"""
def cpf ():
    cpf = input("CPF: ")
    cpf_seg = criptografia(cpf)
    return cpf_seg
"""    
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    return chave

def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    return chave

def criptografia(texto):
    texto_criptografado = cipher.encrypt(texto.encode("utf-8"))
    return texto_criptografado

def descriptografia(texto):
    if texto is None:
        raise ValueError("Senha não pode ser None!")
    if isinstance(texto, str):
        texto = texto.encode("utf-8")
    try:
        return cipher.decrypt(texto).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Erro na descriptografia: {e}")
    
def menu_principal ():
    menu="""
========| MENU PRINCIPAL |========

1 - CADASTRAR FUNCIONARIO
2 - CHECAR CADASTRO DE FUNCIONARIO
3 - EDITAR CADASTRO DE FUNCIONARIO
4 - DEMISSAO DE FUNCIONARIO
5 - FAZER LOGIN DE FUNCIONARIO
6 - SAIR
"""  
    return menu

def cadastrando_funcionario():
    CPF = input("CPF: ")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")
    Senha = senha()
    admissao = datetime.now()
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    service.criando_usuario(CPF, nome,sobrenome, idade, email, Senha, admissao, altura, peso)

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
    
def login():
    cpf = input("CPF: ")
    senha = input("Senha: ")
    funcionario =repository.pesquisar_usuario(cpf)
    if funcionario and senha == descriptografia(funcionario.senha):
        print("===Login efetuado com sucesso===")
    else:
        print("===Login ou senha incorretos===")
    
chave = carregar_chave()  
cipher = Fernet(chave)
