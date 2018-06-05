# lista 2 - algoritmos e estrutura de dados
# 

Q1 - Implemente uma classe Grafo. Para isso suponha que seus vértices são apenas
números, e que variam sempre de 0 até n (onde n é o tamanho do grafo, número de
vértices), portanto use lista de adjacências para mapear as arestas. Sua classe deve conter
pelo menos os seguintes atributos e métodos:

    ● Atributos:
      ○ Número de vértices (definido apenas inicialmente, não alterável);
      ○ Número de arestas;
      ○ Se é ou não direcionado;
      ○ Se é ou não com peso nas arestas;
    ● Métodos:
      ○ Dado dois vértices (e possivelmente um peso), adicionar uma aresta entre
      eles. (Caso o grafo não seja direcionado adicionar aresta no destino
      também).
      ○ Dado dois vértices, remover a aresta entre eles​.
      ○ Dado dois vértices, devolver (bool) se existe uma aresta que liga eles​.
      ○ Dado um vértice, devolver (int) o grau de entrada dele​.
      ○ Dado um vértice, devolver (int) o grau de saída dele​.
      ○ Dado um vértice, devolver (list) a lista de adjacência deles.

Usem esse site(https://visualgo.net/pt/graphds) para visualizar se sua classe está se comportando como deveria. Você
também pode implementar fora dela, um programa que alimenta um objeto com as arestas
vindas de um arquivo de texto como esses(https://drive.google.com/drive/folders/1uoxg328qhL1g2geFHEXTtpZac0t_RBGs).

A1 - ​Analise o trecho de código abaixo, explique seu funcionamento. Em seguida adapte
sua classe grafo para que um objeto dela seja capaz de rodar nessa função. Por fim, refaça
esse código para que ele exiba na tela a informação desejada de uma forma interessante
para o usuário e teste-o.

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


C1 - ​O código a seguir está errado​. Descubra o que o código deveria fazer, quais são os
erros e conserte-o. Altamente recomendado que nessa questão você use o debugger do
Eclipse ou alguma outra IDE com um bom debugger.

    def FUNCAOUtil(self,v,visitado):
        for i in self.grafo[v]:
            if visitado[i] == False:
                self.FUNCAOUtil(i, visitado)

    def FUNCAO(self,v):
        visitado = [False]*(len(self.grafo))
        self.FUNCAOUtil(v,visitado)
