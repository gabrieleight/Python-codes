# Exercício de jogo da forca - Alura

def jogar():
    print("*" * 36)
    print("   Bem vindo ao jogo da Forca!   ")
    print("*" * 36)

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    
    enforcou = False
    acertou = False
    
    print(letras_acertadas)
    
    while not enforcou and not acertou:
        chute = input("Chute uma letra: ").lower().strip()
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = chute
                #print(f"Encontrei a letra '{chute}' na posição {index+1}")
            index = index + 1
    
        print(letras_acertadas)
    
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()