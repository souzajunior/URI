N = int(input())

for i in range(N):
    entrada = input()
    if (len(entrada) % 2 == 0):
        primeira_parte = entrada[len(entrada)//2 -1::-1]
        segunda_parte = entrada[:len(entrada)//2 -1:-1]
    else:
        primeira_parte = entrada[len(entrada)//2::-1]
        segunda_parte = entrada[:len(entrada)//2:-1]

    primeira_parte = primeira_parte.split()
        
    segunda_parte = segunda_parte.split()
    segunda_parte[0] =  primeira_parte[-1] + segunda_parte[0]
    del primeira_parte[-1]

    if ((len(primeira_parte) > 1) and (len(segunda_parte) > 1)):
        primeira_parte = ' '.join(primeira_parte)
        primeira_parte += ' '
        segunda_parte = ' '.join(segunda_parte)
    else:
        primeira_parte = ' '.join(primeira_parte)
        segunda_parte = ' '.join(segunda_parte)

    resultado_final = primeira_parte + segunda_parte
    print(resultado_final)

'''
N = int(input()) 
for h in range(N):
 Entrada = input()
 Meio = len(Entrada)//2
 Fim = len(Entrada) 
 String = "" 
 for i in reversed(range(Meio)):
  String += Entrada[i] 
 for j in reversed(range(Meio, Fim)):
  String += Entrada[j]
 
 print(String)
'''
