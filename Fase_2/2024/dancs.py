linhas, colunas, numPassos = map(int, input().split())

matriz = []
cont = 1

for i in range(0, linhas):
    linha = []
    for j in range(0, colunas):
        linha.append(cont)
        cont += 1
    matriz.append(linha)

map_linhas = []
map_col = []
for a in range(0, linhas):
    map_linhas.append(a)
for b in range(0, colunas):
    map_col.append(b)


for i in range(0, numPassos):
    passos_leitura = input().split()

    posicao1 = int(passos_leitura[1]) - 1
    posicao2 = int(passos_leitura[2]) - 1

    if passos_leitura[0] == 'L':
        map_linhas[posicao1], map_linhas[posicao2] = map_linhas[posicao2], map_linhas[posicao1]
    else:
        map_col[posicao1], map_col[posicao2] = map_col[posicao2], map_col[posicao1]

for i in range(linhas):
    for j in range(colunas):
        valor = matriz[map_linhas[i]][map_col[j]]
        print(valor, end=' ')
    print()
