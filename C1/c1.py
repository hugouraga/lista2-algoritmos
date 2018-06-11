def FUNCAOUtil(grafo, v, visitado):
    visitado[v] = True
    adjacentes = grafo.listaAdjacentes(v)
    print(adjacentes)
    for i in adjacentes:
        indice = i[0]
        if visitado[indice] is False:
            FUNCAOUtil(grafo, indice, visitado)
    return visitado

def FUNCAO(grafo,v):
    visitado = [False] * len(grafo)
    FUNCAOUtil(grafo, v, visitado)
    return visitado
