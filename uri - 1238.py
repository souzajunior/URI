n = int(input())

for i in range(n):
    p1, p2 = input().split()
    nova_palavra = ''

    while True:
        if (p1 == ''):
            nova_palavra += p2
            break
        elif (p2 == ''):
            nova_palavra += p1
            break

        nova_palavra += p1[0] + p2[0]

        if (len(p1) == 1):
            p1 = ''
        else:
            p1 = p1[1:]

        if (len(p2) == 1):
            p2 = ''
        else:
            p2 = p2[1:]

    print(nova_palavra)

