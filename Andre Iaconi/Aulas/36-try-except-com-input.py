'''
try:
    valor = int(input('Digite o valor do seu prdouto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')


print('Mais código abaixo...')
'''

'''
try:
    valor = int(input('Digite o valor do seu prdouto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
else:
    print('Usuario digitou um valor correto')
    resultado = valor * 2
    print(resultado)

print('Mais código abaixo...')
'''

try:
    valor = int(input('Digite o valor do seu prdouto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
finally:
    print('Codigo ok')

print('Mais código abaixo...')


