ent = input().split()

for index, i in enumerate(ent):
    if (len(i) > 3):
        if(i[:2] == i[2:4]):
              ent[index] = i[2:]           

print(" ".join(ent))
