contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20:'))
    if num < 0 or num > 20:
        print('Tente novamente')
        num = int(input('Digite um número entre 0 e 20:'))
    else:
        print(f'Você digitou o número {contagem[num]}')

#* Solução Guanabara
#   while True:
#       num = int(input('Digite um número:))
#       if 0 <= num <= 20:
#           break
#       print('Tente novamente', end=' ')
#  # 