# Par ou Ímpar
numero = float(input("Digite um número.")) # Pergunta o número para o usuário.
resultado = numero % int(2) # O cálculo gira em volta do número ser dívisivel por 2 ou não.

if resultado == 0: # Se o número for divísivel por 2, será considerado par.
  print("O número escolhido é par!")
elif resultado != 0: # Se o número não for divísivel por 2, será considerado ímpar.
  print("O número escolhido é ímpar!")
else: # Se ele for um número quebrado, será considerado inválido.
  print("O número escolhido é inválido!")