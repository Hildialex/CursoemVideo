print('\033[2;31mÉ UM PALÍNDROMO\033[m')
frase = str(input('Digite uma frase:')).lower()
lista = []
lista2 = []
s = 0
for i in range(0, len(frase)):
    if frase[i] != ' ':
        lista2.append(frase[i])
for i in range(len(frase)-1, -1, -1):
    if frase[i] != ' ':
        lista.append(frase[i])
for i in range(0, len(lista)):
    if lista2[i] == lista[i]:
        s += 1

if s == len(lista):
    print('\033[2;34mÉ PALÍNDROMO!\033[m')
else:
    print('\033[2;31mNÃO É PALÍNDROMO!\033[m')
#* Solução Guanabara
#   frase = str(input('Digite uma frase:')).strip().upper()
#   palavras = frase.split()
#   junto = ''.join(palavras)
#   inverso = ''
#   for letra in range(len(junto) -1, -1, -1):
#       inverso += junto[letra]
#   if inverso == junto:
#       print('É PALINDROMO!')
#   else:
#       print('NÃO É PALINDROMO!')
#    
#outra forma
#   inverso = junto[::-1]
#   ELIMINA O FOR, E VAI PRO IF DIRETO, ISSO É FATIAMENTO EM PYTHON
*#
