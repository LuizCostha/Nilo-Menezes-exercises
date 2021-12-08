salario = float(input("Digite o salário do funcionário em reais: "))
if salario > 1250:
    print ("O novo salário é R$%5.2f." % (salario + salario * 0.10))
elif salario <= 1250:
    print ("O novo salário é R$%5.2f." % (salario + salario * 0.15))
