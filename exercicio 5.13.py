divida = float(input("Qual o valor inicial da dívida: "))
juros = float(input("Qual os juros percentuais contratados para essa dívida? "))
pagamento = 0
mes = 1
saldodevedor = divida + (divida * juros/100) - pagamento
pagamentototal = 0
while saldodevedor > 0:
    pagamento = float(input("Qual o valor será pago no mês %d? " % mes))
    saldodevedor = saldodevedor + (saldodevedor * juros/100) - pagamento
    pagamentototal += pagamento
    mes = mes + 1
print ("O total de meses necessários para pagamento da dívida é %d. " % (mes-1))
print ("O total pago com essa dívida foi de %5.2f." % pagamentototal)
print ("O valor total dos juros pagos foi de %5.2f. " % (pagamentototal - divida))

