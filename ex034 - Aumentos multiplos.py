s = float(input('Informe salario: R$ '))
if s >= 1250:
    a = '10%'
    aumento = s * 1.10
else:
    a = '15%'
    aumento = s * 1.15
print('Seu aumento salarial foi de {} e seu salario atual é R${:.2f}!'.format(a, aumento))
