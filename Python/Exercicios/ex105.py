def notas (*turma, sit=False):
    """
    ->Notas retorna informacoes da turma de aluno
    param turma: recebe varias notas de alunos
    param sit: (opcional) indica se deve ou nao passar situacao da turma
    return: retorna informacoes como maior, menor notas e media da turma
    """
    soma = maior = menor = media = 0
    info = dict()
    for i in range(0, len(turma)):
        if i == 0:
            maior = menor = turma[0]
        if turma [i] > maior:
            maior = turma[i]
        if turma[i] < menor:
            menor = turma[i]
        soma += turma[i]
    media = soma/len(turma)
    info["qtdNotas"] = len(turma)
    info["maiorNota"] = maior
    info["menorNota"] = menor
    info["mediaTurma"] = media
    if sit:
        if media < 6:
            s = 'RUIM'
        elif 6 < media < 7:
            s = 'RAZOÁVEL'
        else:
            s = 'BOA'
        info["situacao"] = s
    return info


a = notas(6, 7.5, 8)
print(a)
a = notas(6, 7.5, 8, 10, sit=True)
print(a)
# Solução Guanabara
# def notas(*n, sit=False):
#   r = dict()
#   r['total'] = len(n)
#   r['maior'] = max(n)
#   r['menor'] = min(n)
#   r['média'] = sum(n)/len(n)
#   if sit:
#       if r['média'] >= 7:
#           r['situação'] = 'BOA'
#       elif r['média'] >= 5:
#           r['situação'] = 'RAZOÁVEL'
#       else:
#           r['situação'] = 'RUIM'
#   return r