#entrada dos dados já strip e upper.
f = str(input('Digite uma frase: ')).strip().upper()

#Primeiro na saida conto a quatidade, depois uma procura e por fim uma procura da direita para esquerda.
print('Existem {} letras "A" na frase !'.format(f.count('A')))
print('O primeiro "A" está na posição {} !'.format(f.find('A')))
print('O ultimo "A" esta na posição {} !'.format(f.rfind('A')))
