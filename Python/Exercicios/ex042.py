print('\033[7;31;40mTIPOS DE TRIÂNGULOS\033[m')
ret = float(input('Informe o primeiro comprimento:'))
ret1 = float(input('Informe o segundo comprimento:'))
ret2 = float(input('Informe o terceiro comprimento:'))
print('Analizando se as retas formam um triângulo...')
if (ret < (ret1+ret2)) and (ret1 < (ret+ret2)) and (ret2 < (ret+ret1)):
    print('Elas formam um triângulo!')
    if ret == ret1 and ret == ret2:
        print('Triangulo Equilátero formado!')
    elif ret == ret1 or ret1 == ret2 or ret2 == ret:
        print('Trângulo Isósceles formado')
    else:
        print('Triângulo Escaleno formado')
else:
    print('Elas NÂO FORMAM um trinângulo!')
