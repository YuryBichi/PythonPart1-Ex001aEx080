lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    if str(input('Quer continuar? [S/N] ')).upper().strip() == 'N':
        break

print(f'Você digitou {len(lista)} numeros e a média foi de {sum(lista)/len(lista):.2f} !\n'
      f'O maior valor foi {max(lista)} e o menor foi {min(lista)} !')
