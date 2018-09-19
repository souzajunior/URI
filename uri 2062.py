N = int(input())
entrada = input().split()

for n in range(N):
    if (entrada[n] == 'OBI') or (entrada[n] == 'URI'):
        continue
    elif (len(entrada[n]) == 3 and (entrada[n][:2] == 'OB')):
        entrada[n] = 'OBI'
    elif (len(entrada[n]) == 3 and (entrada[n][:2] == 'UR')):
        entrada[n] = 'URI'

entrada = ' '.join(entrada)
print(entrada)
