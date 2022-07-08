n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
if n1 >= n2 >= n3:
    print('O numero {} é o maior e {} é o menor'.format(n1, n3))
elif n2 >= n1 >= n3:
    print('O Numero {} é o mior e {} é o menor'.format(n2, n3))
elif n2 >= n3 >= n1:
    print('O numero {} é o maior e o {} é menor'.format(n2, n1))
elif n3 >= n1 >= n2:
    print('O numero {} é o maior e {} é menor'.format(n3, n2))
elif n3 >= n2 >= n1:
    print('O numero {} é o maior e {} é o menor'.format(n3, n1))

'''
Uma das formas mais simples !!

primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))