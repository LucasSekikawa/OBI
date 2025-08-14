mensagem = input()

alfabeto_alienigena = set(alfabeto)

check = True
for char_mensagem in mensagem:
    if char_mensagem not in alfabeto_alienigena:
        check = False
        break
if check:
    print('S')
else:
    print('N')
