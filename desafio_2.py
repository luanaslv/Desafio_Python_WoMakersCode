#função de classificação de faixa etária
def classifica_idade(idade):
  if idade >= 0 and idade < 13:
    print("Criança – 0 a 12 anos.")
    return 1
  elif idade >= 13 and idade < 18:
    print("Adolescente – 13 a 17 anos.")
    return 1
  elif idade >= 18: #o enunciado classifica adulto como sendo acima de 18 anos(idade > 18), caso seja seguido ao pé da letra o valor exato "18" ficará sem classificação.
    print("Adulto – acima de 18 anos.")
    return 1
  else:
    print("Idade inválida! Insira um valor positivo.\n")

#considerando idade inteira
while True:
  try:
    idade = int(input("Insira a idade que deseja saber a faixa etária: "))
    loop = classifica_idade(idade)
    if loop == 1:
      break

  except ValueError:
    print("Valor inválido! Insira apenas números inteiros.\n")