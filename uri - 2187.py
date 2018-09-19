teste = 0
while True:
    valor = int(input())

    if (valor == 0):
        break

    teste += 1

    nota_50 = valor//50
    resto_50 = valor%50

    nota_10 = resto_50//10
    resto_10 = resto_50%10

    nota_5 = resto_10//5
    resto_5 = resto_10%5

    nota_1 = resto_5//1
    resto_1 = resto_5%1

    print('Teste {}'.format(teste))
    print('{0} {1} {2} {3}'.format(nota_50, nota_10, nota_5, nota_1))
    print()