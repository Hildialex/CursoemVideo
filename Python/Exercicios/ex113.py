def leiaInt(msg):
    try:
        num = int(input(msg))
    except (ValueError): 
        print('\033[0;31mERRO: por favor informe um número inteiro válido!\033[m')
    except (KeyboardInterrupt):
        print()
        print('\033[0;31mUsuário não continuou!\033[m')
        num = 0
    finally:
        return num
def leiaFloat(msg):
    try: 
        num = float(input('Número Real:'))
    except (ValueError):
        print('\033[0;31mERRO: por favor, digite um número real válido!\033[m')
    except (KeyboardInterrupt):
        print()
        print('\033[0;31mUsuário não continuou o processo!\033[m')
        num = 0
    finally:
        return num

a = leiaInt('Número Inteiro:')
b = leiaFloat('Número Real:')
print(f'O número inteiro digitado foi {a}, o número real digitado foi {b}')
