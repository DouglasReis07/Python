nota = int(input('Qual foi a nota do aluno?: '))

if nota >= 9:
    print('Excelente! Você tirou um A!')
elif nota >= 7:
    print('Bom Trabalho! Você tirou um B!')
elif nota >= 5:
    print('Você passou! Mas precisar estudar mais. Sua nota é C!')
else:
    print('Você foi reprovado! Estude mais!')
