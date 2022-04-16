def dimensoes(matriz):
    numero_linhas = 0
    numero_colunas = 0
    for i in range(len(matriz)):
        numero_linhas += 1
    for j in range(len(matriz[0])):
        numero_colunas += 1
        
    return print(f"{numero_linhas}X{numero_colunas}")