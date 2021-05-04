distancia = float(input('Informe a distância de sua viagem:'))
print('Analizando o preço a pagar ...')
if distancia <= 200:
    print('O valor à pagar é R${:.2f}'.format(distancia*0.5))
else:
    print('O valor à pagar é R${:.2f}'.format(distancia*0.45))
#SOLUÇÃO GUANABARA IF INLINE+++ preco = distancia*0.5 if distancia <= 200 else distancia * 0.45