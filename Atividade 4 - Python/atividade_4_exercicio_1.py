# O filtro de slogans
palavra_chave = "gato"
min_palavras = 7
max_palavras = 10
slogan = input("Digite um slogan que possua a palavra-chave --> " + palavra_chave + ". ")
if palavra_chave in slogan: # Se a palavra-chave estiver incluida no slogan, um novo código para verificar a quantidade de palavras será executado.
  num_palavras = len(slogan.split())
  if num_palavras < min_palavras: # Se tiver menos de 7 palavras, será inadequado.
    print("Slogan inadequado (menos de 7 palavras).")
  elif num_palavras > max_palavras: # Se tiver mais de 10 palavras, será inadequado.
    print("Slogan inadequado (mais de 10 palavras).")
  else: # Se estiver entre 7 e 10 palavras, será adequado, e executará um novo código para verificar se o slogan começa e termina com uma letra.
    if slogan[0].isalpha() and slogan[-1].isalpha(): # Se começar e terminar com uma letra, além de cumprir os outros requisitos, será adequado.
      print("Slogan adequado (palavra-chave "+palavra_chave+" está no slogan, possui a quantidade certa de letras e começa e termina com uma letra).")
    else: # Se não começar e terminar com uma letra, será inadequado.
      print("Slogan inadequado, seu slogan deve começar e terminar com uma letra.")
else: # Se a palavra-chave não estiver incluida no slogan, será retornado como inadequado.
  print("Slogan inadequado (palavra-chave "+palavra_chave+" não está no slogan).")