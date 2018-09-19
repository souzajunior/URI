while True:
    L,R = map(int, input().split())

    if (L == R == 0):
        break

    soma = L + R
    print(soma)