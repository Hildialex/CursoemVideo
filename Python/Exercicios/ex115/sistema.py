from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome:')).strip()
        idade = leiaInt('Idade:')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do Sistema!...Até Logo!')
        break
    else:
        print('\033[31mOpção Inválida!\033[m')
    sleep(1)