n = int(input('Digite um numero de 1 a 5: '))
from random import choice
r = [1, 2, 3, 4, 5]
e = choice(r)
print('O computador escolheu {} !'.format(e))
print('Parabens' if e == n else 'Errou')
