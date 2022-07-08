#Entrada de dados
print('Digite o nome dos alunos!')
a1 = str(input('Primeiro aluno : '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1,a2, a3, a4]

#importo commando que embaralha lista
from random import shuffle
shuffle(lista)
print('A ordem de apresentação é : {}'.format(lista))
