print('CALCULANDO IMC')
peso = float(input('Informe seu peso:'))
alt = float(input('Informe sua altura:'))
imc = peso / (alt**2)
if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade Mórbida')