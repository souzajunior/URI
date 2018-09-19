X = float(input())
vetor = [X]
for i in range(100):
    print('N[{}] = {:.4f}'.format(i, vetor[i]))

    vetor.append(vetor[i]/2.0)