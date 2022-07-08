s = 0
for c in range(0, 6):
    n = int(input('Informe um numero: '))
    if n % 2 == 0:
        s += n
print('A soma dos pares é {} !'.format(s))