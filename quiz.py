print("Bem-vindo ao meu quiz de computador")

jogando = input("Você quer jogar? ")

if jogando.lower() != "sim":
    quit()

print("Okay! Vamos jogar :)")

pontos = 0

resposta1 = input("O que faz a CPU no computador? ")
if resposta1.lower() == "unidade central de processamento":
    print("Correto!")
    pontos += 1
else:
    print("Está errado!")

resposta2 = input("O que GPU significa em português? ")
if resposta2.lower() == "unidade de processamento de gráficos":
    print("Correto!")
    pontos += 1
else:
    print("Está errado!")

resposta3 = input("O que RAM significa em portguês? ")
if resposta3.lower() == "memória de acesso aleatório":
    print("Correto!")
    pontos += 1
else:
    print("Está errado!")

resposta4 = input("O que significa PSU em portguês? ")
if resposta4.lower() == "unidade de fonte de alimentação":
    print("Correto!")
    pontos += 1
    print(f"Você fez {pontos} pontos")
else:
    print("Está errado!")


