sal = int(input("Qual o seu salário?: "))
sal1 = sal + (sal * 10) / 100
sal2 = sal + (sal * 15 ) / 100
if sal > 1250:
    print(f"O seu salário recebeu um aumento de 10%, e agora é R${sal1:.2f} reais.")
else:
    print(f"O seu salário recebeu um aumento de 15%, e agora é R${sal2:.2f} reais.")