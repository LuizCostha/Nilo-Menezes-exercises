s = 0
quantidade  = 0
totalcompra = 0
while True:
    codproduto = int(input("Digite o código do produto. Se não deseja comprar nada, digite 0: "))
    if codproduto == 0:
        break
    quantidade = int(input("Qual a quantidade comprada: "))
    if codproduto == 1:
        totalcompra = totalcompra + quantidade * 0.50
        codproduto = int(input("Deseja comprar mais produtos? Se sim, digite o código do produto. Se não, digite 0. "))
        if codproduto == 0:
            break
        if codproduto == 2:
            quantidade = int(input("Qual a quantidade comprada: "))
            totalcompra = totalcompra + quantidade * 1
            codproduto = int(input("Deseja comprar mais produtos? Se sim, digite o código do produto. Se não, digite 0. "))
            if codproduto == 0:
                break
            if codproduto == 3:
                quantidade = int(input("Qual a quantidade comprada: "))
                totalcompra = totalcompra + quantidade * 4
                codproduto = int(input("Deseja comprar mais produtos? Se sim, digite o código do produto. Se não, digite 0. "))
                if codproduto == 0:
                    break
                if codproduto == 5:
                    quantidade = int(input("Qual a quantidade comprada: "))
                    totalcompra = totalcompra + quantidade * 7
                    codproduto = int(input("Deseja comprar mais produtos? Se sim, digite o código do produto. Se não, digite 0. "))
                    if codproduto == 0:
                        break
                    if codproduto == 9:
                        quantidade = int(input("Qual a quantidade comprada: "))
                        totalcompra = totalcompra + quantidade * 8
print ("O total das compras é %3.2f" % totalcompra)



