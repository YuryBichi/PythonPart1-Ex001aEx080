print('---------------------\nSequência Fibonacci !\n---------------------')
mostrar = int(input('Quantos numeros deseja mostrar? '))

cont = fn = 1
resultado = rante = 0 + 0

while cont <= mostrar:
    print(resultado, end=' -> ' if cont < mostrar else ' FIM')

    cont += 1
    resultado = fn + rante
    fn = rante
    rante = resultado
