preco = float(input("Digite o preço da mercadoria: "))
desconto =  float(input("Digite o percentual do desconto: "))
novopreco = preco - preco * desconto/100
print ("Diante de um desconto de %5.2f por cento, o novo preço da mercadoria é %5.2f." % (desconto, novopreco))

