#Usando FOR

n = int(input('Informe o numero: '))
for c in range(1, 11):
	print('{} x {} = {}'.format(n, c, n*c))

#Usando While
n = int(input('Digite um numero: '))
cont = 1
while cont <= 10:
	print(f'{n} x {cont} = ',n*cont)
	cont = cont +1
print('FIM')
