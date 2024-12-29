# Login Authentication

usuario1 = 'admin'
usuario1_senha = '123456'

usuario = input('Digite o nome de usuário: ')
senha = input('Digite a sua senha: ')

if usuario == usuario1 and senha == usuario1_senha:
    print('LOGIN CONCEDIDO!')
else:
    print('Usuário ou senha incorretos.TENTE NOVAMENTE!')