km = float(input('Total de Kilometros(Km) percorridos?'))
qtd = int(input('Quantos dias ficou alugado?'))
print('O preço a pagar pelo aluguel é de R${:.2f}'.format((km*0.15)+(qtd*60)))