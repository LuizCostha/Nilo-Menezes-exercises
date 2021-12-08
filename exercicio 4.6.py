distancia = float(input("Digite a distância em quilômetros que deseja percorrer: "))
if distancia <= 200:
    print ("O preço da passagem é R$%3.2f." % (0.5 * distancia))
else:
    print ("O preço da passagem é R$%3.2f." % (0.45 * distancia))


