termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
n = 1
lista = [termo]
while n < 10:
    termo = termo + razao
    lista.append(termo)
    n += 1
print('Os 10 primeiros termos dessa P.A. são {}'.format(lista))
#*Solução Guanabara
# primeiro = int(input('Digite Um número'))
# termo = primeiro
# cont = 1
# while cont <= 10:
#   print('{}¬'.format(termo), end ='')
#   termo += razao
#   cont += 1
# #