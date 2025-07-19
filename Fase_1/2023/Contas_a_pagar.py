V = int(input())
A = int(input())
F = int(input())
P = int(input())
cont = 0
valores = [A, F, P]
while valores:
    menor_valor = min(valores)
    if V >= menor_valor:
        cont += 1
        V = V - menor_valor
        valores.remove(menor_valor)
    else:
        break
print(cont)
