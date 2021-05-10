print('\033[33mALÉM DO PESO\033[m')
menor = 0
maior = 0
lista = []
for i in range(0, 5):
    peso = float(input('Digite seu peso (Kg):'))
    lista.append(peso)
menor = min(lista)
maior = max(lista)
print('\nO mais pesado é: {:.2f}Kg\nO mais leve é {:.2f}Kg'.format(maior, menor))
#* Solução Guanabara
#   maior = 0
#   menor = 0
#   for i in range(1,6):
#       peso = float(input('Peso da pessoa:'))
#       if i == 1:
#           maior = i
#           menor = i
#       else:
#           if peso > maior:
#               maior = peso
#           if peso < menor:
#               menor = peso
#   print('O maior peso {:.2f}\nO menor é {:.2f}'.format(maior, menor))
#  *#