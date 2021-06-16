from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        #wt+ cria um arquivo se ele não existir por causa do +
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve erro na criação do arquivo')
    else:
        print('Criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO ao ler o arquivo!\033[m')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split()
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<30}{dado[2]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='<desconhecido>', idade =0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome} ; {idade}\n')
        except:
            print('Houve um ERRO ao escrever no arquivo!')
        else:
            print(f'Novo registro, {nome} adicionado!')
            a.close()