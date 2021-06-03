from time import sleep
def maior(*var):
    print('=-'*20)
    print('Analisando os valores passados...')
    maior = cont = 0
    for i in var:
        print(f'{i}', end=' ', flush=True)
        sleep(0.5)
        if i > maior:
            maior = i
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
maior(9,56,47,1)
maior(9)
maior(9,5,12)
maior()