 # Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...

# aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# print(aluno)
# print(aluno['nome'])



# aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# aluno['nome'] = 'Jose'
# print(aluno)



# aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# aluno.update({'endereço': 'Rua A','nome': 'Francisco', 'nota_final': 'B'})
# print(aluno)


# aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# del aluno['idade']
# print(aluno)



# aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

# for keys, values in aluno.items():
#   print(keys, values)



aluno = {
    'nome': 'Ana',
    'idade': 16,
    'nota_final': 'A',
    'aprovação': True,
    'Materias': ['Fisica', 'Matematica', 'Ingles']
}
print(aluno)
print(aluno.get('Materias'))
print(len(aluno))
print(aluno.items())
print(aluno.keys())
print(aluno.values())