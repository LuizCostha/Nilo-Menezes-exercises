n = int(input("Tabuada de: "))
m1 = int(input("Digite o primeiro múltiplo da tabuada de n que deseja mostrar: "))
m2 = int(input("Digite o último múltiplo da tabuada de n que deseja mostrar: "))
while m1 <= m2:
    print ("%s * %s = %d"  % (n, m1, (n * m1)))
    m1 =  m1 + 1

