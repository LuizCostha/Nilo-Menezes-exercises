a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
if a > b > c:
    print ("Os dois maiores números são %3.2f e %3.2f." % (a,b))
if b > c > a:
    print("Os dois maiores números são %3.2f e %3.2f." % (b, c))
if c > a > b:
    print("Os dois maiores números são %3.2f e %3.2f." % (c, a))
if c > b > a:
    print("Os dois maiores números são %3.2f e %3.2f." % (c, b))
if b > a > c:
    print("Os dois maiores números são %3.2f e %3.2f." % (b, a))
if a > c > b:
    print("Os dois maiores números são %3.2f e %3.2f." % (a, c))


