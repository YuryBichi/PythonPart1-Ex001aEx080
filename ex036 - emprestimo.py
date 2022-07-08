vcasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe salario: R$'))
anos = int(input('Informe quantos anos deseja pagar: '))
parcela = vcasa / (anos * 12)
if parcela <= (salario * 0.30):
    print('A parcela do seu emprestimo ficou em R${:.2f} !\nEmprestimo aprovado'.format(parcela))
else:
    print('A parcela ficaria no valor de R${:.2f}, excedendo 30% de R${:.2f} !\nEmprestimo negado'.format(parcela, salario))
