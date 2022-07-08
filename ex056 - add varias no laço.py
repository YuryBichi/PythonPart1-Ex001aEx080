soma = 0
maioridade = 0
velho = ''
totalmulhernova = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M] Masculino ou [F] Feminino: ')).strip().upper()
    soma += idade
    if p == 1 and sexo == 'M':
        maioridade = idade
        velho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        totalmulhernova += 1



print('A media da idade do grupo  é {} !'.format(soma/4))
print('O homem mais velho é {} e sua idade é {} !'.format(velho.title(), maioridade))
print('O numero total de mulheres com menos de 20 anos é {} !'.format(totalmulhernova))

