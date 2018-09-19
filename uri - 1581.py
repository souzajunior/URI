N = int(input())
for i in range(N):
    K = int(input())
    
    lista_idiomas = []
    idioma_escolhido = ''
    
    for j in range(K):
        entrada = input()
        lista_idiomas.append(entrada)
        
    for m in lista_idiomas: # m sera cada idioma da lista
        if (lista_idiomas.count(m) > 1): # Se o idioma se repetir, entao iremos remover para ficar fácil saber qual sera escolhido
            for k in range(lista_idiomas.count(m) - 1): # removendo repetições
                lista_idiomas.remove(m)
        if (len(lista_idiomas) > 1): #Se tiver mais de um elemento, entao sera ingles, pois não terá repetição do mesmo idioma
            idioma_escolhido = 'ingles'
        else:
            idioma_escolhido = m # Se o tamanho for 1 da lista, então significa dizer que temos o idioma definido
    print(idioma_escolhido)
