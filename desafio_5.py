#FUNCAO DA ETAPA 1
def contador(equipes_bootcamp_dados):
  contador = []
  for i in equipes_bootcamp_dados:
    quantidade = i.count('a')
    contador.append(quantidade)
  return contador

#RODAR A ETAPA 1
equipes_bootcamp_dados = ['BerthaLutz', 'GraceHopper', 'JaquelineGoes', 'SarahGilbert']
resultado = contador(equipes_bootcamp_dados)
print(resultado)

#LER A ETAPA 2
lista_alunas = ['Maria', 'Ana','Camila','Mariana','Elaine','Patricia','Marina','Erica','Larissa','Luiza', 'Nicole','Bruna']

#FUNCAO DA ETAPA 3

def ordenacao(lista_alunas, equipes_bootcamp_dados):
  dicionario_equipes = {}
  contador_aluna = 0
  contador_equipe = 0

  lista_alunas_ordenada = sorted(lista_alunas)

  for equipe in equipes_bootcamp_dados:
    if len(lista_alunas_ordenada) >= contador_aluna+1:
      dicionario_equipes[equipe] = []
      contador_equipe += 1
      for i in range(3):
        if len(lista_alunas_ordenada) >= contador_aluna+1:
          dicionario_equipes[equipe].append(lista_alunas_ordenada[contador_aluna])
          contador_aluna += 1
        else:
          break
    else:
      break

  if len(lista_alunas_ordenada) > contador_aluna:
    print("Há %i aluna(s) fora de uma equipe. Sugiro escalar mais funcionários ou aumentar a quantidade de alunas por equipe." %(len(lista_alunas_ordenada)-contador_aluna))
    return dicionario_equipes
  elif len(equipes_bootcamp_dados) > contador_equipe:
    print("Há %i avaliador(es) sem alunas. Sugiro realocá-lo(s) para outras funções ou diminuir a quantidade de alunas de alguma(s) equipe(s) e redistribuir." %(len(equipes_bootcamp_dados)-contador_equipe))
    return dicionario_equipes
  else:
    return dicionario_equipes
  
#RODAR A FUNCAO DA ETAPA 3
distribuicao_equipes = ordenacao(lista_alunas, equipes_bootcamp_dados)
print(distribuicao_equipes)