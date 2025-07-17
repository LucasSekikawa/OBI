N, K = map(int,input().split())
Notas = list(map(int, input().split()))
Notas.sort(reverse=True)
print(Notas[K-1])
