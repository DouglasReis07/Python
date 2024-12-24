nome = str(input("Digite seu nome completo: ")).strip()
nomem = nome.upper()
nomemi = nome.lower()
nomesp = len(nome)
nomen = nome.find(" ")


print(f"O seu nome com todas as letras maiúsculas fica {nomem}")
print(f"O seu nome com todas as letras minisculas fica {nomemi}")
print(f"O seu nome completo sem espaços tem {nomesp-nome.count(" ")} letras")
print(f"O seu primeiro nome tem {nomen} letras")