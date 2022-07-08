numero = int(input('Informe o numero fatorial: '))
cont = numero
fatorial = 1
print(f'Calculando {numero}! =', end=' ')
while cont > 0:
    print(f'{cont}', end=' ')
    print('x' if cont > 1 else '=', end=' ')
    fatorial *= cont
    cont -= 1
print(fatorial)
