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
#Solução Guanabara
# pilha = []
# for simb in expre:
#   if simb == '(':
#      pilha.append('(')
#   elif simb == ')':
#      if len(pilha) > 0:   
#          pilha.pop()
#      else:
#          pilha.append(')')
#          break
# if len(pilha) == 0:
#   print('Expressão Válida!')
# else:
#   print('Expressão Inválida!')
# #