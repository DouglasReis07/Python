# Controle de temperatura

temp = int(input('Qual a temperatura?: '))

if temp <=10:
    print(f'A temperatura é de {temp}°c. MUITO FRIO!')
elif temp < 20:
    print(f'A temperatura é de {temp}°c. ESTÁ FRESCO!')
else:
    print(f'A temperatura é de {temp}°c. MUITO QUENTE!')
