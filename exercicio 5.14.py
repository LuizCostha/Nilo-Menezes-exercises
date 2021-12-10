s = 0
n = 0
while True:
    v = int(input("Digite um número ou 0 para sair: "))
    if v == 0:
        break
    s += v
    n = n + 1
print ("A quantidade de números digitados foi %d. " % n)
print ("A soma dos números digitados é %d. " % s)
print ("A média aritmética dos números digitados é %3.2f." % (s/n))
