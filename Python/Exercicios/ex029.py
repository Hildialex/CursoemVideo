velo = float(input('Informe a velocidade do carro:'))
if velo > 80:
    print('Limite de velocidade é de 80 Km/h')
    print('Você foi multado em R${:.2f}'.format((velo-80)*7.0))

print('Você não foi multado!')
print('Tenha um bom dia!')
