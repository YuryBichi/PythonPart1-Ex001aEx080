l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
m2 = l * a
t = m2 / 2
print('A dimensão da parede é {}x{} e sua área é {:.2f}!\n'
      'Para pintar essa parede, você ira precisar de {:.2f} litros de tinta!'.format(l, a, m2, t))
