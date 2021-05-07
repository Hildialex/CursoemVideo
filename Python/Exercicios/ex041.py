from datetime import date
print('\033[30;45mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
nasc = int(input('Informe seu ano da nascimento(AAAA):'))
atual = date.today()
idade = atual.year - nasc
if idade <= 9:
    print('Nadador \033[34mMIRIM\033[m')
elif idade <= 14:
    print('Nadador \033[34mINFANTIL\033[m')
elif idade <= 19:
    print('Nadador \033[34mJUNIOR\033[m')
elif idade <= 20:
    print('Nadador \033[34mSÊNIOR\033[m')
else:
    print('Nadador \033[34mMASTER\033[m')