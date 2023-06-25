preco = float(input('Qual é o preço do produto ? '))
desconto = float(input('Quanto de desconto o produto tem ? '))
novo = preco - (preco * desconto / 100)
print('O produto que custava R${:.2f}, na promoção irá custar R${:.2f} com o desconto de {}%.'.format(preco, novo, desconto))