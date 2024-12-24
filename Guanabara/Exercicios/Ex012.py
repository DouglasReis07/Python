pr = float(input('Qual o preço do produto: '))
dsc = float(pr*5)/100

print(f'O preço do produto é R${pr:.2f} reais, com 5% de desconto ele fica a R${pr-dsc:.2f}.')