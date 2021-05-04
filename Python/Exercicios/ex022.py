nome = str(input('Digite seu nome completo:')).strip()
novonome = nome.count(' ')
primeiro = nome.split()
qtdnome = len(nome) - novonome
print('Nome com letras maiúculas: {}'.format(nome.upper()))
print('Nome com letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(qtdnome))
print('Quantidade letras primeiro nome: {}'.format(len(primeiro[0])))

#Guanabara print('Qantidade primeiro:{}'.format(nome.find(' ')))