n = str(input('Digite o nome: ')).strip().upper()
lista = n.split()
if 'SILVA' in lista:
    print('Existe Silva no nome!')
else:
    print('Nao existe Silva no nome!')