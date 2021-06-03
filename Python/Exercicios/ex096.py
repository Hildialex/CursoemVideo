def area(larg, comp):
    print(f'A área de um terreno {larg}x{comp} é de {larg*comp}m²')
print('-'*20)
print('Controle de Terrenos')
print('-'*20)
la = float(input('Largura do terreno:'))
co = float(input('Comprimento do terreno:')) 
area(la, co)