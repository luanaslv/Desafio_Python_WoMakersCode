#função calculando a média de notas
def calcula_media(m1,m2,m3):
  media = (m1 + m2 + m3) / 3
  if media >= 0.0 and media <= 4.0: #nesta caso valores acima de 4.0 e abaixo de 4.1 ficam sem classificação.
    print("\nO aluno está reprovado!")
    return 1
  elif media >= 4.1 and media <= 6.0:
    print("\nO aluno pegou exame!")
    valor = 0
    while True:
      try:
        nota_exame = float(input("\nInsira o valor da nota final: "))
        if nota_exame < 0:
          print("Nota inválida! Insira um valor positivo.")
        elif nota_exame > 6.0:
          print("\nEstá aprovado!")
          return 1
        else:
          print("\nEstá reprovado!")
          return 1
      except ValueError:
        print("Valor inválido! Insira apenas números.")
  elif media > 6.0:
    print("\nO aluno está aprovado!")
    return 1
  else:
    print("Valor sem classificação conforme enunciado. Tente novamente.\n")

#rodando programa
while True:
  try:
    m1 = float(input("Insira a primeia nota: "))
    m2 = float(input("Insira a segunda nota: "))
    m3 = float(input("Insira a terceira nota: "))
    
    if (m1 > 10 or m1 < 0) or (m2 > 10 or m2 < 0) or (m3 > 10 or m3 < 0): 
      print("Nota inválida! Insira valores de 0 a 10.\n")
    else:
      loop = calcula_media(m1,m2,m3)
      if loop == 1:
        break

  except ValueError:
    print("Valor inválido! Insira apenas números.\n")