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
len