n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    resultado = str(x**y)
    print(len(resultado))
