num_ingles = ['one', 'two', 'three']
N = int(input())

for i in range(N): # quantas vezes usuario ira digitar
    num_final = ''
    qntd_erro = 0
    entrada = input()
    for j in num_ingles: #j é cada numero da lista ingles
        if (len(j) == (len(entrada)) and (qntd_erro < 2)):
            for k in range(len(entrada)): #k servira como indice [0,1,2,3]
                if (qntd_erro > 1):
                    break
                if (entrada[k] == j[k]):
                    num_final += j[k]
                else:
                    num_final += j[k]
                    qntd_erro += 1

                
    if (num_final == num_ingles[0]):
        print(1)
    elif (num_final == num_ingles[1]):
        print(2)
    elif (num_final == num_ingles[2]):
        print(3)
    else:
        print(num_final)
    
    
