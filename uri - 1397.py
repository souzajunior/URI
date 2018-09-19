while True:
    N = int(input())

    if (N == 0):
        break

    pnts_A = pnts_B = 0

    for i in range(N):
        A, B =  map(int, input().split())

        if (A > B):
            pnts_A += 1
        elif (A < B):
            pnts_B += 1
    print('{} {}'.format(pnts_A,pnts_B))

