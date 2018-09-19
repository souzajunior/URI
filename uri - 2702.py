ref_disp = list(map(int,input().split()))
ref_req = list(map(int,input().split()))

dif = 0

for i in range(3):
    if (ref_req[i] > ref_disp[i]):
        dif += abs(ref_req[i] - ref_disp[i])

print(dif)