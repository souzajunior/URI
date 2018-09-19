while True:
    try:
        lista = []
        N = int(input())
        
        for i in range(N):
            entrada = input()
            lista.append(entrada)

        lista.sort()
        for j in lista:
            print(j)
    except EOFError:
        break
