i = soma = media = maior = menor = 0
resp = 's'
while resp == 's':
    num = int(input('Digite um número:'))    
    if i == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    i += 1
    soma += num
    media = soma/i
    resp = str(input('Deseja continuar?(s/n)')).lower()
print('A média dos {} valores digitados é: {}\nO maior valor é: {}\nO menor valor é: {}'.format(i, media,maior,menor))