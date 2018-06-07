def b(grafo):
    marcado = [False] * len(grafo)
    antecessor = [-1] * len(grafo)
    vertices = []
    for i in range(0,len(grafo)):
        if marcado[i] == False:
            vertices.append(i)
            marcado[i] = True
            while len(vertices) > 0:
                v = vertices.pop(0)
                for u in grafo.getAdj(v):
                if marcado[u] == False:
                    marcado[u] = True
                    antecessor[u] = v
                    vertices.append(u)

    return antecessor
