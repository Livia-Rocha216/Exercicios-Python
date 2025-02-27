# Can you drive?
idade = input("Diga sua idade.")
if idade <= 18:
  print("Você é menor de idade.")
elif idade >= 19 or idade <= 59:
  print("Você é adulto.")
elif idade >= 60:
  print("Você é idoso.")
else: idade <= 0
print("Isso não é um número válido.")