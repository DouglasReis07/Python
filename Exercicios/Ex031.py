km = int(input("Qual a distancia da sua viagem?: "))
prc = km * 0.50
prc1 = km * 0.45
if km <= 200:
    print(f"O preço da sua viagem de {km}KM fica R${prc:.2f} reais!")
else:
    print(f"O preço da sua viagem de {km}KM fica R${prc1:.2f} reais!")


