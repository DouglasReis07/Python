cor = str(input('Qual cor deseja?: '))
estoque = ['azul',
         'verde',
         'azul',
         'vermelho']

if cor.lower() in estoque:
    print('Essa cor se encontra no estoque.')
else:
    print('Essa cor está em falta.')