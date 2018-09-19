N = int(input())
vetor = []
for i in range(N):
    num = int(input())
    vetor.append(num)
vetor_2 = vetor[:]
vetor_2 = list(set(vetor_2))
for i in vetor_2:
    print('{} aparece {} vez(es)'.format(i, vetor.count(i)))

