from functions.functions_app import menu_principal, login_1,cadastrando_empresa,verificando_cadastro_empresa , cadastrando_funcionario, verificando_cadastro, editando_dados,desligamento, login
from os import system
from time import sleep
while True:
    system("cls||clear")
    print(login_1())
    opcao1 = input(": ")
    
    match opcao1:
        case '1':
            cadastrando_empresa()
            sleep(2)
        case '2':
            verificando_cadastro_empresa()
    while True:
        print(menu_principal())
        opcao = input(": ")
        match opcao:
            case '1':
                while True:
                    system("cls||clear")
                    print("=== | CADASTRO | === ")
                    cadastrando_funcionario()
                    opcao = int(input("Deseja Adicionar outro funcionario ? \n1-Sim\n2-Não"))
                    if opcao == 2:
                        break       
            case '2':
                system("cls||clear")
                print("=== | CHECAGEM | === ")
                verificando_cadastro()
                sleep(5)
            case '3':
                system("cls||clear")
                print("=== | EDIÇÃO | === ")
                editando_dados()
                sleep(3)
            case '4':
                system("cls||clear")
                print("=== | DEMISSÃO | === ")
                desligamento()
            case '5':
                system("cls||clear")
                login()
                sleep(3)
            case '6':
                break
            