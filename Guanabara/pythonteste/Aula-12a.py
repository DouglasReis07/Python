nome = str(input('Qual é o seu nome?: '))
if nome == 'Douglas':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Gustavo':
    print('Seu nome é bastante popular.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')