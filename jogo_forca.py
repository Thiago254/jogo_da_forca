import random
#lista de palavras
palavras= ["analista", "engenheiro", "arquiteto", "desenvolvedor", "tecnico", "infraestrutura", "lider"]
#vamos usar choice que é uma função do random
palavra= random.choice(palavras)
print(palavra)

#variaveis
tentativas_inicio = 0
tentativas = 0
chance = 4
letras_escolhidas = []
estado_atual = ["_"]* len(palavras)

print("==============================")
print("==Bem vindo ao jogo da FORCA==")
print("==============================")

while tentativas_inicio <= chance and ''.join(estado_atual) != palavras:
    letra= input("\n\nQual a letra vc quer tentar?")
    
    while letra in letras_escolhidas:
        print("Você escolheu essa letra, por favor, escolha outra.")
        letra = input("\nQual a letra você quer? ")

    letras_escolhidas.append(letra)

    if letra in palavras:
        print("Parabens, vc ACERTOU")
        for i in range(len(palavras)):
            if letra == palavras[i]:
                estado_atual[i] = letra
    else:
        print("Que pena, vc ERROU")
        tentativas_inicio= tentativas+1
    #quantas tentativas ele tem
    print("Você ja fez", tentativas, "tentativas e ainda tem", chance-tentativas, "tentativas")
    #qual estado atual da palavra
    print("Esse é o estado atual: ")
    print(estado_atual)
    #quais as letras ele ja tentou
    #end=" " coloca as letras de lado uma da outra
    print("As letras que vc ja tentou são:")
    for item in letras_escolhidas:
        print(item, end=" ")
#fazer um final para o jogo
if tentativas == chance:
    print("\nVocê perdeu")
    print("Acabaram suas tentativas")
else:
    print("\nVocê ganhou, parabens")
print("A palavra era", palavras)

