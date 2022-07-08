numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero: '))
while True:
    escolha = int(input('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
                        '\n[1] Soma'
                        '\n[2] Multiplica'
                        '\n[3] Maior'
                        '\n[4] Novos numeros'
                        '\n[5] Sair do programa'
                        '\n----> Qual opção?'))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    if escolha == 1:
        print(f'Soma de {numero1} + {numero2} =', numero1+numero2)
    elif escolha == 2:
        print(f'Multiplicação de {numero1} x {numero2} =', numero1*numero2)
    elif escolha == 3:
        lista = [numero1, numero2]
        print(f'O maior numero é {max(lista)}!')
    elif escolha == 4:
        numero1 = int(input('Primeiro numero: '))
        numero2 = int(input('Segundo numero: '))
    elif escolha == 5:
        print('Programa encerrado!')
        break
    from time import sleep
    sleep(5)
print('Volte sempre!')
