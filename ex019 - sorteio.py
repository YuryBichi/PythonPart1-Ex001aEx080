# Entradas a serem trabalhadas
a1 = input('Aluno 1:  ')
a2 = input('Aluno 2:  ')
a3 = input('Aluno 3:  ')
a4 = input('Aluno 4:  ')

# Criei uma lista com as entradas
lista = [a1, a2, a3, a4]

# Usei o medoto para sortear um escolhido na lista
from random import choice
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))
