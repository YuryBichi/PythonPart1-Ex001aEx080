import math
n = int(input('Digite um angulo: '))
# pego o valor em radiando e transformo em cosseno, seno e tangente #

c = math.cos(math.radians(n))
s = math.sin(math.radians(n))
t = math.tan(math.radians(n))

print('O cosseno de {:.2f} é'.format(c))
print('O seno de {:.2f} é'.format(s))
print('A tangente de {:.2f} é'.format(t))