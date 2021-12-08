kwh = float(input("Quantos kwh foram consumidos? "))
tipoins = str(input("Qual seu tipo de instalação elétrica? Digite R para residência, I para indústria ou C para comércios. "))
if tipoins == "R":
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
        print("O preço da fatura é R$%3.2f." % (kwh * preco))
elif tipoins == "I":
    if kwh <= 5000:
        preco = 0.55
        print("O preço da fatura é R$%3.2f." % (kwh * preco))
    else:
        preco = 0.60
        print("O preço da fatura é R$%3.2f." % (kwh * preco))
elif tipoins == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
        print ("O preço da fatura é R$%3.2f." % (kwh * preco))
else:
    print ("Dados incorretos. Reexecute o programa e, em seguida, digite a quantidade de kmw consumidos e o tipo de instalação elétrica. Digite R para residência, I para indústria ou C para comércios." )
    