ano = int(input('Informe o ano a ser analizado:'))
print('Analizando se é Bissexto')
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano {} informado É Bissexto!'.format(ano))
else:
    print('O ano {} informado NÃO É Bissexto!'.format(ano))
# SOLUÇÃO GUANABARA
# from datetime import date
# if ano == 0:
#   ano = date.today().year