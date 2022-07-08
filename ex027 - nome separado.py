n = str(input('Digite o nome: ')).strip().title()
lista = n.split()
print('O primeiro nome é', lista[0])
print('O ultimo nome é', lista.pop())
