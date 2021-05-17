total = mil = barato = cont = 0
nome = ''
while True:
    print('#*#*#*#*#SUPER-PYTHON*#*#*#')
    prod = str(input('Informe o nome do produto:')).strip()
    preco = float(input('Informe o preço R$'))
    total += preco
    if cont == 0:
        barato = preco
        nome = prod
    if preco > 1000:
        mil += 1
        if preco < barato:
            nome = prod
    elif preco < barato:
        nome = prod
    resp = str(input('Deseja cadastrar mais?')).strip().upper()
    while resp not in 'SsNn':
        resp = str(input('Deseja cadastrar mais?')).strip().upper()
    cont += 1
    if resp == 'N':
        break
print(f'O total da compra R${total:.2f}.\n{mil} produtos acima de R$1000,00.\n{nome.upper()} é o produto mais barato custando R${barato:.2f}.')
