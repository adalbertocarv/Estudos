print("Bem-vindo ao meu quiz de computador")

jogando = input("Você quer jogar? ")

if jogando != "sim":
    quit()

print("Okay! Vamos jogar :)")

resposta1 = input("O que faz a CPU no computador? ")
if resposta1 == "unidade central de processamento":
    print("Correto!")
else:
    print("Está errado!")

resposta2 = input("O que GPU significa em português? ")
if resposta2 == "unidade de processamento de gráficos":
    print("Correto!")
else:
    print("Está errado!")

resposta3 = input("O que RAM significa em portguês? ")
if resposta3 == "memória de acesso aleatório":
    print("Correto!")
else:
    print("Está errado!")

resposta4 = input("O que significa PSU em portguês? ")
if resposta4 == "unidade de fonte de alimentação":
    print("Correto!")
else:
    print("Está errado!")


