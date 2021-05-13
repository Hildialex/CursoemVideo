termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
n = 1
lista = [termo]
while n < 10:
    termo = termo + razao
    lista.append(termo)
    n += 1
print('Os 10 primeiros termos dessa P.A. são {}'.format(lista))