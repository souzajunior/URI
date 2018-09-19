N = int(input())

for i in range(N):
    entrada = input().split()
    entrada = [int(x) for x in entrada]
    entrada.sort()
    X,Y = entrada
    lista_impares = []
    for j in range(X+1, Y):
        if (j % 2 != 0):
            lista_impares.append(j)
    print(sum(lista_impares))




