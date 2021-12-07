km = float(input("Qual a distância em quilômetros percorrida pelo carro alugado? "))
dias = int(input("Por quantos dias o carro ficou alugado? "))
preco = (60 * dias) + (0.15 * km)
print ("O preço total da locação a pagar é R$%5.2f." % preco)

