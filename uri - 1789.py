while True:
    try:
        N = int(input())
        entrada = list(map(int, input().split()))
        num_max = max(entrada)
        nivel = 1

        if (10 <= num_max < 20):
            nivel = 2
        elif (20 <= num_max):
            nivel = 3

        print(nivel)
    except (EOFError):
        break