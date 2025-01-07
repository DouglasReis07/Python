 #O PRINT ele realiza tarefa, e o RETURN retorna um valor


def cliente1(nome):
    print(f'Olá {nome}')


def cliente2(nome):
    return f'Olá {nome}'

x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)