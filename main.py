import os
import socket
import HW as cmd
while True:
    comando = input('\nO que você gostaria de fazer?\n'
                    '1 - Entrar em um diretório\n'
                    '2 - Criar um diretório\n'
                    '3 - Remover um diretório\n'
                    '4 - Cópia de um diretório\n'
                    '5 - Renomear um diretório\n'
                    '6 - Listar diretório atual\n'
                    '7 - Sair\n'
                    'Opção: ')
    if comando == '1':
        cd = input('Nome do diretório: ')
        print(cmd.cd(cd))
    if comando == '2':
        mkdir = input('Nome do diretório a ser criado: ')
        print(cmd.criardir(mkdir))
    if comando == '3':
        rmv = input('Nome do diretório a ser removido: ')
        print(cmd.removedir(rmv))
    if comando == '4':
        nome_antigo = input('Nome do diretório a ser copiado: ')
        nome_novo = input('Nome do novo diretório: ')
        print(cmd.copia(nome_antigo, nome_novo))
    if comando == '5':
        ren = input('Nome do diretório a ser renomeado: ')
        ren_novo = input('Nome que vai substituir o antigo: ')
        print(cmd.renomear(ren, ren_novo))
    if comando == '6':
        print(cmd.list_dir_atual())
    if comando == '7':
        print('Saindo')
        break