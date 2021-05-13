sexo = ''
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Informe seu sexo (M/F):')).upper()
    if sexo == 'F' or sexo == 'M':
        break
    else:
        print('Entrada inválida! Apenas F/M')
        