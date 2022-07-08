km = int(input('Informe a distancia em km: '))
if km <= 200:
    preço = km * 0.50

else:
    preço = km * 0.45
print('O custo da viagem é de R${}'.format(preço))
