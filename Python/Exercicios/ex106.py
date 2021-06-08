from time import sleep
def ajuda(frase):
    return f'\033[1:31:40m {help(frase)}'

def linha(tam):
    li = len(tam) + 4
    for i in range(0, li):
        print('~', end='')
    print()
    print(' ',tam)
    for i in range(0, li):
        print('~', end='')
    print()

while True:
    print('\033[1:30:42m')
    linha("SISTEMA DE AJUDA PYHELP")
    print('\033[m')
    sleep(0.5)
    fra = str(input('Função ou Biblioteca-> ')).strip().lower()
    sleep(0.5)
    if fra != 'fim':
        print('\033[1:30:45m', end='')
        linha("Acessando o manual de comando")
        print(f"'{fra}'\033[m")
        print(ajuda(fra))
    else:
        break
# Solução Guanabara
# ESSE NÂO TERMINEI
# c = ('\033[m',        #sem cor
#       '\033[0:30:41m',#1-vermelho
#       '\033[0:30:42m',#2-verde
#       '\033[0:30:44m',#3-azul
#       '\033[0:30:45m',#4-roxo
#       '\033[7:30m'    #5-branco
#       )
# def titulo(msg, cor=0):
#   tam = len(msg) + 4
#   print(c[cor], end='')
#   print('~' * tam)
#   print(f'  {msg}')
#   print('~' * tam)
#   print(c[0], end='')
#
# def ajuda(com):
#   titulo(f'ACESSANDO O MANUAL DO COMANDO \'{com}\'', 4)
#   print(c[5], end='')
#   help(com)
#   print(c[0], end='')
# 
# comando = '' 
# while True:
#   titulo('SISTEMA DE AJUDA PYHELP', 1)
#   comando = str(input('Função ou Biblioteca ->'))
#   if comando.upper() == 'FIM':
#       break
#   else:
#       ajuda(comando)
# titulo('ATÉ LOGO', 1)