#Entrada de dados
n = str(input('Digite o nome: '))

#Saida em maiusculo
print('O nome em maiusculo', n.upper())

#Saida em minusculo
print('O nome em minusculo', n.lower())

#Trocando os espaços por vazio
nr = n.replace(' ','')

#Saida quantidade de letras
print('Quantidade de letras no nome', len(nr))

#Tornando entrada uma lista e saida quantidade letras 1° nome
p = n.split()
print('Quantidade de letras primeiro nome', len(p[0]))