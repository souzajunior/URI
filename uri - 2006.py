tipo_cha = int(input())
entrada = input().split()
entrada =[int(x) for x in entrada]
respostas_corretas = entrada.count(tipo_cha)
print(respostas_corretas)