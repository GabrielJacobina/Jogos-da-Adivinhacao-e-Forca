def jogar():

  import random
  print("*********************************")
  print("***Bem vindo ao jogo da Forca!***")
  print("*********************************")

  pontos = 1000
  numero_secreto = random.randrange(1, 100)
  total_de_tentativas = 0

  print("Qual o nível de dificuldade?")
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("Defina o nível: "))

  if(nivel == 1):
    total_de_tentativas = 20
  elif (nivel == 2):
    total_de_tentativas = 10
  else:
    total_de_tentativas = 5


  for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}". format(rodada, total_de_tentativas))
    

    chute_str = input("Digite um número entre 1 e 100: ")
    print("VocÊ digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
      print("Você acertou e fez {} pontos!".format(pontos))
      break
    else:
      if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
      elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    
    rodada = rodada + 1

  print("Fim de jogo")


  '''print("R$ {:7.2f}".format(1234.50))

  print("R$ {:07.2f}".format(1.5))

  print("R$ {:07d}".format(4))'''

  '''print("Data {:02d}/{:02d}".format(9,4))

  print("Data {:02d}/{:02d}".format(19,11))'''

  '''print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))'''

  '''import random

  random.seed(1, 101)
  print(random.randrange(100))'''

  '''print(round(4.5))'''

if(__name__ == "__main__"):
  jogar()