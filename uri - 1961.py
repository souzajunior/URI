altura_pulo, canos = map(int,input().split())
a_canos = list(map(int, input().split()))
ganhou = True

for i in range(len(a_canos) - 1):
    if (altura_pulo < abs(a_canos[i] - a_canos[i+1])):
        ganhou = False
        break

if (ganhou == True):
    print('YOU WIN')
else:
    print('GAME OVER')
