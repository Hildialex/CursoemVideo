palavras = ('abacate', 'amor', 'paixao', 'sossego', 'carinho', 'deus', 'jesus', 'palavra', 'atraso', 'querer', 'deixar', 'ir', 'aprender', 'python', 'programar')
for palavra in palavras:
    vogal = ''
    for letra in palavra:
        if letra in 'aeiou':
            vogal += ' '
            vogal += letra
    print(f'A palavra: {palavra}, tem as vogais: {vogal}')