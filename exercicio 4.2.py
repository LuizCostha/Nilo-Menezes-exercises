vel = float(input("Digite a velocidade do carro em km/h: "))
if vel > 80:
    print ("Você foi multado. O valor da multa a pagar é R$%5.2f." % ((vel - 80) * 5))
