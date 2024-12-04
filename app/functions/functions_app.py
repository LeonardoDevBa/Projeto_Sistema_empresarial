from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from config.database import Session
from cryptography.fernet import Fernet
import pwinput as pin

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)

def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    return chave

chave = carregar_chave()
cipher = Fernet(chave)

def senha():
    senha = pin.pwinput("Senha: ")
    senha_seg = criptografia(senha)
    return senha_seg

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
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

def login_1():
    menu ="""========| SYSTEM OF |========

1 - CADASTRAR EMPRESA
2 - EFETUAR LOGIN
"""
    return menu

def menu_principal():
    menu ="""
========| MENU PRINCIPAL |========

1 - CADASTRAR FUNCIONARIO
2 - CHECAR CADASTRO DE FUNCIONARIO
3 - EDITAR CADASTRO DE FUNCIONARIO
4 - DEMISSAO DE FUNCIONARIO
6 - SAIR
"""  
    return menu

def cadastrando_funcionario():
    CPF = input("CPF: ")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")
    admissao = datetime.now()
    rg = input("RG: ")

    service.criando_usuario(CPF, nome, sobrenome, idade, email, admissao, rg)

def cadastrando_empresa():
    nome = input("Razão social: ")
    cnpj = input("CNPJ: ")
    responsavel = input("Dono: ")
    email = input("Email: ")
    senha_crip = senha()

    service.criando_empresa(nome, cnpj, responsavel, email, senha_crip)

def verificando_cadastro():
    funcionario_cpf = input("Informe o CPF do funcionario: ")
    funcionario = repository.pesquisar_usuario(funcionario_cpf)
    if funcionario:
        print(f"Nome: {funcionario.nome} {funcionario.sobrenome}")
        print(f"RG: {funcionario.rg}")
        print(f"Email: {funcionario.email}")
        print(f"Idade: {funcionario.idade}")
        print(f"Admissão: {funcionario.admissao}")
    else:
        print("Funcionário não encontrado!")

def editando_dados():
    cpf = input("Informe o CPF do funcionário que deseja editar: ")
    funcionario = repository.pesquisar_usuario(cpf)

    if funcionario:
        print("=== Dados Atuais ===")
        print(f"Nome: {funcionario.nome}")
        print(f"Sobrenome: {funcionario.sobrenome}")
        print(f"Idade: {funcionario.idade}")
        print(f"Email: {funcionario.email}")
        print(f"Rg: {funcionario.rg}")
        print("\n=== Insira os novos dados (ou pressione Enter para manter o atual) ===")
        nome = input("Novo Nome: ") or funcionario.nome
        sobrenome = input("Novo Sobrenome: ") or funcionario.sobrenome
        idade = input("Nova Idade: ")
        idade = int(idade) if idade else funcionario.idade
        email = input("Novo Email: ") or funcionario.email
        funcionario.nome = nome
        funcionario.sobrenome = sobrenome
        funcionario.idade = idade
        funcionario.email = email
        repository.atualizar_cadastro(funcionario)
        print("\n=== Dados atualizados com sucesso! ===")
    else:
        print("Funcionário não encontrado!")
    
def desligamento():
    funcionario_cpf = input("Informe o CPF do funcionario: ")
    funcionario = repository.pesquisar_usuario(funcionario_cpf)
    if funcionario:
        repository.excluir_usuario(funcionario)
        print("=== Demissão efetuada com sucesso ===")
    else:
        print("Funcionário não encontrado!")

def login():
    cpf = input("CPF: ")
    senha = input("Senha: ")
    funcionario = repository.pesquisar_usuario(cpf)
    if funcionario and senha == descriptografia(funcionario.senha):
        print("=== Login efetuado com sucesso ===")
    else:
        print("=== Login ou senha incorretos ===")

def verificando_cadastro_empresa():
    while True:
        empresa_email = input("Informe o E-mail da empresa: ") 
        empresa = repository.pesquisar_empresa(empresa_email)
        if empresa:
            print("Email correto")
            senha_dig = pin.pwinput("Digite a senha: ")
            if senha_dig == descriptografia(empresa.senha):
                print("LOGIN EFETUADO COM SUCESSO")
                break
        else:
            print("Empresa não encontrada. Tente novamente.")
    return empresa