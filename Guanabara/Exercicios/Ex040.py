n1 = float(input('Qual foi sua primeira nota?: '))
n2 = float(input('Qual foi sua segunda nota?: '))
n3 = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f} a média do aluno é {n3:.1f}!')
if  n3 >= 7:
    print('PARABÉNS! VOCÊ ESTÁ APROVADO!')
elif 7 > n3 >= 5:
    print('Você está de RECUPERAÇÃO!')
elif n3 < 5:
    print('Você está REPROVADO!')

