vetor = []
for i in range(20):
    valor = int(input())
    vetor.append(valor)

inicial = 0
final = 19

while (inicial < 10):
    temp = vetor[inicial]
    vetor[inicial] = vetor[final]
    vetor[final] = temp
    inicial += 1
    final -= 1

for index, k in enumerate(vetor):
    print('N[{}] = {}'.format(index, k))