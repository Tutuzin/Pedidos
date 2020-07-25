import pedido
card = open('./cardapio.txt','r')
print(card.read())
card.close()
request = input('Insira os produtos ')
quantidades = pedido.produtos(request)
pedido.valor(quantidades)
