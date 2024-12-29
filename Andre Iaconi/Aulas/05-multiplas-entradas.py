#Multiplas entradas na mesma linha de Input()

dados = input('Digite o seu nome, idade e altura: ').split()
nome = dados[0]
idade = dados[1]
altura = dados[2]

print(f'Meu nome é {nome.upper()}, tenho {idade} anos de idade e minha é de {altura} em centimetros ')