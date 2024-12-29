hor = int(input('Qual o horário de agora?: '))

if hor < 12:
    print(f'Agoar são {hor}HR. BOM DIA!')
elif hor < 18:
    print(f'Agora são {hor}HR. BOA TARDE!')
else:
    print(f'Agora são {hor}HR. BOA NOITE!')
