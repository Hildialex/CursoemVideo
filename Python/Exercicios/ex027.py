nome = str(input('Digite seu nome completo:')).strip()
novo = nome.split()
print('Primeiro Nome: {}\nÚltimo Nome: {}'.format(novo[0], novo[-1]))
