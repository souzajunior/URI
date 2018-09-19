x = int(input())
y = int(input())
valores_somar = []
if (x > y):
    x,y = y,x

for i in range(x,y+1):
    if (i % 13 == 0):
        continue
    valores_somar.append(i)

soma = sum(valores_somar)
print(soma)
