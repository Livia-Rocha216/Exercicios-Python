# Calcule sua gorjeta
def dolares_para_float(d):
  # Remove o '$' do valor dado pelo usuário, retornando como float.
  return float(d.replace('$', " ")) 
def percentual_para_float(p):
  # Remove o '%' do valor dado pelo usuário, retornando como float.
  # Divide o valor por 100, fazendo o calculo de porcentagem para decimal.
  return float(p.replace('%', " ")) / 100

dolares_para_float('$50.00') # Saída: 50.00
percentual_para_float('15%') # Saída: 0.15

dolares = dolares_para_float(input("Quanto custou a refeição? ")) # Valor em dinheiro.
percentual = percentual_para_float(input("Qual percentual você gostaria de deixar de gorjeta? ")) # Valor em porcentagem.
gorjeta = dolares * percentual # Multiplicação para o valor da gorjeta.
print(f"Deixe ${gorjeta:.2f}") # Saída