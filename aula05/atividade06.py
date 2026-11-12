venda = float(input('Valor da venda: '))

match venda:
    case venda if venda < 100:
        print('Venda Pequena')
    case venda if venda < 500:
        print('Venda Média')
    case _:
        print('Venda Grande')
    
