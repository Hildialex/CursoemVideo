lg = float(input('Largura da parede:'))
al = float(input('Altura da parede:'))
latas = (lg*al)/2
print('Sua parede de {:.2f}X{:.2f} possui {:.2f}m²\nSerá necessário {}litros de tinta'.format(lg, al, lg*al, latas))