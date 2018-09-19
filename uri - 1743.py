entrada = list(map(int,input().split()))
entrada_dois = list(map(int,input().split()))
encaixa = 'N'
cont = 0

for i in range(5):
    if (entrada[i] == entrada_dois[i]):
        break
    cont += 1
if (cont == 5):
    encaixa = 'Y'
    print(encaixa)
else:
    print(encaixa)
