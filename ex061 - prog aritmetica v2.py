print('-=-=-=-=-=-=--=-=-=-=-=-=-=-\nGerador de PA !\n-=-=-=-=-=-=--=-=-=-=-=-=-=-')
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))
cont = 1

while cont <= 10:
    termo = ptermo + (cont - 1) * razao

    print(termo, end=' -> ' if cont < 10 else ' -> FIM')
    cont += 1
