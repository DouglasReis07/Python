idade = int(input('Digite a sua idade: '))

# if idade >= 18:
#    print(f'Sua idade é de {idade} anos. MAIOR DE IDADE!')
# else:
#    print(f'Sua idade é de {idade} anos. MENOR DE IDADE!')

if idade < 18:
    print(f'Sua idade é de {idade} anos. MENOR DE IDADE!')
elif idade >= 18 and idade < 60:
   print(f'Sua idade é de {idade} anos. MAIOR DE IDADE!')
else:
    print(f'Sua idade é ed {idade} anos. IDOSO')
