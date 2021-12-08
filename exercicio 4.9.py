valorcasa = float(input("Qual o valor da casa a ser financiada? "))
salario = float(input("Qual o valor do seu salário? "))
anos = int(input("Em quantos anos será o financiamento? "))
valorprestacao = valorcasa / (12 * anos)
if valorprestacao > (0.3 * salario):
    print("Infelizmente o financiamento não será possível.")
else:
    print("A casa será financiada com prestações mensais no valor de R$%5.2f." % valorprestacao)


