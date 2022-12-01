with open('input1.txt') as f:
    pontos = [list(map(int, row.split(','))) for row in f.readlines()]

with open('input2.txt') as f:
    comandos = [f.readline().split('=')]

for comando in comandos:
    if comando[0] == 'x':
        for i,ponto in enumerate(pontos):
            if ponto[0] > int(comando[1]):
                pontos[i][0] = ponto[0] - abs(ponto[0] - int(comando[1]))*2
    if comando[0] == 'y':
        for i,ponto in enumerate(pontos):
            if ponto[1] > int(comando[1]):
                pontos[i][1] = ponto[1] - abs(ponto[1] - int(comando[1]))*2

print(len(set(map(tuple, pontos))))