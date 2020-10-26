val = int(input())
vet = []
for i in range(val):
    vet.append(int(input()))
    
t = vet[0]
vet = sorted(vet)
if t >= vet[-1]: print("S")
else: print("N")
