def leiaInt(str):
    """
    -> Verifica se o valor informado e numero
    """
    num = int(input(str))
    if num:
        return num
    else:
        return 'ERRO! Digite um número inteiro válido.'
n = leiaInt('Digite um número:')
print(f'O número digitado foi {n}')