n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
x = 0
s = n1
while s >= n2:
    s = s - n2
    x = x + 1
print ("A divisão inteira é: %d. " % (x))
print ("O resto da divisão é %3.2f. " % (s))

