def FUNCAOUtil(self,v,visitado):
    for i in self.grafo[v]:
        if visitado[i] == False:
            self.FUNCAOUtil(i, visitado)

def FUNCAO(self,v):
    visitado = [False]*(len(self.grafo))
    self.FUNCAOUtil(v,visitado)
