def nome_mais_curto(lista_de_nomes):
    for i in range(len(lista_de_nomes)):
        nome_curto = lista_de_nomes[i].strip().capitalize()
        print(nome_curto)
        
lista_de_nomes = ['  ana  ', 'josé', 'Arquibado ', ' Alouhis']

nome_mais_curto(lista_de_nomes)