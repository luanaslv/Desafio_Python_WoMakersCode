#função plus conversão de horas em segundos, recebendo horas, minutos e segundos.
def time_converter_completo():
  while True:
    horario = input("\nInsira o horário que deseja converter: ")
    separa_horario = horario.split(":")
    try:
      horas = int(separa_horario[0])
      minutos = int(separa_horario[1])
      segundos = int(separa_horario[2])
      
      if len(horario) != 8 or len(separa_horario) != 3:
        print("Quantidade de caracteres inválida. por favor, seguir o modelo a seguir: HH:MM:SS")   
      elif horas > 23:
        print("Valor de horas acima de 23. Favor, inserir valor até 23.")
      elif minutos > 59:
        print("Valor de minutos acima de 59. Favor, inserir valor até 59.")
      elif segundos > 59:
        print("Valor de segundos acima de 59. Favor, inserir valor até 59.")
      else:
        conversao = horas * 3600 + minutos * 60 + segundos
        return conversao

    except ValueError:
      print("Valor inválido. Use apenas números inteiros para as horas, minutos e segundos.") 

#funçao conversao de horas em segundos, conforme enunciado.
def time_converter_horas():
  while True:
    try:
      horas = float(input("\nInsira o valor em horas que deseja converter: "))
      if horas < 0:
        print("Valor negativo! Insira o valor correto.")
      else:
        conversao = int (horas * 3600)
        return conversao

    except ValueError:
      print("Valor inválido. Use apenas números para as horas.") 

#código com menu 1 e 2, para aquele uma função plus e para este a função pedida no enunciado.
print("Olá, bem-vindo ao conversor de horas para segundos! ")
print("Para converter um valor de relógio em segundos confome exemplo a seguir *09:05:26*, insira 1.")
print("Para converter um valor de uma quantidade de horas em segundos conforme o exemplo a seguir *300 horas*, insira 2.")

try:
  menu = int(input("\nInsira 1 ou 2: "))
  if menu == 1:
    print("\nInsira o valor que deseja usando : (dois pontos) para separar as horas, os minutos e os segundos, como no exemplo a seguir --> 09:05:26")
    conversao = time_converter_completo()
  elif menu == 2:
    conversao = time_converter_horas()
  else:
    print("Valor inválido. Insira 1 ou 2.")

except ValueError:
  print("\nValor inválido. Use apenas números.")  

print(f"\nO valor em segundos referente o horário inserido é de: {conversao} segundos.")