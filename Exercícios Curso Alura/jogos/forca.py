# Exercício de jogo da forca - Alura
import random

def jogar():
    print("*" * 27)
    print("Bem vindo ao jogo da Forca!")
    print("*" * 27)
    
    with open("Exercícios Curso Alura\jogos\palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())
    
    palavra_secreta = palavras[random.randrange(0, len(palavras))].lower() 
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