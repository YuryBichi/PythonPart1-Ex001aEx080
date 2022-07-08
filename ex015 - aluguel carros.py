d = int(input('Dias que ficou com o carro: '))
km = int(input('Informe quantos km percorreu: '))
custo = (60 * d) + (km * 0.15)
print('O valor a ser pago é de R${:.2f}!'.format(custo))
