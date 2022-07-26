import Upgrade_banco_dados
import Dowgrade_Banco_de_dados
while True:
    try:
        print('-----------------------------')
        print('Menu para Migrations')
        print('1: Adicionar a tabela Endereço no banco de dados')
        print('2: Adicionar a tabela Teste para posterior downgrade')
        print('3: Remover a tabela Teste')
        print('4: sair')
        escolha=int(input("Escolha a opção que deseja"))

        if escolha == 1:
            Upgrade_banco_dados.upgrade()
            print('Tabela Endereco adicionada')
        elif escolha == 2:
            Dowgrade_Banco_de_dados.upgrade_tabela_teste()
            print('Tabela teste adicionada')
            print('Deseja remover a tabela Teste?')
            print('1: Sim')
            print('2: Não')
            escolha_remover=int(input('Escolha uma opção'))
            if escolha_remover ==1:
                Dowgrade_Banco_de_dados.downgrade_tabela_teste()
                print('Tabela teste removida')
        elif escolha==3:
            Dowgrade_Banco_de_dados.downgrade_tabela_teste()
            print('Tabela teste removida')
        elif escolha == 4:
            break
        else:
            print('Opção invalida')
    except:
        print('Opção não desponivel no momento')