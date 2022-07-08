a = float(input('Primeiro numero: '))
b = float(input('Segundo numero: '))
c = float(input('Terceiro numero: '))

lo = (a - b) < c < a + b and (b - c) < a < b + c and (c - a) < b < c + a
if lo == True:
    lo = 'Forma triangulo'
    if a == b == c:
        print('Equilátero')
    elif a == b or a == c or b == c:
        print('Isóscelis')
    elif a != b != c:
        print('Escaleno')
else:
    lo = 'Não forma triangulo'
print('Os segmentos {}'.format(lo))
