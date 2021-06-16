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
# Solução Guanabara
# def leiaInt(msg):
#   while True:
#       try:
#           n = int(input(msg))
#       except (ValueError, TypeError):
#           print('ERRO: por favor digite um número inteiro válido!')
#           continue
#       except KeyboardInterrupt:
#           print('Usuário preferiu não digitar')
#           return 0
#       else:
#           return n
# 
# def leiaFloat(msg):
#   while True:
#       try:
#           n = float(input(msg))
#       except (ValueError, TypeError):
#           print('ERRO: por favor digite um número real válido!')
#           continue
#       except KeyboardInterrupt:
#           print('Usuário preferiu não digitar')
#           return 0
#       else:
#           return n
# DAR O RETURN NO EXCEPT EVITA O APARECIMENTO DE ERRO. 
# 
#