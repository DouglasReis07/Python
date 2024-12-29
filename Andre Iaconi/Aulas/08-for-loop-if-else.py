# Enviar um email com os detalhes da compra onnline (maximo 3 tentativas) para compras confirmadas.

compra_confirmada = False
dados_compra = 'Compra no valor de R$ 12.50 e entrega confirmada'

for enviar in range (3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para o seu E-mail.')
        break
else:
    print('Ocorreu um ERRO ao efetuar a compra!')

