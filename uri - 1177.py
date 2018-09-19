N = int(input())
aux = 0

for i in range(1000):
    if (aux == N):
        aux = 0
    print('N[{}] = {}'.format(i, aux))
    aux += 1
