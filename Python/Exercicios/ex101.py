from datetime import datetime
def voto(nasc):
    idade = datetime.now().year - nasc
    if idade < 18:
        return f'Com {idade} anos, NÃO VOTA!'
    elif idade > 65:
        return f'Com {idade} anos, VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO!'

pes = int(input('Digite o ano de nascimento:'))
print(voto(pes))