km = float(input('Quantos KM: '))
km1 = (km - 80) * 7
if km <=80:
    print('Dirija com cuidado!')
else:
    print(f'Você esta a {km}KM/h. MULTADO!')
    print(f'Terá que pagar uma multa de R${km1:.2f} reais, por estar acima do limite permitido.')

