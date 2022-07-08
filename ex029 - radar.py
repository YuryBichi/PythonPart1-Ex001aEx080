r = int(input('Digite a velocidade do carro: '))
print('O carro esta a {}km/h !'.format(r))
if r > 80:
	e = r - 80
	m = e * 7
	print('Voce foi multado no valor de R${:.2f}, pelo excendente de {}km/h da velocidade maxima permitida, 80km/h !'.format(m, e))
else:
	print('Motorista correto')