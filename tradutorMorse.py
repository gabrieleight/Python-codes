def IdentificaMorse(string):
    if ('.' and '-' and '/') in string or ('.' and '-') in string:
        stringMorse = True
    else:
        stringMorse = False    
    return stringMorse

def ConverteMorse(string):
    simbolos = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
              'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ': '/',
              '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}
    stringMorse = IdentificaMorse(string)
    
    elementosSimbolos = simbolos.items()
    
    if stringMorse == False:
        stringConvertida = ''
        for letra in string:
            for i in elementosSimbolos:
                if letra == i[0]:
                    stringConvertida += simbolos[letra] + ' '
                
    else:
        stringConvertida = ''
        for simbolo in string:
            pass
    
    return stringConvertida


if __name__ == "__main__":
    string = input("Digite a frase p/ converter em Morse (ou vice-versa): ").upper()
    stringMorse = ConverteMorse(string)
    print(stringMorse)