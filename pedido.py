def produtos(pedido):
    if pedido.isdigit():
        vezes = 0
        lenght = len(pedido)
        quantidades = [0,0,0]
        while vezes != lenght:
            atual = int(pedido[vezes])
            vezes += 1
            if atual == 1: quantidades[0] += 1
            elif atual == 2: quantidades[1] += 1
                elif atual == 3: quantidades[2] += 1
                    else: print('Produto ', atual, ' não cadastrado')
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

