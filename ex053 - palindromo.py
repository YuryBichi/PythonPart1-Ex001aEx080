#entrada dos dados
palavra = str(input('\033[1;32mDigite a palavra: ')).strip().upper()

#nova variavel com metodo para trocar os espaços
p1 = palavra.replace(' ', '')

#logica onde é comparado se a variavel é igual revertida
if p1 == p1[::-1]:
    print('Palindromo!')
else:
    print('Não palindromo!')