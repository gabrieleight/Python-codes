def IdentificaMorse(string):
    if ('.' and '-' and '/') in string or ('.' and '-') in string:
        stringMorse = True
    else:
        stringMorse = False    
    return stringMorse

def ConverteMorse(string):
    simbolos = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
              'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ': '/', ',':'--..--',
              '.':'.-.-.-', '?':'..--..', '!':'-.-.--', ':':'---...', ';':'-.-.-.', '(':'-.--.', ')':'-.--.-', 'Õ':'..--.', 'É':'..-..', '=':'-...-', 'Ã':'.-.-', 'Á':'.-.-',
              '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}
    stringMorse = IdentificaMorse(string)
    
    elementosSimbolos = simbolos.items()
    stringConvertida = ''
    
    if stringMorse == False:
        for letra in string:
            for i in elementosSimbolos:
                if letra == i[0]:
                    stringConvertida += simbolos[letra] + ' '
                
    else:
        string += ' '
        stringNaoConvertida = ''
        for caractere in string:
            stringNaoConvertida += caractere
            if caractere == ' ':
                stringNaoConvertida = stringNaoConvertida[: -1]
                for i in elementosSimbolos:
                    if i[1] == stringNaoConvertida:
                        stringConvertida += i[0]
                stringNaoConvertida = ''
                continue
            
    
    return stringConvertida


if __name__ == "__main__":
    print('*' * 40)
    print('*' * 7, 'Tradutor de Código Morse', '*' * 7)
    print('*' * 6, 'Criado por Gabriel Gilberto', '*' * 5)
    print('*' * 13, 'Versão 1.2.1', '*' * 13)
    print('*' * 40)
    print()
    string = input("Digite uma comunicação curta p/ converter em Morse (ou vice-versa): \n").upper()
    stringMorse = ConverteMorse(string)
    print(stringMorse)
    print()
    print('*' * 14,'Thank you!', '*' * 14)
