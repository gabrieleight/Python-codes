def maiusculas(frase):
    lista_maiuscula = []
    for i in range(len(frase)):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            lista_maiuscula.append(frase[i])
        else:
            continue
        
    string_maiuscula = ''
    
    for i in lista_maiuscula:
        string_maiuscula += i
        
    return string_maiuscula