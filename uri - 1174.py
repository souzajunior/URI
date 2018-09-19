vetor = []
for i in range(100):
    valor = float(input())
    vetor.append(valor)

for index, j in enumerate(vetor):
    if (j <= 10):
        print('A[{}] = {:.1f}'.format(index, j))

