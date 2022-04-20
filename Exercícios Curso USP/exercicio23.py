def menor_nome(nomes):
    lista_tamanhos = []
    for i in nomes:
        lista_tamanhos.append(len(i.strip(' ')))
    menor = min(lista_tamanhos)
    for i in nomes:
        j = i.strip()
        if len(j) == menor:
            return j.capitalize()