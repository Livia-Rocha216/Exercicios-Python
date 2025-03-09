# A caixa registradora
produto = input("Qual o produto? ") # Nome do produto
valor = input("Qual o valor do produto? ") # Valor do produto
pagamento = input("Qual o valor pago? ") # Valor pago pelo usuário
troco = float(pagamento) - float(valor) # Calculo para obter o troco
print("------------------------------------")
print("Comprovante de Venda")
print("------------------------------------")
print("Produto: " + str(produto))
print("Valor do Produto: " + str(valor))
print("Valor Pago: " + str(pagamento))
print("Troco: " + str(troco))
print("------------------------------------") # Retorno em formato de comprovante