print('\033[35mPROGRESSÃO ARITMÉTICA\033[m')
pt = int(input('Digite o primeiro termo da P.A.:'))
razao = int(input('Digite a razão:'))
s = pt
for i in range(1, 11):
    print('{}º termo da P.A: {}'.format(i, s))
    s += razao

#*Solucao Guanabara
# primeiro  = int(input('Digite o 1º termo:'))
# razao = int(input('A razão:'))
# decimo = primeiro + (10-1) * razao
# for c in range(primeiro, decimo+razao, razao):
#   print('{}'.format(c), end='¬ ')
# print('ACABOU')
*#