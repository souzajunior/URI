vetor = [1,1,1,1,1,1,1,1,1,1]

V = int(input())
vetor[0] = V

for i in range(1,10):
    vetor[i] = vetor[i-1] * 2

for index,k in enumerate(vetor):
    print('N[{}] = {}'.format(index, k))

