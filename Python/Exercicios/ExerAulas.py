#tuplas são imutáveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#isso dá erro lanche[1] ='Arroz'
print(lanche[-1])
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
#Sem precisar da posição do elemento os outros quando precisar
for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
#para ordenar em alfabeto
print(sorted(lanche))
a = (2,1,2,3)
b = (12,3,4)
c = a + b
print(c)
#Diferente do anterior
c = b + a
print(c)
#mostra a posição do item na tupla
print(c.index(12))
#mostra a posição do item a partir da posição 1
print(c.index(3, 1))
#para apagar qualquer variavel
del(lanche)
#Quantidade de vezes que aparece o elemento
print(c.count(3))


#lista podem ser modificadas
lanche = []
#adicionar
lanche.append('Cachorro Quente')
lanche.insert(0,'Suco')
#apagar
del lanche[1]
lanche.pop(0)
lanche.insert(0,'Suco')
lanche.remove('Suco')
#criar lista com range
valores = list(range(4,11))
#ordenar
valores.sort()
#inverso
valores.sort(reverse=True)


#dicionario
lanche = {}
lanche['nome'] = 'Hamburguer'
lanche['preco'] = 12.10
print(lanche.items())

pessoas = {'nome': 'Alex', 'idade': 27, 'sexo': 'm'}
print(pessoas.values())
print(pessoas.keys())
#Isso é como o enumerate em tuplas e listas
for k,v in pessoas.items():
    print(f'O {k} é {v}')
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
   #Assim da erro pq cria um link nao mudando o valor brasil.append(estado)
   #Assim da erro pq não copia brasil.append(estado[:])
    brasil.append(estado.copy())
print(brasil)
#FUNÇOES toda passagem de parametro é por referencia
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A some de A+B = {s}')

soma(4,5)
soma(a=4, b=5)
#O * significa que ele vai desempacotar, para receber varios parametros
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são {tam} números')

contador(2,3,4,5)
contador(9,9)
contador(9)

def dobra(lst):
    pos = 0
    while pos > len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2,3, 4, 5]
dobra(valores)
#Interactive Help = é uma maneira de usar uma ajuda
help(print)
help(input)
print(input.__doc__)
#DocStrings = é como um manual para explicar o comando
def contador(i,f,p):
    """
    Aqui inicia a docString
    -> Faz uma contagem e mostra na tela
    param i : inicio da contagem
    param f: fim da contagem
    param p: passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')
help(contador)
#PARAMETROS OPCIONAIS = colocando c=0 estou dizendo que é opcional, sendo assim na chamada da função posso ou nao informa-lo, todos podem ser opcionais tbm
#def somar(a=0,b=0,c=0)
def somar(a,b,c=0):
    s = a+b+c
    print(f'A soma vale{s}')
#ESCOPO DE VARIÁVEIS = local onde a variavel vai existir e onde não vai
def fatorial(num=0):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Número:'))
print(f'Os resultados são {n}')

#AULA 23
#Pode-se utilizar try, except sem else e finally, também com apenas except na frente dele criamos a variavel que recebe o erro
try:
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except KeyboardInterrupt:
    print('Usuário não quis continuar')
except Exception as erro:
    print(f'O erro foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte Sempre!')

