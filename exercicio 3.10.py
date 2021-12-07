valor_salario = float(input("Digite o valor do salário: "))
percentagem = float(input("Qual a percentagem do aumento: "))
novo_salario = (valor_salario + valor_salario * percentagem/100)
print ('Diante de um aumento de %4.2f por cento no salário, o novo salário é de %5.2f.' % (percentagem, novo_salario))
