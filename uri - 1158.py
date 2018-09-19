N = int(input())

for i in range(N):
    entrada = input().split()
    X,Y = [int(x) for x in entrada]
    lista_impares = []

    for j in range(X,(X+Y*2)+1):
        if (len(lista_impares) == Y):
            break
        if (j % 2 != 0):
            lista_impares.append(j)

    print(sum(lista_impares))
