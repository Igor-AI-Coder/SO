import os
import socket


def criardir (nome):
    try:
        x = os.mkdir(nome)
        return x
    except FileNotFoundError:
        return ('Error 90000000000')
    except PermissionError:
        return ('Error 901234')
def removedir(nome):
    try:
        c = os.rmdir(nome)
        return c
    except FileNotFoundError:
        return ('Error 90000000000')
    except PermissionError:
        return ('Error 901234')

def copia(nome, nome_novo):
    try:
        s = os.system(f'copy {(nome)} {(nome_novo)} ')
        return s
    except FileNotFoundError:
        return ('Error 90000000000')
    except PermissionError:
        return ('Error 901234')

def renomear(nome, nome_novo):
    try:
        l = os.rename(nome, nome_novo)
        return l
    except FileNotFoundError:
        return ('Error 90000000000')
    except PermissionError:
        return ('Error 901234')
    except FileExistsError:
        return (f'Erro 9012 -> {nome_novo} já existe')
def cd(nome): 
    try:
        a = os.chdir(nome)
        return f"Diretório alterado para: {os.getcwd()}"
    except FileNotFoundError:
        return ('Error 90000000000')
    except TypeError:
        return ('Error 0923495234')
def list_dir_atual() -> str:
    return f"Diretório atual: {os.getcwd()}"
