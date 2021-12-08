a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = int(input("Qual operação algébrica deseja realizar? Digite 1 para adição, 2 para subtração, 3 para multiplicação, 4 para divisão. "))
if operacao == 1:
    print ("A soma dos dois números é %3.2f." % (a + b))
elif operacao == 2:
    print("A subtração dos dois números é %3.2f." % (a - b))
elif operacao == 3:
    print("A multiplicação dos dois números é %3.2f." % (a * b))
elif operacao == 4:
    print("A divisão dos dois números é %3.2f." % (a / b))
