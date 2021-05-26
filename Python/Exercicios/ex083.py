expressao = str(input('Digite uma expressão:')).strip().upper()
expressao.split()
lista = list()
lista1 = list()
for palavra in expressao:
    for letra in palavra:
        if letra == '(':
            lista.append(letra)
        if letra == ')':
            lista1.append(letra)
if len(lista) == len(lista1):
    print('Expressão Correta!')
else:
    print('Expressão incorreta!')
    