numero = int(input('Informe um numero: '))
escolha = int(input('Menu de conversão:\n1 - Binario.\n2 - Octal.\n3 - Hexadecimal.\n'))
if escolha == 1:
    print('O numero {} em Binario é {} !'.format(numero, bin(numero)))
elif escolha == 2:
    print('O numero {} em Octal é {} !'.format(numero, oct(numero)))
elif escolha == 3:
    print('O numero {} em Hexadecimal é {} !'.format(numero, hex(numero)))
else:
    print('Opição invalida!')
