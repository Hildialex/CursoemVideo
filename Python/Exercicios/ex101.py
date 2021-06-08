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
# Solução Guanabara
# IMPORTAR COISAS DENTRO DA FUNÇÃO ECONOMIZA MEMÓRIA
# 
# def voto(ano):
#   from datetime import date
#   atual = date.today().year
#   idade = atual - ano
#   if idade < 16:
#       return f'Com {idade} anos: NÃO VOTA!'
#   elif 16 <= idade < 18 or idade > 65:
#       return f'Com {idade} anos: VOTO OPCIONAL!'
#   else: return f'Com {idade} anos: VOTO OBRIGATÒRIO!'