a = (input('Digite algo: '))

print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços?: ',a.isspace() )
print('É um numero?: ', a.isnumeric())
print('É alfabético?: ', a.isalpha())
print('É alfanúmerico?: ', a.isalnum())
print('Está em maiúscula?: ',a.isupper())
print('Está em minúscula?: ',a.islower())
print('Está capitalizada?: ',a.istitle())
