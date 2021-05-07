print('\033[7;30;40mCalculando Média!\033[m')
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
if media < 5.0:
    print('Sua média é {}, você foi {}REPROVADO{}'.format(media, '\033[2;31m', '\033[m'))
elif media >=5.0 and media <= 6.9:
    print('Sua média é {}, você está de {}RECUPERAÇÂO{}'.format(media, '\033[2;32m', '\033[m'))
else:
    print('Sua média é {}, você está {}APROVADO{}'.format(media, '\033[2;36m', '\033[m'))