while True:
    N = int(input())
    if (N == 0):
        break

    lista_par = []
    for i in range(N, N+11):
        if (len(lista_par) == 5):
            break
        if (i % 2 == 0):
            lista_par.append(i)

    print(sum(lista_par))
