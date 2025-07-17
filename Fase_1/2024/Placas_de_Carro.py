placa = input()
saida = 0
if len(placa) == 8:
    check = True
    for i in range(0, 3):
        if not placa[i].isupper():
            check = False
            break
    if placa[3] != '-':
        check = False
    for j in range(4, 8):
        if not placa[j].isdigit():
            check = False
            break
    if check:
        saida = 1

elif len(placa) == 7:
    check = True
    for i in range(0, 3):
        if not placa[i].isupper():
            check = False
            break
    if not placa[3].isdigit():
        check = False
    if not placa[4].isupper():
        check = False
    if not (placa[5].isdigit() or placa[6].isdigit()):
        check = False
    if check:
        saida = 2
print(saida)
