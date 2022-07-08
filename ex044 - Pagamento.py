produto = float(input('Valor do produto: R$'))
selecao = int(input('Menu opção pagamento:\n1 - Dinheiro.\n2 - A vista Cartão.\n3 - Parcelado no cartão.\n'))
if selecao == 1:
    print('Produto com 10% de desconto, de R${:.2f} sai por R${:.2f}.'.format(produto, produto*0.9))
if selecao == 2:
    print('Produto com 5% de desconto, de R${:.2f} sai por R${:.2f}.'.format(produto, produto*0.95))
if selecao == 3:
    parcela = int(input('Digite o numero de parcelas: '))
    if parcela <= 2:
        print('Produto sai por {} de R${:.2f}.'.format(parcela, produto/parcela))
    elif parcela > 3:
        print('Produto com juros de 20%, de R${:.2f} sai por {} de R${:.2f}.'.format(produto, parcela, produto*1.2/parcela))
