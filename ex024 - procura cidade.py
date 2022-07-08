#entrada de dados cortando espaços nas extremidades e jogando tudo para maiusculo.
#desse modo é possivel achar a correspondecia independente da entrada do usuario.
c = str(input('Digite o nome de sua cidade: '.strip())).upper()

#entrada transformada em lista para poder encontrar santo comente na primeira parte do nome.
l = c.split()

#aqui crio uma condição onde ele me mostra true se achar 'santo' no primeiro item da lista, caso contrario false.
if  l[0] == 'SANTO':
    print('Existe Santo no primeiro nome!')
else:
    print('Não existe Santo no primeiro nome')
