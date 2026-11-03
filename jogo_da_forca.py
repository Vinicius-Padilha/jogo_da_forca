import random

palavras = {
    "programação": ["python", "programacao", "variavel", "funcao", "algoritmo",
                    "terminal", "teclado", "dicionario", "repositorio", "servidor"],
    "inteligência artificial": ["agente", "modelo", "prompt", "inteligencia",
                                "automacao", "neuronio", "aprendizado", "dados"],
    "frutas": ["banana", "abacaxi", "morango", "laranja", "melancia", "goiaba"],
    "animais": ["elefante", "girafa", "cachorro", "borboleta", "golfinho", "papagaio"],
    "objetos": ["janela", "mochila", "celular", "garrafa", "escola", "teclado"],
}


def escolher_palavra():
    tema = random.choice(list(palavras))
    palavra = random.choice(palavras[tema])
    return tema, palavra


tema, palavra_selecionada = escolher_palavra()


def comecar_jogo():
    tentativas = 5
    acertou = False
    letras_corretas = []
    letras_incorretas = []
    print("Bem-vindo ao jogo da Forca!")
    print(f"Dica: o tema é {tema}.")
    print(f"A palavra selecionada tem {len(palavra_selecionada)} letras.")
    print(f"Você tem {tentativas} tentativas para adivinhar a palavra.")
    while acertou == False and tentativas > 0:
        letra = input("Digite uma letra: ").lower()
        if letra in palavra_selecionada:
            letras_corretas.append(letra)
            print("Parabéns! Você acertou uma letra.")
        else:
            letras_incorretas.append(letra)
            print("Ops! Você errou uma letra.")
            tentativas -= 1
            print(f"Você ainda tem {tentativas} tentativas restantes.")
        print(f"Letras corretas: {letras_corretas}")
        escolha_chute = input("Deseja chutar a palavra? (s/n): ").lower()
        if escolha_chute == 's':
            chute = input("Digite a palavra:").lower()
            if chute == palavra_selecionada:
                acertou = True
                print(f"Parabéns! Você acertou a palavra: {palavra_selecionada}")
                break
            else:
                tentativas -= 1
                print(f"Você ainda tem {tentativas} tentativas restantes.")
            if tentativas == 0:
                print(f"Você perdeu! A palavra era: {palavra_selecionada}")
                print("Fim de jogo!")
                break

        else:
            continue


comecar_jogo()