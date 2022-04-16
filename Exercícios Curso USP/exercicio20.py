def dimensoes(matriz):
    numero_linhas = 0
    numero_colunas = 0
    for i in range(len(matriz)):
        numero_linhas += 1
    for j in range(len(matriz[0])):
        numero_colunas += 1
        
    return [numero_linhas, numero_colunas]

def soma_matrizes(m1, m2):
    dimensao_m1 = dimensoes(m1)
    dimensao_m2 = dimensoes(m2)
    
    if dimensao_m1[0] == dimensao_m2[0] and dimensao_m1[1] == dimensao_m2[1]:
        pass
    else: 
        return False
    
    m3 = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            m1[i][j] = m1[i][j] + m2[i][j]
            linha.append(m1[i][j])
        m3.append(linha)
        
    return m3
