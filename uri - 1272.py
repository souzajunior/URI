N = int(input())

for i in range(N):
    entrada = input()
    entrada = entrada.strip()
    entrada = entrada.split()
    nova_palavra = ''

    for j in entrada:
        nova_palavra += j[0]

    print(nova_palavra)
