linhas, colunas = map(int, input().split())
matriz = []
for i in range(linhas):
    linha = list(map(int, input().split()))
    matriz.append(linha)
num_itens = int(input())
cont = 0
conta_vendas = 0
while cont < num_itens:
    lin, col = map(int, input().split())
    if matriz[lin-1][col-1] != 0:
        matriz[lin-1][col-1] -= 1
        conta_vendas += 1
    cont += 1
print(conta_vendas)
