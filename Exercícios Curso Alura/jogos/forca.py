# Exercício de jogo da forca - Alura

def jogar():
    print("*" * 30)
    print("Bem vindo ao jogo da Forca!")
    print("*" * 30)

    palavra_secreta = "banana"
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0
    
    print()
    print(letras_acertadas)
    print()
    print("Você tem 6 tentativas para errar!")
    print()
    
    while not enforcou and not acertou:
        chute = input("Chute uma letra: ").strip().lower()
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = chute
                    #print(f"Encontrei a letra '{chute}' na posição {index+1}")
                index += 1
        else:
            erros += 1
            print(f"Você errou! Tentativas restantes: {6 - erros}")
            
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
    
        print(letras_acertadas)
    
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()