deposito = float(input("Qual o depósito inicial na poupança? "))
taxa = float(input("Qual a taxa percentual de juros da poupança? "))
mes = 1
saldo_poupanca = deposito
while mes <= 24:
    saldo_poupanca = saldo_poupanca + (saldo_poupanca * (taxa / 100))
    novodeposito = float(input("Digite o valor do depósito no mês %d. Se não houve novo depósito, digite 0. " % mes))
    saldo_poupanca = saldo_poupanca + novodeposito
    depositosacumulados = deposito + novodeposito
    print ("O valor atualizado da poupança no mês %d é %5.2f. " % (mes, saldo_poupanca))
    mes = mes + 1
print ("O total ganho com juros no período foi de R$%5.2f." % (saldo_poupanca-depositosacumulados))