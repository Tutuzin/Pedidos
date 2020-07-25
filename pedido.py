def produtos(pedido):
    if pedido.isdigit():
        vezes = 0
        lenght = len(pedido)
        quantidades = [0,0,0]
        while vezes != lenght:
            vez = int(pedido[vezes])
            vezes += 1
            if vez == 1: quantidades[0] += 1
            else:
                if vez == 2: quantidades[1] += 1
                else:
                    if vez == 3: quantidades[2] += 1
                    else: print('Produto ', vez, ' não cadastrado')
        return quantidades
def valor(quantidades):
    #modificar preços aqui
    preço = (1,3,5)
    produto = 0
    valor = 0
    for x in quantidades:
        valor += x*preço[produto]
        produto += 1
    print(valor)

