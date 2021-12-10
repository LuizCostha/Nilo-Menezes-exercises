deposito = float(input("Qual o depósito inicial na poupança? "))
taxa = float(input("Qual a taxa percentual de juros da poupança? "))
mes = 1
valor_poupanca = deposito
while mes <= 24:
    valor_poupanca = valor_poupanca + (valor_poupanca * (taxa / 100))
    print ("O valor atualizado da poupança no mês %d é %5.2f. " % (mes, valor_poupanca))
    mes = mes + 1
print ("O total ganho com juros no período foi de R$%5.2f." % (valor_poupanca-deposito))
