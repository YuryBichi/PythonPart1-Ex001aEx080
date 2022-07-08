print('\033[;41mSoma em laço infinito!\033[m')
numero = cont = soma = 0

while True:
    cont += 1
    numero = int(input(f'\033[1;33mNumero {cont}: \033[m'))
    if numero == 999:
        break
    soma += numero

print(f'A soma dos numeros é {soma:-^10}')
