ret = float(input('Informe o primeiro comprimento:'))
ret1 = float(input('Informe o segundo comprimento:'))
ret2 = float(input('Informe o terceiro comprimento:'))
print('Analizando se as retas formam um trinângulo...')
if (ret < (ret1+ret2)) and (ret1 < (ret+ret2)) and (ret2 < (ret+ret1)):
    print('Elas FORMAM um triângulo!')
else:
    print('Elas NÂO FORMAM um trinângulo!')