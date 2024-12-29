compra = float(input('Qual o valor da compra?: R$ '))

if compra > 200:
    desconto = 0.2
elif compra > 100:
    desconto = 0.1
else:
    desconto = 0.05

valor_final = compra - (compra * desconto)
print(f'Sua compra foi de R$ {compra:.2f} reais. Com o  desconto fica R$ {valor_final:.2f} reais.')

