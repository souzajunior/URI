#Incompleto
A, B = list(map(int, input().split()))

quociente = A//B
resto = A%B

if (resto < 0):
    if (quociente > 0):
        quociente += 1
    elif (quociente < 0):
        quociente -= 1
    resto = A -(quociente * B)

print(quociente, resto)