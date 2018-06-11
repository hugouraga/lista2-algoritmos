from Lista import Lista

class Grafo:
    def __init__(self,quantVertices = 0,grafoDirecionado=False,pesoAresta=None):
        self.quantVertices = quantVertices
        self.listaVertices = Lista()
        self.grafoDirecionado = grafoDirecionado
        self.pesoAresta = pesoAresta
        for elemento in range(quantVertices):
            self.listaVertices.inserir([])

    def vazia(self):
        return self.quantVertices == 0

    def inseAres(self,verticeA,verticeB,grafoDirecionado=None,peso=1):
        if grafoDirecionado == False:
            self.listaVertices.inserirAresNaoDire(verticeA,verticeB)
        elif grafoDirecionado == True:
            self.listaVertices.inserirAresDire(verticeA,verticeB)

    def verifica(self,verticeA,verticeB):
        aux = self.listaVertices.verificaAresta(verticeA,verticeB)
        return aux

    def removeAresta(self,verticeA,verticeB):
        self.listaVertices.removeAresta(verticeA,verticeB)

    def grauEntrada(self,vertice):
        grau = self.listaVertices.grauEntrada(vertice)
        return grau

    def grauSaida(self,vertice):
        aux = self.listaVertices.grauSaida(vertice)
        print(aux)
        return aux

    def listaAdjacentes(self,vertice):
        lista = self.listaVertices.listaAd(vertice)
        return lista

    def __str__(self):
        #return self.listaVertices.__str__()
        aux = 0
        tamanhoLista = self.listaVertices.__len__()
        objeto = self.listaVertices.primeiro.proximo
        s = ""
        while aux < tamanhoLista:
            s += str(aux) + " = " + str(objeto.item)
            s += "\n"
            aux += 1
            objeto = objeto.proximo
        return s
    def __len__(self):
        return self.quantVertices

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

