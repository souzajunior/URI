while True:
    N = int(input())
    if N == 0:
        break
    entrada = input()
    # os indices da lista representam os pontos
    pontos_cardeais = ["N", "L", "S", "O"]
    # Comeca no norte = "0"
    estado = 0
    for i in entrada:
        if i == 'D':
            if (estado == 3):
                estado = 0
            else:
                estado += 1
        elif (i == 'E'):
            if (estado == 0):
                estado = 3
            else:
              estado -= 1
    print(pontos_cardeais[estado])