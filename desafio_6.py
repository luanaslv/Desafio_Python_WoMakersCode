#Função conversor de temperatura Celsius para Fahrenheit.
def conversor_temperatura(temperatura):
  conversao = (9 * temperatura + 160) / 5
  return conversao

#Rodar função
while True:
  try:
    temperatura = float(input("Insira o valor em graus Celsius: "))
    break
  except ValueError:
    print("Valor inválido! Insira somente números\n")

resultado = conversor_temperatura(temperatura)
print(f"\nA temperatura {temperatura} graus Celsius é equivalente a {resultado:.2f} graus Fahrenheit.")